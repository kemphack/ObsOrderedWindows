import win32gui
import re

def handler(hwnd, param):
  print(win32gui.GetWindowText(hwnd))

def iterate_windows():
  PyCWnd = win32gui.GetForegroundWindow()
  win32gui.EnumWindows(handler, None)

  h = PyCWnd
  z = 0
  while h != 0:
    #next window
    GW_HWNDPREV = 3
    h = win32gui.GetWindow(h, GW_HWNDPREV)
    print(win32gui.GetWindowText(h))
    print(h)
    z = z + 1

def decode_string(str):
  def replace_with_symbol(matched):
    print(matched.group(1))
    return chr(int(matched.group(1), 16))
  return re.sub(r"#([\dABCDEF]{2})", replace_with_symbol, str)
