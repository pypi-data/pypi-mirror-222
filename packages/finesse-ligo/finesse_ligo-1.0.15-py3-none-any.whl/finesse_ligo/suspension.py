from finesse.components import Connector, NodeType, NodeDirection
from finesse.components.general import LocalDegreeOfFreedom
from finesse.components.mechanical import (
    MIMOTFWorkspace,
    get_mechanical_port,
)
from finesse.components.workspace import ConnectorWorkspace
import importlib.resources as pkg_resources
import numpy as np
from finesse.utilities.misc import reduce_getattr

TRIPLE_DATA = (
    None  # Global for storing the triple pendulum data so we don't keep reloading it
)


QUAD_DATA = (
    None  # Global for storing the triple pendulum data so we don't keep reloading it
)


def get_quad_zpk_plant(*extract_nodes):
    import importlib
    import h5py
    from copy import copy

    data_path = importlib.resources.path(
        "finesse_ligo.data.suspensions",
        "quad_damped_zpk.h5",
    )

    omap = {
        ".disp.P": "_pitch",
        ".disp.Y": "_yaw",
        ".disp.L": "_z",
    }
    imap = {
        ".drive.P": "_F_pitch",
        ".drive.Y": "_F_yaw",
        ".drive.L": "_F_z",
        ".disp.P": "_pitch",
        ".disp.Y": "_yaw",
        ".disp.L": "_z",
    }
    zpk_plant = {}
    allowed_nodes = set(extract_nodes)
    with h5py.File(data_path, mode="r") as f:
        for O in f["damped/zpk"].keys():
            o = copy(O)
            for a, b in omap.items():
                o = o.replace(a, b)
            for I in f["damped/zpk/"][O].keys():
                Isplit = I.split(".")
                if Isplit[0] in allowed_nodes:
                    Itest = "." + ".".join(Isplit[1:])
                    if Itest in imap:
                        z = f["damped/zpk"][O][I]["z"][:]
                        p = f["damped/zpk"][O][I]["p"][:]
                        k = f["damped/zpk"][O][I]["k"][()]
                        i = copy(I)
                        for a, b in imap.items():
                            i = i.replace(a, b)
                        zpk_plant[(o, i)] = (z, p, k)
    return zpk_plant


def node_2_ligo_node(io, node, name_map={}):
    """Maps a Finesse node to a LIGO suspension model degree of freedom string, i.e.
    in.gnd.disp.L."""
    if node.name.startswith("F_"):
        _type = "drive"
        dof = node.name[2:]
    else:
        _type = "disp"
        dof = node.name
    mapp = {"z": "L", "yaw": "Y", "pitch": "P"}
    return "{io}.{port}.{_type}.{dof}".format(
        io=io,
        port=name_map.get(node.port.name, node.port.name),
        _type=_type,
        dof=mapp[dof.lower()],
    )


