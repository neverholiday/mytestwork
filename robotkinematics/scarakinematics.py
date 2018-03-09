import numpy as np
from robotconfiguration import RobotConfiguration

class SCARAKinematics(object):

    def __init__(self):
        
        self.robot = RobotConfiguration()

    def rot(self,theta,axis):
        if(axis == 'x'):
            row1 = np.array([1,0,0,0])
            row2 = np.array([0,np.cos(theta),-1*np.sin(theta),0])
            row3 = np.array([0,np.sin(theta),np.cos(theta),0])
            row4 = np.array([0,0,0,1])
            h_mat = np.vstack((row1,row2,row3,row4))
        elif(axis == 'y'):
            row1 = np.array([np.cos(theta),0,np.sin(theta),0])
            row2 = np.array([0,1,0,0])
            row3 = np.array([-1*np.sin(theta),0,np.cos(theta),0])
            row4 = np.array([0,0,0,1])
            h_mat = np.vstack((row1,row2,row3,row4))
        elif(axis == 'z'):
            row1 = np.array([np.cos(theta),-1*np.sin(theta),0,0])
            row2 = np.array([np.sin(theta),np.cos(theta),0,0])
            row3 = np.array([0,0,1,0])
            row4 = np.array([0,0,0,1])
            h_mat = np.vstack((row1,row2,row3,row4))

        return h_mat
    
    def trans(self,distance,axis):
        if(axis == 'x'):
            row1 = np.array([1,0,0,distance])
            row2 = np.array([0,1,0,0])
            row3 = np.array([0,0,1,0])
            row4 = np.array([0,0,0,1])
            h_mat = np.vstack((row1,row2,row3,row4))
        elif(axis == 'y'):
            row1 = np.array([1,0,0,0])
            row2 = np.array([0,1,0,distance])
            row3 = np.array([0,0,1,0])
            row4 = np.array([0,0,0,1])
            h_mat = np.vstack((row1,row2,row3,row4))
        elif(axis == 'z'):
            row1 = np.array([1,0,0,0])
            row2 = np.array([0,1,0,0])
            row3 = np.array([0,0,1,distance])
            row4 = np.array([0,0,0,1])
            h_mat = np.vstack((row1,row2,row3,row4))

        return h_mat

    def dh_trans(self,theta,d,a,alpha):
        rot_z = self.rot(theta,'z')
        trans_z = self.trans(d,'z')
        trans_x = self.trans(a,'x')
        rot_x = self.rot(alpha,'x')
        dh_mat = reduce(np.dot,[rot_z,trans_z,trans_x,rot_x]) 
        return dh_mat

    def orientationZYZ(self,angle):
        R1 = self.rot(angle[0],'z')
        R2 = self.rot(angle[1],'y')
        R3 = self.rot(angle[2],'z')
        rot_mat = reduce(np.dot,[R1,R2,R3])
        return rot_mat
    
    def orientationRPY(self,angle):
        R1 = self.rot(angle[0],'x')
        R2 = self.rot(angle[1],'y')
        R3 = self.rot(angle[2],'z')
        rot_mat = reduce(np.dot,[R3,R2,R1])
        return rot_mat

    def forwardKinematics(self,q):
        n = self.robot.dh_table.shape[0]

        # Add q depend on type of joint
        for i in range(n):
            if(self.robot.type_of_joint[i] == 0):
                self.robot.dh_table[i,1] = self.robot.dh_table[i,1] + q[i]
            elif(self.robot.type_of_joint[i] == 1):
                self.robot.dh_table[i,0] = self.robot.dh_table[i,0] + q[i]
        
        # Find forwardkinematics equation
        for i in range(n):
            A_n = self.dh_trans(self.robot.dh_table[i,0],self.robot.dh_table[i,1],self.robot.dh_table[i,2],self.robot.dh_table[i,3])
            if(i == 0):
                H = A_n
            else:
                temp_H = A_n
                H = np.dstack((H,temp_H))
        
        H_e = H[:,:,n-1]
        R_e = H_e[0:2,0:2]
        p_e = H_e[0:2,2]
        
        return (H,H_e,R_e,p_e)

    def inverseKinematicsCalculate(self,position,orientation,type_of_orientation):
        if(type_of_orientation == "rpy"):
            R_e = self.orientationRPY(orientation)
        elif(type_of_orientation == "zyz"):
            R_e = self.orientationZYZ(orientation)

        # End-effector to wrist
        pos_wrist = (position - reduce(np.dot,[R_e,np.array([[0],[0],[1]])])) + np.array([[0],[0],[3]])

        q2 = pos_wrist[2] - self.robot.h1 - self.robot.h2

        c3 = (pos_wrist[0]**2 + pos_wrist[1]**2 - self.robot.l1**2 - self.robot.l2**2)/(2*self.robot.l1*self.robot.l2)
        s3_positive = np.sqrt(1-(c3**2))
        s3_negative = -np.sqrt(1-(c3**2))

        q3_A = np.arctan2(s3_positive,c3)
        q3_B = np.arctan2(s3_negative,c3)

        s1_positive = (-self.robot.l2 * s3_positive)*pos_wrist[0] + (self.robot.l1 + self.robot.l2*c3)*pos_wrist[1]
        s1_negative = (-self.robot.l2 * s3_negative)*pos_wrist[0] + (self.robot.l1 + self.robot.l2*c3)*pos_wrist[1]

        c1_positive = (self.robot.l1+(self.robot.l2*c3))*pos_wrist[0] + (self.robot.l2*s3_positive)*pos_wrist[1]
        c1_negative = (self.robot.l1+(self.robot.l2*c3))*pos_wrist[0] + (self.robot.l2*s3_negative)*pos_wrist[1]
        
        q1_A = np.arctan2(s1_positive,c1_negative)
        q1_B = np.arctan2(s1_negative,c1_negative)

        q_wrist_pos_A = np.array([0,q1_A,q2,q3_A,0,0,0])
        q_wrist_pos_B = np.array([0,q1_B,q2,q3_B,0,0,0])
        
        H_A = self.forwardKinematics(q_wrist_pos_A)
        H_B = self.forwardKinematics(q_wrist_pos_B)

        R_04_A = H_A[0:2,0:2,3]
        R_04_B = H_B[0:2,0:2,3]

        R_47_A = reduce(np.dot, [np.transpose(R_04_A),R_e])
        R_47_B = reduce(np.dot, [np.transpose(R_04_B),R_e])

        # A ---------------------------------
        r23_A = R_47_A[1,2]
        r13_A = R_47_A[0,2)
        r31_A = R_47_A(2,0)
        r32_A = R_47_A[2,1]
        r33_A = R_47_A[2,2]

        sq_Aa = np.sqrt(r31_A**2 + r32_A**2)
        sq_Ab = -np.sqrt(r31_A**2 + r32_A**2)

        q4_Aa = np.arctan2(r23_A/sq_Aa,r13_A/sq_Aa)
        q4_Ab = np.arctan2(r23_A/sq_Ab,r13_A/sq_Ab)
        q5_Aa = np.arctan2(sq_Aa,-r33_A)
        q5_Ab = np.arctan2(sq_Ab,-r33_A)
        q6_Aa = np.arctan2(-r32_A/sq_Aa,r31_A/sq_Aa)
        q6_Ab = np.arctan2(-r32_A/sq_Ab,r31_A/sq_Ab)

        # B ------------------------------
        r23_B = R_47_A[1,2]
        r13_B = R_47_A[0,2)
        r31_B = R_47_A(2,0)
        r32_B = R_47_A[2,1]
        r33_B = R_47_A[2,2]

        sq_Ba = np.sqrt(r31_B**2 + r32_B**2);  % plus
        sq_Bb = -np.sqrt(r31_B**2 + r32_B**2); % minus

        q4_Ba = np.arctan2(r23_B/sq_Ba,r13_B/sq_Ba);
        q4_Bb = np.arctan2(r23_B/sq_Bb,r13_B/sq_Bb);
        q5_Ba = np.arctan2(sq_Ba,-r33_B);
        q5_Bb = np.arctan2(sq_Bb,-r33_B);
        q6_Ba = np.arctan2(-r32_B/sq_Ba,r31_B/sq_Ba);
        q6_Bb = np.arctan2(-r32_B/sq_Bb,r31_B/sq_Bb);

        # Result of 4 Configuration
        q_1 = np.array([0 q1_A,q2,q3_A,q4_Aa,q5_Aa,q6_Aa])
        q_2 = np.array([0,q1_A,q2,q3_A,q4_Ab,q5_Ab,q6_Ab])

        q_3 = np.array([0,q1_B,q2,q3_B,q4_Ba,q5_Ba,q6_Ba])
        q_4 = np.array([0,q1_B,q2,q3_B,q4_Bb,q5_Bb,q6_Bb])
        return (q_1,q_2,q_3,q_4)
# def main():

    

#     fk = forwardKinematics()
#     d = fk.dh_trans(np.pi/2,2,2,np.pi/2)
#     print np.floor(d)

# if __name__ == '__main__':
#     main()
    