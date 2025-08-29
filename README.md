# QTE Macro for Huzz RNG | v2.0

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![GitHub License](https://img.shields.io/github/license/gangstayencoin/QTE_Macro)


A fast and accurate macro for automating the QTE (Quick Time Event) sequence in Huzz RNG. Uses multi-threaded screen capture and predictive clicking for high-speed precision.

---

## Features

- Real-time, multi-threaded screen capture for high responsiveness
- Predictive bar clicking with smoothed speed calculation
- Dynamic target width handling for shrinking/growing targets
- HSV color filtering and morphological cleaning to reduce false positives
- Live detection visualization (optional)
- Lightweight and efficient

---

## Installation

1. Ensure you have **Python 3.10+** installed.
2. Clone or download the repository:

```bash
git clone https://github.com/yourusername/QTE-Macro.git

cd QTE-Macro

pip install -r requirements.txt
```
 ## Dependencies include:

 - `pyautogui`
 - `opencv-python`
 - `numpy`
 - `mss`
 - `pygetwindow`

 ## Usage

 1. Naviagte to the quick time event.

 2. Go through all the necassary dialogue, once there press "Play Hard".

 3. Run the macro.
    ```bash
    python main.py
    ```

5. If everything is done correctly then it should start automating the QTE instantly.

## Configuration

- The screen capture region is set in main.py with `qte_region`. Adjust the coordinates if your resolution or UI layout differs.
- Adjust `bar_hsv_lower`, `bar_hsv_upper`, `target_hsv_lower`, and `target_hsv_upper` if game colors change.

## Notes

- The macro only handles the QTE itself; it does not automate any menu buttons like “Play Hard.” (yet)
- Multi-threaded capture ensures high frame rates for fast-moving bars.

## Changelog

**v2.0 (Current)**
- Switched to HSV color detection for better robustness
- Added morphological cleaning to reduce false positives
- Smoothed speed prediction with moving average over last 5 frames
- Dynamic target width handling
- Added safety checks for `predicted_x` to prevent crashes
- Improved Roblox window activation handling

**v1.0**
- Original RGB-based QTE automation
- Basic predictive clicking
- Single-threaded capture
- Worked best with consistent target size and moderate speed