class QUADSuspension(Connector):
    """A mechanics element that represents a LIGO Quad suspension. This uses the damped
    ZPK model of the full state space model. Based on the data in
    https://dcc.ligo.org/LIGO-T2300299. Local degrees of freedom for forcing L3 and L2
    stages and reading out the L3 motion are provided:

        - dofs.L2_F_pitch, dofs.L2_F_yaw, dofs.L2_F_z
        - dofs.L3_F_pitch, dofs.L3_F_yaw, dofs.L3_F_z

    Also provided are nodes for driving L1 and M0 as well as
    the suspoint (gnd) motion. Only couplings between each stage
    and L3 are included.

    Parameters
    ----------
    name : str
        Name of the suspension element
    connect_to : Port
        A mechanical signal port of a mirror component to suspend.
    """

    def __init__(self, name, connect_to):
        super().__init__(name)

        mech_port = get_mechanical_port(connect_to)
        # Add motion and force nodes to mech port.
        # Here we duplicate the already created mechanical
        # nodes in some other connector element
        self._add_port("L3", NodeType.MECHANICAL)
        self.L3._add_node("z", None, mech_port.z)
        self.L3._add_node("yaw", None, mech_port.yaw)
        self.L3._add_node("pitch", None, mech_port.pitch)
        self.L3._add_node("F_z", None, mech_port.F_z)
        self.L3._add_node("F_yaw", None, mech_port.F_yaw)
        self.L3._add_node("F_pitch", None, mech_port.F_pitch)
        # Penultimate mass port
        self._add_port("L2", NodeType.MECHANICAL)
        self.L2._add_node("F_z", NodeDirection.BIDIRECTIONAL)
        self.L2._add_node("F_yaw", NodeDirection.BIDIRECTIONAL)
        self.L2._add_node("F_pitch", NodeDirection.BIDIRECTIONAL)
        # Intermediate mass port
        self._add_port("L1", NodeType.MECHANICAL)
        self.L1._add_node("F_z", NodeDirection.BIDIRECTIONAL)
        self.L1._add_node("F_yaw", NodeDirection.BIDIRECTIONAL)
        self.L1._add_node("F_pitch", NodeDirection.BIDIRECTIONAL)
        # topmass
        self._add_port("M0", NodeType.MECHANICAL)
        self.M0._add_node("F_z", NodeDirection.BIDIRECTIONAL)
        self.M0._add_node("F_yaw", NodeDirection.BIDIRECTIONAL)
        self.M0._add_node("F_pitch", NodeDirection.BIDIRECTIONAL)
        # Suspension point ground port
        self._add_port("gnd", NodeType.MECHANICAL)
        self.gnd._add_node("z", NodeDirection.BIDIRECTIONAL)
        self.gnd._add_node("yaw", NodeDirection.BIDIRECTIONAL)
        self.gnd._add_node("pitch", NodeDirection.BIDIRECTIONAL)

        global QUAD_DATA
        if QUAD_DATA is None:
            QUAD_DATA = get_quad_zpk_plant("L3", "L2", "L1", "M0", "gnd")

        self.zpk_plant = QUAD_DATA
        self.zpks = []
        self._ois = []

        for (output, input), zpk in self.zpk_plant.items():
            i = reduce_getattr(self, input.replace("_", ".", 1))
            o = reduce_getattr(self, output.replace("_", ".", 1))
            self._ois.append((o, i))
            self._register_node_coupling(
                f"{input}_to_{output}",
                i,
                o,
            )
            self.zpks.append(zpk)  # store ordered zpks

        import types

        self.dofs = types.SimpleNamespace()
        self.dofs.L3_F_z = LocalDegreeOfFreedom(
            f"{self.name}.dofs.L3_F_z", None, self.L3.F_z, 1, AC_OUT=self.L3.z
        )
        self.dofs.L3_F_pitch = LocalDegreeOfFreedom(
            f"{self.name}.dofs.L3_F_pitch",
            None,
            self.L3.F_pitch,
            1,
            AC_OUT=self.L3.pitch,
        )
        self.dofs.L3_F_yaw = LocalDegreeOfFreedom(
            f"{self.name}.dofs.L3_F_yaw", None, self.L3.F_yaw, 1, AC_OUT=self.L3.yaw
        )
        self.dofs.L2_F_z = LocalDegreeOfFreedom(
            f"{self.name}.dofs.L2_F_z", None, self.L2.F_z, 1, AC_OUT=self.L3.z
        )
        self.dofs.L2_F_pitch = LocalDegreeOfFreedom(
            f"{self.name}.dofs.L2_F_pitch",
            None,
            self.L2.F_pitch,
            1,
            AC_OUT=self.L3.pitch,
        )
        self.dofs.L2_F_yaw = LocalDegreeOfFreedom(
            f"{self.name}.dofs.L2_F_yaw", None, self.L2.F_yaw, 1, AC_OUT=self.L3.yaw
        )

    def _get_workspace(self, sim):
        if sim.signal:
            refill = sim.model.fsig.f.is_changing
            ws = SimplifiedQUADWorkspace(self, sim)
            ws.signal.add_fill_function(self.fill, refill)
            zpks_to_use = []
            for zpk, (output, input) in zip(self.zpks, self._ois):
                if (
                    output.full_name in sim.signal.nodes
                    and input.full_name in sim.signal.nodes
                ):
                    zpks_to_use.append(zpk)
            ws.zpks = [
                (np.asarray(z), np.asarray(p), float(k)) for z, p, k in zpks_to_use
            ]

            return ws
        else:
            return None

    def fill(self, ws):
        s = 2j * np.pi * ws.sim.model_settings.fsig

        for i, (z, p, k) in enumerate(ws.zpks):
            H = k * np.prod(s - z) / np.prod(s - p)
            with ws.sim.signal.component_edge_fill3(
                ws.owner_id,
                i,
                0,
                0,
            ) as mat:
                mat[:] = H


LIGOQuadSuspension = QUADSuspension


class MIMOSSWorkspace(ConnectorWorkspace):
    pass


