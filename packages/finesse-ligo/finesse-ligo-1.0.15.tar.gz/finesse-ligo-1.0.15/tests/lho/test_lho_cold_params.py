# %%
from finesse.ligo.lho import make_O4_lho
import numpy as np
import pytest


@pytest.fixture()
def lho_model():
    lho = make_O4_lho()
    lho.beam_trace()
    return lho


def test_gouy_phases(lho_model):
    assert np.allclose(lho_model.cavSRX.gouy_x, 26.45, atol=1e-2)
    assert np.allclose(lho_model.cavSRY.gouy_x, 29.89, atol=1e-2)
    assert np.allclose(lho_model.cavSRX.gouy_y, 19.65, atol=1e-2)
    assert np.allclose(lho_model.cavSRY.gouy_y, 23.82, atol=1e-2)

    single_pass = {
        "x": [17.99, 16.52],
        "y": [17.59, 15.58],
    }
    for direction in ["x", "y"]:
        parm = lho_model.propagate_beam(
            from_node="ITMX.p1.i", to_node="ITMX.p2.o", direction=direction
        )
        p1 = lho_model.propagate_beam(
            from_node="ITMX.p2.o",
            to_node="SRM.p1.i",
            q_in=parm.q(lho_model.ITMX.p2.o),
            direction=direction,
        )
        p2 = lho_model.propagate_beam(
            from_node="SRM.p1.i",
            to_node="ITMX.p2.o",
            q_in=p1.q(lho_model.SRM.p1.i),
            direction=direction,
        )
        assert np.allclose(
            p1.acc_gouy_up_to(lho_model.SRM.p1.i), single_pass[direction][0], atol=1e-2
        )
        assert np.allclose(
            p2.acc_gouy_up_to(lho_model.ITMX.p2.o), single_pass[direction][1], atol=1e-2
        )


def test_physical_lengths(lho_model):
    # E1300128-v4
    assert np.allclose(lho_model.lSRC.value.eval(), 56008.5e-3, atol=1e-3)
    assert np.allclose(lho_model.lPRC.value.eval(), 57651.3e-3, atol=1e-3)
