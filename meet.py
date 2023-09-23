import pyautogui
import time

meetingId=pyautogui.prompt(text="Enter Your Meeting ID",title="Meeting Id",default="")
time.sleep(1)
pyautogui.press('win', interval=0.5)
time.sleep(1)
pyautogui.write("Chrome")
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write(meetingId)
time.sleep(1)
pyautogui.press("Enter",interval=0.5)
time.sleep(5)
pyautogui.click(x=1359,y=586)
