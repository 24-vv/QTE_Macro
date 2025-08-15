import pyautogui
import threading
import time

class Clicker:
    def __init__(self):
        self.last_click_time = 0
        self.lock = threading.Lock()

    def safe_click(self, x, y):
        with self.lock:
            if time.time() - self.last_click_time > 0.003:
                pyautogui.click(x, y)
                self.last_click_time = time.time()
