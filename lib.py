import win32gui

def handler(hwnd, param):
  print(win32gui.GetClassName(hwnd))

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
