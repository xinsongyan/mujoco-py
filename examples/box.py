#!/usr/bin/env python3
"""
Example of box drop from the air.
"""
from mujoco_py import load_model_from_xml, MjSim, MjViewer
import math
import os




MODEL_XML = """
<?xml version="1.0" ?>
<mujoco>
   <worldbody>
      <light diffuse=".5 .5 .5" pos="0 0 3" dir="0 0 -1"/>    
      <geom type="plane" size="1 1 0.1" rgba=".9 0 0 1"/>
      <body pos="0 0 1">
         <joint type="free"/>
         <geom type="box" size=".1 .2 .3" rgba="0 .9 0 1"/>
      </body>
   </worldbody>
</mujoco>
"""


model = load_model_from_xml(MODEL_XML)
sim = MjSim(model)
viewer = MjViewer(sim)
t = 0
while True:
    t += 1
    sim.step()
    viewer.render()
    if t > 100 and os.getenv('TESTING') is not None:
        break