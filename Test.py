import pyautogui
import GetWindow, Back
import time
x,y,center = GetWindow.window_found()
print("test+++++++")
print("窗口坐标 X：" + str(x) + "，Y：" + str(y))
# find location
pyautogui.moveTo(x + 100, y + 600)
time.sleep(2)
pyautogui.moveTo(x + 400, y + 700)
time.sleep(2)
# click
pyautogui.moveTo(x + 350, y + 650)
time.sleep(2)

print(Back.img_research(x,y))