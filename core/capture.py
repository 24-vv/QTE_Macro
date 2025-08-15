import mss
import numpy as np
import cv2
import threading

class Capture:
    def __init__(self, region):
        self.region = region
        self.latest_frame = None
        self.frame_lock = threading.Lock()
        self.thread = threading.Thread(target=self._capture_loop, daemon=True)
        self.thread.start()

    def _capture_loop(self):
        sct_thread = mss.mss()
        while True:
            img = np.array(sct_thread.grab(self.region))
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            with self.frame_lock:
                self.latest_frame = frame

    def get_frame(self):
        with self.frame_lock:
            return self.latest_frame.copy() if self.latest_frame is not None else None
