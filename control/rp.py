
from MyHand import MyGripper_H100
import time
if __name__=="__main__":
    print("port")
    print("Device says its ID is", hand.get_gripper_Id())

    hand=MyGripper_H100("/dev/ttyCH343USB0", 115200,id=14)
    print("Device says its ID is", hand.get_gripper_Id())
    print(hand.port)
    print(hand.ser)
    hand.set_gripper_pose(0,0)
    print("init")
    time.sleep(2)
    print("pose")
    hand.set_gripper_pose(1,5)
    time.sleep(5)
    hand.set_gripper_pose(2,5)
    time.sleep(5)
    hand.set_gripper_pose(3,5)
    time.sleep(5)
    hand.set_gripper_pose(4,15)
    time.sleep(5)
    hand.set_gripper_pose(0,0)
    time.sleep(2)