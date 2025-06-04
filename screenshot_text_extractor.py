import tkinter as tk
from tkinter import Canvas
from PIL import ImageGrab
import pytesseract
import keyboard
import datetime
import os
from playsound import playsound
import threading
import ctypes


try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  # Enables DPI awareness for accurate scaling
except:
    try:
        ctypes.windll.user32.SetProcessDPIAware()  # Fallback for older Windows versions
    except:
        pass


# Set Tesseract executable path if needed
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

OUTPUT_FOLDER = "extracted_text"
BEEP_SOUND = "beep.mp3"  # Place this file in the same directory

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)


def play_sound():
    try:
        threading.Thread(target=playsound, args=(BEEP_SOUND,), daemon=True).start()
    except Exception as e:
        print(f"[ERROR] Failed to play sound: {e}")


def select_region():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-alpha", 0.3)
    root.config(bg='black')
    root.title("Select Region")
    root.lift()
    root.attributes("-topmost", True)
    root.focus_force()

    canvas = Canvas(root, cursor="cross", bg="gray", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    coords = {}

    def on_mouse_down(event):
        coords['start_x'] = event.x
        coords['start_y'] = event.y
        coords['rect'] = canvas.create_rectangle(event.x, event.y, event.x, event.y, outline="red", width=2)

    def on_mouse_drag(event):
        canvas.coords(coords['rect'], coords['start_x'], coords['start_y'], event.x, event.y)

    def on_mouse_up(event):
        coords['end_x'] = event.x
        coords['end_y'] = event.y
        root.quit()

    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_drag)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)

    root.mainloop()
    root.destroy()

    if all(k in coords for k in ('start_x', 'start_y', 'end_x', 'end_y')):
        x1, y1 = min(coords['start_x'], coords['end_x']), min(coords['start_y'], coords['end_y'])
        x2, y2 = max(coords['start_x'], coords['end_x']), max(coords['start_y'], coords['end_y'])
        return (x1, y1, x2, y2)
    else:
        return None


def capture_and_extract_text():
    print("[INFO] Hotkey pressed! Select region...")
    region = select_region()

    if not region:
        print("[WARN] No region selected.")
        return

    screenshot = ImageGrab.grab(bbox=region)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    text_output = pytesseract.image_to_string(screenshot)

    if text_output.strip():
        output_file = os.path.join(OUTPUT_FOLDER, f"text_{timestamp}.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text_output)
        print(f"[INFO] Text extracted and saved to {output_file}")
    else:
        print("[INFO] No text found in the selected region.")

    play_sound()


def main():
    print("[INFO] Screenshot OCR Tool running...")
    print("Press Ctrl+Shift+S to select a region and capture text.")
    keyboard.add_hotkey('ctrl+shift+s', capture_and_extract_text)
    keyboard.wait()  # Keeps the program running


if __name__ == "__main__":
    main()
