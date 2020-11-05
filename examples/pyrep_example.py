from os.path import dirname, join, abspath
import numpy as np
import random
from pyrep import PyRep
from pyrep.robots.arms.ur3 import UR3
from pyrep.robots.arms.panda import Panda
from pyrep.robots.end_effectors.baxter_gripper import BaxterGripper
from pyrep.robots.end_effectors.panda_gripper import PandaGripper

# SCENE_FILE = join(dirname(abspath(__file__)), 'scene_ur3_reinforcement_learning_env.ttt')
SCENE_FILE = join(dirname(abspath(__file__)), 'scene_reinforcement_learning_env.ttt')

pr = PyRep()
# Launch the application with a scene file that contains a robot
pr.launch(SCENE_FILE, headless=False) 
pr.start()  # Start the simulation

arm = Panda()
gripper = PandaGripper()

arm.set_control_loop_enabled(False)
# arm.set_motor_locked_at_zero_velocity(True)

for i in range(300):
    arm.set_joint_target_velocities(list(np.random.uniform(-0.5, 0.5, size=(7,))))
    pr.step()

for i in range(100):
    gripper_state = random.random()
    done = False
    # Open the gripper to gripper_state (1 is open 0 is closed) at a velocity of 0.04.
    while not done:
        done = gripper.actuate(gripper_state, velocity=0.04)
        pr.step()
    
pr.stop()  # Stop the simulation
pr.shutdown()  # Close the application