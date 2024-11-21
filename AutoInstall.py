import pyautogui as auto
import time

auto.PAUSE = 1

auto.press("win")
auto.write("Chrome", interval=0.15)
auto.press("enter")
auto.write("vscode", interval=0.15)
auto.press("enter")
auto.click(x=366, y=304, duration=0.25)
auto.click(x=790, y=459, duration=0.25)

auto.hotkey("ctrl", "n")

auto.write("Python download", interval=0.15)
auto.press("enter")
auto.click(x=366, y=304, duration=0.25)
auto.click(x=534, y=395, duration=0.25)

auto.hotkey("win", "e")
auto.click(x=562, y=194, duration=0.25)

auto.alert('Instalação do VScode e Python realizada! ')


