# 🖼️ Screenshot OCR Tool with OpenCV & Tesseract

This is a Python-based desktop tool that lets you **quickly capture a portion of your screen using a hotkey** (`Ctrl + Shift + S`), extract **text from the selected region** using **Tesseract OCR**, and **save it to a `.txt` file** automatically. A beep sound confirms the operation.

## 🔍 Features

- Instant screen region selection via hotkey (no need to open any window manually)
- Optical Character Recognition (OCR) using **Tesseract**
- Optional image preprocessing using **OpenCV** for better OCR accuracy
- Automatic timestamped text file creation
- Visual rectangle for region selection
- Custom notification sound support

## 🧪 Technologies Used

- **Python 3.12**
- **Tkinter** – for GUI and region selection overlay
- **Pillow (PIL)** – for capturing screen regions
- **Tesseract OCR** – to recognize and extract text from images
- **OpenCV** – (optional) to preprocess screenshots before OCR
- **Keyboard** – to bind the global hotkey
- **Playsound** – to play a sound once the capture is complete

## 🛠️ How It Works

1. Run the script or executable.
2. Press `Ctrl + Shift + S` from anywhere.
3. Select a region on the screen.
4. The tool captures the image, optionally preprocesses it using OpenCV, and passes it to Tesseract.
5. Extracted text is saved into a `.txt` file inside the `extracted_text` folder with a timestamped name.
6. A beep sound is played to indicate completion.

## 📂 Folder Structure

