#!/usr/bin/env python3
"""
This model is a 7 degree-of-freedom arm "holding" a string with a cylinder attached at the other end.
The string is implemented as a tendon with length limits.
There is ball joint at the shoulder and pairs of hinge joints at the elbow and wrist.
The box inside the cylinder indicates a free "joint".
The outer body element in the XML is the required worldbody.
Note that using multiple joints between two bodies does not require creating dummy bodies.
"""
from mujoco_py import load_model_from_xml, MjSim, MjViewer
import math
import os




MODEL_XML = """
<?xml version="1.0" ?>
<mujoco model="arm">
    <compiler coordinate="global"/>
    <default>
        <geom rgba=".8 .6 .4 1"/>
    </default>
    <asset>
        <texture type="skybox" builtin="gradient" rgb1="1 1 1" rgb2=".6 .8 1" 
                 width="256" height="256"/>
    </asset>
    <worldbody>
        <light pos="0 1 1" dir="0 -1 -1" diffuse="1 1 1"/>
        <body>
            <geom type="capsule" fromto="0 0 1  0 0 0.6" size="0.06"/>
            <joint type="ball" pos="0 0 1"/>
            <body>
                <geom type="capsule" fromto="0 0 0.6  0.3 0 0.6" size="0.04"/>
                <joint type="hinge" pos="0 0 0.6" axis="0 1 0"/>      
                <joint type="hinge" pos="0 0 0.6" axis="1 0 0"/>      
                <body>
                    <geom type="ellipsoid" pos="0.4 0 0.6" size="0.1 0.08 0.02"/>
                    <site name="end1" pos="0.5 0 0.6" type="sphere" size="0.01"/>
                    <joint type="hinge" pos="0.3 0 0.6" axis="0 1 0"/>        
                    <joint type="hinge" pos="0.3 0 0.6" axis="0 0 1"/>        
                </body>
            </body>
        </body>
        <body>
            <geom type="cylinder" fromto="0.5 0 0.2  0.5 0 0" size="0.07"/>
            <site name="end2" pos="0.5 0 0.2" type="sphere" size="0.01"/>
            <joint type="free"/>
        </body>
    </worldbody>
    <tendon>
        <spatial limited="true" range="0 0.6" width="0.005">
            <site site="end1"/>
            <site site="end2"/>
        </spatial>
    </tendon>
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