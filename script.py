from pydualsense import *
import pyautogui
import os

dualsense = pydualsense()
dualsense.init()

# mouse nav with gyro but only when L1 is pressed
def gyro_handler(pitch, yaw, roll):
    if dualsense.state.L1:
        pyautogui.move(pitch / 100 * -1, roll / 100, duration=0.0001)
    
dualsense.gyro_changed += gyro_handler

while not dualsense.state.ps:
    # motor rumbling by triggers
    # dualsense.setRightMotor(dualsense.state.R2)
    # dualsense.setLeftMotor(dualsense.state.L2)
    
    # wow pretty led lights by triggers
    # dualsense.light.setColorI(dualsense.state.R2, 0, dualsense.state.L2)
    
    # pc turnoff button lol (triangle)
    # if dualsense.state.triangle:
        # os.system('shutdown /s /t 1')
        
    # left mouse button (l2)
    if dualsense.state.L2:
        pyautogui.click()
    
    
dualsense.close()