class LIGOTripleSuspension(Connector):
    """A mechanics element that represents a LIGO Triple suspension.

    LIGO Triple version 20140304TMproductionTM
    generate_TRIPLE_Model_Production.m
    SVN REV 10312
    https://redoubt.ligo-wa.caltech.edu/svn/sus/trunk/QUAD/Common/MatlabTools

    The Matlab code above was run to generate the state space model which
    was exported to Python. The Python Controls toolbox was then used
    to generate the transfer-function coefficients and stored in a Pickled
    file which this object accesses.

    The component being suspended must have a mechanical port with
    nodes z, pitch, and yaw and forces F_z, F_pitch, and F_yaw.

    This mechanics element provides access to the ground (`gnd` port)
    and penultimate (`pum` port) mass stages for injecting in
    displacement noise or feedback signals for controlling the test
    (`tst` port) mass.
    """

    def __init__(self, name, connect_to):
        super().__init__(name)
        mech_port = get_mechanical_port(connect_to)
        # Add motion and force nodes to mech port.
        # Here we duplicate the already created mechanical
        # nodes in some other connector element
        self._add_port("tst", NodeType.MECHANICAL)
        self.tst._add_node("z", None, mech_port.z)
        self.tst._add_node("yaw", None, mech_port.yaw)
        self.tst._add_node("pitch", None, mech_port.pitch)
        self.tst._add_node("F_z", None, mech_port.F_z)
        self.tst._add_node("F_yaw", None, mech_port.F_yaw)
        self.tst._add_node("F_pitch", None, mech_port.F_pitch)
        # Suspension point ground port
        self._add_port("gnd", NodeType.MECHANICAL)
        self.gnd._add_node("z", NodeDirection.BIDIRECTIONAL)
        self.gnd._add_node("yaw", NodeDirection.BIDIRECTIONAL)
        self.gnd._add_node("pitch", NodeDirection.BIDIRECTIONAL)
        # Penultimate mass port
        self._add_port("pum", NodeType.MECHANICAL)
        self.pum._add_node("F_z", NodeDirection.BIDIRECTIONAL)
        self.pum._add_node("F_yaw", NodeDirection.BIDIRECTIONAL)
        self.pum._add_node("F_pitch", NodeDirection.BIDIRECTIONAL)

        global TRIPLE_DATA
        if TRIPLE_DATA is None:
            import bz2
            import control
            import pickle
            from . import data

            # Load some data in and process it
            ss = pickle.loads(
                bz2.decompress(
                    pkg_resources.read_binary(data, "ligo_triple_suspension_ss.pbz2")
                )
            )
            tfs = control.ss2tf(
                ss["A"],
                ss["B"],
                ss["C"],
                ss["D"],
            )
            TRIPLE_DATA = (tfs, ss["inputs"], ss["outputs"])

        self.tfs, self.inputs, self.outputs = TRIPLE_DATA

        # Add in connections for GND/PUM coupling into TST
        for i in self.gnd.nodes + self.pum.nodes:
            for o in self.tst.nodes:
                # Sus model computes how PUM/GND couple
                # into TST displacement
                if not o.name.startswith("F_"):
                    self._register_node_coupling(
                        f"{i.full_name}__{o.full_name}".replace(".", "_"), i, o
                    )
        # Add in TST drives to TST displacements
        # coupling and cross-coupling
        for i in self.tst.nodes:
            if i.name.startswith("F_"):  # drives only
                for o in self.tst.nodes:
                    if not o.name.startswith("F_"):  # disp only
                        self._register_node_coupling(
                            f"{i.full_name}__{o.full_name}".replace(".", "_"), i, o
                        )

        # Define typical degrees of freedom for this component
        import types

        self.dofs = types.SimpleNamespace()
        self.dofs.tst_z = LocalDegreeOfFreedom(
            f"{self.name}.dofs.tst_z", None, self.tst.z, 1
        )
        self.dofs.tst_F_z = LocalDegreeOfFreedom(
            f"{self.name}.dofs.tst_F_z", None, self.tst.F_z, 1
        )
        self.dofs.pum_F_z = LocalDegreeOfFreedom(
            f"{self.name}.dofs.pum_F_z", None, self.pum.F_z, 1
        )
        self.dofs.gnd_z = LocalDegreeOfFreedom(
            f"{self.name}.dofs.gnd_z", None, self.gnd.z, 1
        )

    def _get_workspace(self, sim):
        if sim.signal:
            refill = sim.model.fsig.f.is_changing  # Need to recompute H(f)
            N = len(self._registered_connections)
            ws = MIMOTFWorkspace(self, sim, refill, N)
            ws.set_denominator(self.tfs.den[0][0])
            name_map = {n.port.name: "tst" for n in self.tst.nodes}

            # Setup the TFs for filling
            for j, (i, o) in enumerate(self._registered_connections.values()):
                i = self.nodes[i]
                o = self.nodes[o]
                idx = self.inputs[node_2_ligo_node("in", i, name_map)]
                odx = self.outputs[node_2_ligo_node("out", o, name_map)]
                ws.add_numerator(self.tfs.num[odx][idx])

            return ws
        else:
            return None


