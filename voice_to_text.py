import speech_recognition as sr

def speech_to_text_from_file(file_path):
    """Convert speech to text from a recorded audio file."""
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            print("Processing audio file...")
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            print("Transcription from file:", text)
    except FileNotFoundError:
        print("Error: The specified file was not found. Please check the file path.")
    except sr.UnknownValueError:
        print("Error: Speech recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Error: Could not request results from Google Speech Recognition; {e}")
    except Exception as e:
        print("Error processing audio file:", e)

def speech_to_text_from_mic():
    """Convert speech to text from microphone input."""
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Please speak into the microphone...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            audio_data = recognizer.listen(source, timeout=10)
            print("Processing your speech...")
            text = recognizer.recognize_google(audio_data)
            print("Transcription from microphone:", text)
    except sr.UnknownValueError:
        print("Error: Speech recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Error: Could not request results from Google Speech Recognition; {e}")
    except sr.WaitTimeoutError:
        print("Error: Listening timed out while waiting for speech.")
    except Exception as e:
        print("Error processing microphone input:", e)

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Convert speech from a recorded audio file.")
    print("2. Convert speech directly from the microphone.")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    if choice == "1":
        file_path = input("Enter the path to the audio file (e.g., 'audio.wav'): ").strip()
        speech_to_text_from_file(file_path)
    elif choice == "2":
        print("Ensure your microphone is set up and working correctly.")
        speech_to_text_from_mic()
    else:
        print("Invalid choice. Please select 1 or 2.")
