import os
import pyautogui

spotify_opened = False

def open_spotify():
    global spotify_opened
    if spotify_opened:
        return
    print("Opening Spotify...")

    try:
        spotify_path = r"C:\Users\Tommy\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Spotify.lnk"
        spotify_path = os.path.expandvars(spotify_path)
        if os.path.exists(spotify_path):
            os.startfile(spotify_path)
            spotify_opened = True
        else:
            print("Spotify executable not found. Please check the path.")
    except Exception as e:
        print("Error opening Spotify:", e)

def play_previous_song():
    print("Playing previous song")
    pyautogui.press('prevtrack')

def play_next_song():
    print("Playing next song")
    pyautogui.press('nexttrack')

def play_current_song():
    print("Playing song")
    pyautogui.press('playpause')