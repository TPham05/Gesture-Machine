import pytesseract
import pyautogui
import cv2
import numpy as np
import speech_recognition as sr
from PIL import ImageGrab

 # Upscaling the image to improve the OCR accuracy
def upscale_image(image, scale=2):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)

def find_and_move_to_word(target_word):
    # Take screenshot
    screenshot = ImageGrab.grab()
    screenshot_np = np.array(screenshot)
    screenshot_rgb = screenshot_np  

    # Get actual screen size
    screen_width, screen_height = pyautogui.size()
    image_width, image_height = screenshot.size

    # Calculate scale factor
    scale_x = screen_width / image_width
    scale_y = screen_height / image_height

    # Upscale screenshot to improve OCR accuracy
    upscale_factor = 2
    screenshot_rgb_upscaled = upscale_image(screenshot_rgb, scale=upscale_factor)

    # Switch to Layout Mode 6
    custom_config = r'--psm 6'
    data = pytesseract.image_to_data(screenshot_rgb_upscaled, output_type=pytesseract.Output.DICT, config=custom_config)

    target_word = target_word.strip().capitalize()


    for i in range(len(data['text'])):
        word = data['text'][i].strip()
        if target_word in word:
            # Original coordinates in upscaled image → convert to original image size
            x_raw = data['left'][i] + data['width'][i] // 2
            y_raw = data['top'][i] + data['height'][i] // 2
            x = int((x_raw / upscale_factor) * scale_x)
            y = int((y_raw / upscale_factor) * scale_y)

            print(f"Found '{word}' at ({x}, {y})")

            pyautogui.moveTo(x, y, duration=0.3)
            pyautogui.click()
            return True

    print(f" Word '{target_word}' not found.")
    return False

def voice_typing_loop():
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=1)  # Set the mic index, ensuring it is the correct microphone

    print("Voice command mode")

    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=5) # Listens to audio for 5 seconds
                text = recognizer.recognize_google(audio).lower()
                print(f"Heard: {text}") # Debugging text

                if text.startswith("click "): # If starts with click, then the program will click the button
                    keyword = text.replace("click ", "").strip()
                    found = find_and_move_to_word(keyword)
                    if not found:
                        print(f"Couldn't find the word '{keyword}' on screen.")
                elif text.startswith("please type "): # If start with please type, the program will change audio to text
                    to_type = text.replace("please type ", "").strip()
                    pyautogui.write(to_type + " ")
                else:
                    print("Command ignored: not a recognized action.")

            except sr.UnknownValueError:
                print("Couldn’t understand you.")
            except sr.RequestError as e:
                print(f"API error: {e}")
            except sr.WaitTimeoutError:
                continue

