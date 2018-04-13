#!/usr/bin/env python3
"""
Shows how to toss a capsule to a container.
"""
from mujoco_py import load_model_from_path, MjSim, MjViewer
import os
import numpy as np

np.set_printoptions(precision=5)
def print_state(state):
    time, qpos, qvel, act, udd_state = state.time, state.qpos, state.qvel, state.act, state.udd_state
    print("t: %5.3f" %time)
    print("qpos: ", qpos)
    print("qvel: ", qvel)



model = load_model_from_path("../../xmls/tosser.xml")
sim = MjSim(model)

viewer = MjViewer(sim)


sim_state = sim.get_state()

while True:
    sim.set_state(sim_state)

    for i in range(1000):
        state = sim.get_state()
        # time, qpos, qvel, act, udd_state = state.time, state.qpos, state.qvel, state.act, state.udd_state
        # print(time, qpos, qvel)
        print_state(state)
        if i < 150:
            sim.data.ctrl[0] = -0.0
            sim.data.ctrl[1] = -0.0
        else:
            sim.data.ctrl[0] = -1.0
            sim.data.ctrl[1] = -1.0
        sim.step()
        viewer.render()

    if os.getenv('TESTING') is not None:
        break
