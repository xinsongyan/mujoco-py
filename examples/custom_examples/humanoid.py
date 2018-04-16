#!/usr/bin/env python3
"""
Load claw.xml from xmls folder.
"""
from mujoco_py import load_model_from_xml, load_model_from_path, MjSim, MjViewer
import math
import os
import numpy as np

np.set_printoptions(precision=3)


def print_state(state):
    # qpos(28) = [x, y, z, qw, qx, qy, qz, q(21)]
    # qvel(27) = [xd, yd, zd, omega_x, omega_y, omega_z, qd(21)]
    time, qpos, qvel, act, udd_state = state.time, state.qpos, state.qvel, state.act, state.udd_state
    print("t: %5.3f" % time)
    print("qpos: ", qpos.shape, qpos)
    print("qvel: ", qvel.shape, qvel)


def mass_center(model, sim):
    mass = np.expand_dims(model.body_mass, 1)
    xpos = sim.data.xipos
    com_pos = (np.sum(mass * xpos, 0) / np.sum(mass))
    return com_pos


model = load_model_from_path("../../xmls/humanoid.xml")
sim = MjSim(model)
viewer = MjViewer(sim)
t = 0
while True:
    state = sim.get_state()
    print_state(state)
    print("com: ", mass_center(model, sim))
    t += 1
    sim.step()
    viewer.render()
    if t > 100 and os.getenv('TESTING') is not None:
        break
