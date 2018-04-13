#!/usr/bin/env python3
"""
Load claw.xml from xmls folder.
"""
from mujoco_py import load_model_from_xml, load_model_from_path, MjSim, MjViewer
import math
import os



model = load_model_from_path("../../xmls/humanoid.xml")
sim = MjSim(model)
viewer = MjViewer(sim)
t = 0
while True:
    t += 1
    sim.step()
    viewer.render()
    if t > 100 and os.getenv('TESTING') is not None:
        break