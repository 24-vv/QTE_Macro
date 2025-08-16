import time
import cv2
import pygetwindow as gw
from core.capture import Capture
from core.detection import Detection
from core.clicker import Clicker

roblox_windows = [w for w in gw.getWindowsWithTitle("Roblox") if w.visible]
if not roblox_windows:
    exit("Roblox window not found.")
roblox_window = roblox_windows[0]

try:
    if roblox_window.isMinimized:
        roblox_window.restore()
    time.sleep(0.5)
    roblox_window.activate()
    time.sleep(0.5)
except:
    print("Could not focus Roblox window. Make sure it is visible.")

qte_region = {"top": 724, "left": 505, "width": 842, "height": 50}

bar_hsv_lower = [0, 0, 200]
bar_hsv_upper = [180, 30, 255]
target_hsv_lower = [50, 100, 50]
target_hsv_upper = [90, 255, 255]

capture = Capture(qte_region)
detection = Detection(bar_hsv_lower, bar_hsv_upper, target_hsv_lower, target_hsv_upper)
clicker = Clicker()

while True:
    frame = capture.get_frame()
    if frame is None:
        continue

    bar_info, target_info = detection.process_frame(frame)

    if bar_info and target_info:
        predicted_x = detection.predict_bar_position()
        if predicted_x is not None:
            bx, by, bw, bh, _, _ = bar_info
            tx, ty, tw, th, tcx, tcy = target_info

            if (predicted_x + bw > tx) and (predicted_x < tx + tw) and (by + bh > ty) and (by < ty + th):
                clicker.safe_click(qte_region["left"] + tcx, qte_region["top"] + tcy)

    cv2.imshow("Live Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
