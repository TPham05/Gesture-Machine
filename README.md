# 🙌 Gesture Machine: Mediapipe + Voice-Controlled Python Assistant

Originally inspired by JARVIS from the Iron Man movies, this project has evolved into a powerful accessibility tool. Rather than being a general AI, Gesture Machine is designed to assist individuals who have difficulty typing—such as those with trigger finger or carpal tunnel syndrome—by interpreting predefined hand signs and voice commands to perform everyday computer tasks.

---

## 🧠 Features

- 🎯 **Special Command Recognition**  
  Detects specific hand gestures that trigger keyboard actions such as **Enter**, **Open Spotify**, and **Volume Up/Down**.

- 🧑‍💻 **User-Friendly Python Implementation**  
  Clean and readable code structure using standard Python libraries.

- 🧊 **Cooldown Mechanism**  
  Prevents accidental multiple key presses from repeated detection, ensuring smooth user experience.

- 📺 **Real-Time Visual Feedback**  
  Terminal-based debug output to track gesture recognition and system behavior.

- 🎙️ **Voice Recognition**  
  Supports voice-based **typing** and **clicking**, allowing hands-free interaction with the screen.

---

## 🛠️ Technologies & Tools

- **Python 3.x** – Main programming language.  
- **SpeechRecognition** – Captures and converts audio to actionable text commands.  
- **OpenCV** – Handles video capture, processing, and gesture detection.  
- **PyAutoGUI** – Simulates mouse clicks and keyboard presses for automation.  
- **Pytesseract (Tesseract OCR)** – Recognizes text on the screen for click-targeting based on spoken words.  
- **OS** – Used to launch desktop apps like Spotify.

---

## 🚀 Future Improvements

- 🔤 Expand the gesture vocabulary (e.g., full ASL alphabet or more commands).
- 🧩 Add custom hand signs for launching applications or macros.
- 🔊 Implement voice feedback or text-to-speech for improved accessibility.
- 📱 Optimize the system for mobile or low-power embedded devices (e.g., Raspberry Pi).

---

## 🎬 Demonstration

> A full video demo of Gesture Machine in action will be available soon!  
> 

---

---

## ✋ Gesture Control Reference

The following hand signs are recognized in real-time and mapped to specific system actions. This allows the user to control media playback, navigation, and volume without touching a keyboard or mouse.

---

### ✅ `ok`
- **Gesture**: Thumb and index finger touch to form an “O”; all other fingers extended.
- **Action**: Presses the `Enter` key.

---

### ⬆️ `scroll_up`
- **Gesture**: Index and middle fingers extended and close together, pointing upward; thumb not extended.
- **Action**: Scrolls the screen **upward**.

---

### ⬇️ `scroll_down`
- **Gesture**: Index and middle fingers extended and close together, pointing downward; thumb not extended.
- **Action**: Scrolls the screen **downward**.

---

### 🔊 `volume_up`
- **Gesture**: Index finger extended; all other fingers folded.
- **Action**: Increases the system volume.

---

### 🔉 `volume_down`
- **Gesture**: Index finger points downward; middle, ring, and pinky fingers extended.
- **Action**: Decreases the system volume.

---

### 🎵 `play_music`
- **Gesture**: “Rock on” sign – index and pinky fingers extended; middle and ring fingers folded.
- **Action**: Plays or resumes music in Spotify.

---

### ⏮️ `previous_song`
- **Gesture**: Index and middle fingers extended and spread apart; ring finger folded.
- **Action**: Skips to the **previous** track in Spotify.

---

### ⏭️ `next_song`
- **Gesture**: Index, middle, and ring fingers extended and spread apart.
- **Action**: Skips to the **next** track in Spotify.

---

### 🌐 `y_sign`
- **Gesture**: Thumb and pinky extended wide; all other fingers folded.
- **Action**: Launches the default browser (e.g., Chrome).

---

### 👈 `l_sign`
- **Gesture**: Index finger extended upward, thumb extended sideways (forming an “L” shape); other fingers folded.
- **Action**: Presses `Backspace`.

---

### 🫖 `tea`
- **Gesture**: Pinky extended; all other fingers folded (mimicking tea-drinking etiquette).
- **Action**: Opens Spotify.

---

