import speech_recognition as sr

def live_transcription():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    print("Customer Support Transcription System")
    print("Say something... (Press Ctrl+C to stop)\n")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5)
                print("Transcribing...")
                text = recognizer.recognize_google(audio)
                print("Customer Said:", text)
                print("-" * 40)
            except sr.WaitTimeoutError:
                print("Timeout, no speech detected.")
            except sr.UnknownValueError:
                print("Sorry, could not understand.")
            except sr.RequestError as e:
                print(f"Could not request results: {e}")
            except KeyboardInterrupt:
                print("\nSession ended.")
                break

if __name__ == "__main__":
    live_transcription()
