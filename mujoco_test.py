import mujoco
import mujoco.viewer

XML = """
<mujoco>
  <option timestep="0.002"/>
  <worldbody>
    <light diffuse="1 1 1" pos="0 0 3"/>
    <geom type="plane" size="5 5 0.1" rgba="0.9 0.9 0.9 1"/>
    <body pos="0 0 0.2">
      <joint type="free"/>
      <geom type="sphere" size="0.05" rgba="0.2 0.4 0.9 1"/>
    </body>
  </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(XML)
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()
