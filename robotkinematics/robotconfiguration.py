import numpy as np
# TODO : Use configobj for set configuration of robot later

class RobotConfiguration:
    ground_base = 0 # Constant
    # Unit of lenght/height is cm
    h1 = 10
    h2 = 3
    h3 = 3
    l1 = 47
    l2 = 32
    l3 = 3
    l4 = 0

    type_of_joint = [0,1,0,1,1,1,1]
    dh_table = np.array([[0,h1,0,0],
                        [0,0,0,0],
                        [0,0,l1,0],
                        [0,-h2,l2,0],
                        [0,-h3,0,np.pi/2],
                        [0,0,0,np.pi/2],
                        [0,l3+l4,0,0]])
    