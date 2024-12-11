# voice-to-text
# Speech-to-Text Application
This project demonstrates the conversion of speech to text using the SpeechRecognition library in Python. It supports both audio file transcription and real-time speech recognition from a microphone.

# Features
Converts speech from an audio file to text.
Recognizes and transcribes speech in real-time from microphone input.
Handles common errors gracefully, such as file not found, unrecognizable speech, or request issues.

# Dependencies
Make sure the following library is installed:
SpeechRecognition

# Usage
Run the Script
Execute the script:
python script_name.py

# Choose an Option

Option 1: Convert speech from a recorded audio file.
Provide the path to the audio file when prompted (e.g., audio.wav).
Option 2: Convert speech directly from the microphone.
Speak into the microphone when prompted.

# Code Explanation
1. Speech-to-Text from File
The speech_to_text_from_file function:

Reads an audio file.
Transcribes the audio to text using Google Speech Recognition.
Handles errors like file not found or unrecognizable audio.
2. Speech-to-Text from Microphone
The speech_to_text_from_mic function:

Captures live speech through the microphone.
Adjusts for ambient noise and transcribes the speech to text.
Handles microphone-specific errors like timeouts or unrecognizable input.
3. User Interaction
The script offers an intuitive menu to choose between file-based or microphone-based transcription.

# Error Handling
FileNotFoundError: Handles missing or incorrect file paths.
UnknownValueError: Handles cases where speech recognition can't understand the audio.
RequestError: Manages issues with Google Speech Recognition API requests.
WaitTimeoutError: Handles microphone listening timeouts.

