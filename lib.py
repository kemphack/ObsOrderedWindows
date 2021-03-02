import win32gui

def windows_ordered():
  
  ordered = dict()
  z = 0
  def handler(hwnd, param):
    nonlocal z
    PyCWnd = win32gui.GetForegroundWindow()
    ordered.setdefault(hwnd, z)
    z = z + 1
  win32gui.EnumWindows(handler, None)

  return ordered
