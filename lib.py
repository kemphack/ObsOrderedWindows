import win32gui
import re



def windows_ordered():
  
  # h = PyCWnd
  ordered = dict()
  z = 0
  def handler(hwnd, param):
    nonlocal z
    PyCWnd = win32gui.GetForegroundWindow()
    ordered.setdefault(hwnd, z)
    z = z + 1
  win32gui.EnumWindows(handler, None)

  
  # while h != 0:
  #   #next window
  #   GW_HWNDPREV = 3
  #   h = win32gui.GetWindow(h, GW_HWNDPREV)
  #   #print(h)
  #   ordered.setdefault(h, z)
  #   z = z + 1
  return ordered

def decode_string(str):
  def replace_with_symbol(matched):
    print(matched.group(1))
    return chr(int(matched.group(1), 16))
  return re.sub(r"#([\dABCDEF]{2})", replace_with_symbol, str)

# def get_number()