class SimplifiedQUADWorkspace(ConnectorWorkspace):
    pass


class SimplifiedQUAD(Connector):
    """A suspension that models the quad suspension as a double suspension with the PUM
    and TST stage. Models multiple poles and zeros for the z, yaw, or pitch motion of an
    optic. The user must ensure that minus signs are correct for this transfer function
    as well as defining complex conjugae pairs for physically correct behaviour.

    Notes
    -----

    ZPK terms are in units of radians.
    ZPK determined by fitting unlocked IFO measurement of test mass L2/L3 and L3/L3 TF at LHO
    Has been confirmed to match LLO sus TFs as well. Units are torque (Nm) to angle (rad).
    These simplified ZPKs were made by Elenna Capote in 2022-2023 for studying ASC performance.
    However it was found in July 2023 (Hot Stuff workshop, Adelaide) that a full SUS model
    is needed to properly predict the location of ASC optical springs. The suspicion is that
    the reduced order ZPK model either does not have the correct moment of inertia, or the
    due to Courant's nodal domain theorem (https://dcc.ligo.org/LIGO-T2300150) and us not
    having enough poles here that interact correctly when modified by radiation pressure.

    Parameters
    ----------
    name : str
        Element name
    connected_to : Element or mechanical port
        Mechanical port or element to attach this suspension to
    """

    # L2 torque in [Nm] to L3 angle [rad]
    z_l2p_l3p = np.array([-1.795683e-01 + 2.878020e00j, -1.795683e-01 - 2.878020e00j])
    p_l2p_l3p = np.array(
        [
            -1.380233e-01 + 2.687744e00j,
            -1.380233e-01 - 2.687744e00j,
            -9.424111e-02 + 3.546816e00j,
            -9.424111e-02 - 3.546816e00j,
            -2.672733e-01 + 9.355654e00j,
            -2.672733e-01 - 9.355654e00j,
        ]
    )
    k_l2p_l3p = 9.279149e01

    l2_ct2tau = 7.629e-5 * 0.268e-3 * 0.0309

    # L3 torque in [Nm] to L3 angle [rad]
    z_l3p_l3p = np.array(
        [
            -1.679986e-01 + 2.806124e00j,
            -1.679986e-01 - 2.806124e00j,
            -2.576084e-01 + 6.978624e00j,
            -2.576084e-01 - 6.978624e00j,
        ]
    )
    p_l3p_l3p = np.array(
        [
            -1.223585e-01 + 2.670807e00j,
            -1.223585e-01 - 2.670807e00j,
            -9.436692e-02 + 3.554246e00j,
            -9.436692e-02 - 3.554246e00j,
            -2.840980e-01 + 9.335571e00j,
            -2.840980e-01 - 9.335571e00j,
        ]
    )
    k_l3p_l3p = 2.665177e00

    # L2 torque in [Nm] to L3 angle [rad]
    z_l2y_l3y = np.array([-9.722684e-01 + 1.152619e01j, -9.722684e-01 - 1.152619e01j])
    p_l2y_l3y = np.array(
        [
            -1.709761e-01 + 3.811943e00j,
            -1.709761e-01 - 3.811943e00j,
            -1.977740e-01 + 8.614734e00j,
            -1.977740e-01 - 8.614734e00j,
            -1.446690e00 + 1.702979e01j,
            -1.446690e00 - 1.702979e01j,
        ]
    )
    k_l2y_l3y = 1.281647e02

    l2_ct2tau = 7.629e-5 * 0.268e-3 * 0.0309

    # L3 torque in [Nm] to L3 angle [rad]
    z_l3y_l3y = np.array([-2.162474e-01 + 6.886976e00j, -2.162474e-01 - 6.886976e00j])
    p_l3y_l3y = np.array(
        [
            -1.776369e-01 + 3.815934e00j,
            -1.776369e-01 - 3.815934e00j,
            -2.184140e-01 + 8.600263e00j,
            -2.184140e-01 - 8.600263e00j,
        ]
    )
    k_l3y_l3y = 2.409108e00

    def __init__(self, name, connected_to):
        super().__init__(name)
        self.__connected_to = connected_to
        mech_port = get_mechanical_port(connected_to)
        zpk_plant = {}
        zpk_plant["L3_pitch", "L3_F_pitch"] = (
            self.z_l3p_l3p,
            self.p_l3p_l3p,
            self.k_l3p_l3p,
        )
        zpk_plant["L3_pitch", "L2_F_pitch"] = (
            self.z_l2p_l3p,
            self.p_l2p_l3p,
            self.k_l2p_l3p,
        )

        self.zpk_plant = zpk_plant

        # Add motion and force nodes to mech port.
        # Here we duplicate the already created mechanical
        # nodes in some other connector element
        self._add_port("mech", NodeType.MECHANICAL)
        self.mech._add_node("L3_z", None, mech_port.z)
        self.mech._add_node("L3_F_z", None, mech_port.F_z)
        self.mech._add_node("L3_yaw", None, mech_port.yaw)
        self.mech._add_node("L3_F_yaw", None, mech_port.F_yaw)
        self.mech._add_node("L3_pitch", None, mech_port.pitch)
        self.mech._add_node("L3_F_pitch", None, mech_port.F_pitch)

        self.mech._add_node("L2_F_z", None)
        self.mech._add_node("L2_F_yaw", None)
        self.mech._add_node("L2_F_pitch", None)

        # Define typical degrees of freedom for this component
        import types

        self.dofs = types.SimpleNamespace()
        # TST dofs to test mass motion
        self.dofs.L3_F_z = LocalDegreeOfFreedom(
            f"{self.name}.dofs.L3_F_z",
            mech_port.component.phi,
            self.mech.L3_F_z,
            1,
            AC_OUT=mech_port.z,
        )
        self.dofs.L3_F_yaw = LocalDegreeOfFreedom(
            f"{self.name}.dofs.L3_F_yaw",
            mech_port.component.xbeta,
            self.mech.L3_F_yaw,
            1,
            AC_OUT=mech_port.yaw,
        )
        self.dofs.L3_F_pitch = LocalDegreeOfFreedom(
            f"{self.name}.dofs.L3_F_pitch",
            mech_port.component.ybeta,
            self.mech.L3_F_pitch,
            1,
            AC_OUT=mech_port.pitch,
        )
        # PUM dofs to test mass motion
        self.dofs.L2_F_z = LocalDegreeOfFreedom(
            f"{self.name}.dofs.L2_F_z",
            mech_port.component.phi,
            self.mech.L2_F_z,
            1,
            AC_OUT=mech_port.z,
        )
        self.dofs.L2_F_yaw = LocalDegreeOfFreedom(
            f"{self.name}.dofs.L2_F_yaw",
            mech_port.component.xbeta,
            self.mech.L2_F_yaw,
            1,
            AC_OUT=mech_port.yaw,
        )
        self.dofs.L2_F_pitch = LocalDegreeOfFreedom(
            f"{self.name}.dofs.L2_F_pitch",
            mech_port.component.ybeta,
            self.mech.L2_F_pitch,
            1,
            AC_OUT=mech_port.pitch,
        )

        self.zpks = []
        self._ois = []

        for (output, input), zpk in zpk_plant.items():
            i = getattr(self.mech, input)
            o = getattr(self.mech, output)
            self._ois.append((o, i))
            self._register_node_coupling(
                f"{input}_to_{output}",
                i,
                o,
            )
            self.zpks.append(zpk)  # store ordered zpks

    def _get_workspace(self, sim):
        if sim.signal:
            refill = sim.model.fsig.f.is_changing
            ws = SimplifiedQUADWorkspace(self, sim)
            ws.signal.add_fill_function(self.fill, refill)
            zpks_to_use = []
            for zpk, (output, input) in zip(self.zpks, self._ois):
                if (
                    output.full_name in sim.signal.nodes
                    and input.full_name in sim.signal.nodes
                ):
                    zpks_to_use.append(zpk)
            ws.zpks = [
                (np.asarray(z), np.asarray(p), float(k)) for z, p, k in zpks_to_use
            ]

            return ws
        else:
            return None

    def fill(self, ws):
        s = 2j * np.pi * ws.sim.model_settings.fsig

        for i, (z, p, k) in enumerate(ws.zpks):
            H = k * np.prod(s - z) / np.prod(s - p)
            with ws.sim.signal.component_edge_fill3(
                ws.owner_id,
                i,
                0,
                0,
            ) as mat:
                mat[:] = H
