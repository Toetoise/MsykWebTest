import win32gui
import win32con
import pywintypes


class Upload:
    def __init__(self, driver):
        self.driver = driver

    def upload_file(self, filePath):
        dialog = win32gui.FindWindow("#32770", "打开")
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        combox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
        edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
        button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&O)")
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)