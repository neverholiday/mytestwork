import numpy as np
from scarakinematics import SCARAKinematics

from pprint import pprint

kinematics = SCARAKinematics()

position_start = np.array([[200],[400],[300]]).reshape(-1)
orientation_start = np.array([[np.pi],[0],[0]]).reshape(-1)
# 
q_previous = np.array([0,0,0,0,0,0,0])
q_1 = kinematics.inverseKinematicsCalculate(position_start, orientation_start, "rpy",q_previous)
pprint(q_1)

position_end = np.array([[600],[20],[500]]).reshape(-1)
orientation_end = np.array([[0],[np.pi/2],[0]]).reshape(-1)
q_2 = kinematics.inverseKinematicsCalculate(position_end, orientation_end, "rpy",q_1)
pprint(q_2)
