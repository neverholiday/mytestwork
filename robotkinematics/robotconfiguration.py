import numpy as np
# TODO : Use configobj for set configuration of robot later

class RobotConfiguration:
    ground_base = 0 # Constant
    # Unit of lenght/height is cm
    h1 = 99.90
    h2 = 8
    l1 = 44.12
    h3 = 100
    l2 = 500
    h4 = 42.15
    l3 = 320
    h5 = 43.48
    h67 = 93.99

    q_init = [0,0,0,0,0,0,0]

    type_of_joint = [0,1,0,1,1,1,1]
    
    dh_table = np.array([[0,  h1,   0,   0],
                        [0,   h2,  -l1,  0],
                        [0,   h3,   l2,  0],
                        [0,   h4,   l3,  0],
                        [0,  -h5,    0,  np.pi/2],
                        [0,    0,    0,  np.pi/2],
                        [0,  h67,    0,  0]])
    