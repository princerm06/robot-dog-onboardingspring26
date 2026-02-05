import time
from pathlib import Path
import mujoco
import mujoco.viewer

print("START visualize_dog.py")

xml_path = Path(__file__).with_name("dog.xml").resolve()
print("dog.xml:", xml_path)
print("exists:", xml_path.exists())
print("size:", xml_path.stat().st_size if xml_path.exists() else -1)

model = mujoco.MjModel.from_xml_path(str(xml_path))
data = mujoco.MjData(model)
print("LOADED. bodies:", model.nbody, "geoms:", model.ngeom, "joints:", model.njnt)

print("Launching viewer in 2s...")
time.sleep(2)

with mujoco.viewer.launch_passive(model, data) as viewer:
    print("Viewer launched. Looping...")
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()
        time.sleep(0.002)

print("Viewer closed, exiting.")
