# %%
import h5py

# %%
# Use quad ss/zpk model from https://dcc.ligo.org/LIGO-T2300299
f = h5py.File("/Users/ddb/Downloads/quad_ss_zpk_damped_and_undamped (3).h5", "r")
nf = h5py.File("../src/finesse_ligo/data/suspensions/quad_damped_zpk.h5", "w")
# %% We only need to store drives to L3 stage for Finesse really
outputs = ["L3.disp.L", "L3.disp.P", "L3.disp.Y"]
dest = nf.create_group("damped/zpk")
# %%
for output in outputs:
    f.copy(f"damped/zpk/{output}", dest)
# %%
f.close()
nf.close()
# %%
