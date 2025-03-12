import subprocess
import speech_recognition as sr

def run_python_file(filename):
    try:
        subprocess.run(["python3", filename])
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred:", e)

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None

def main():
    while True:
        command = recognize_speech()
        if command:
            if "open" in command:
                filename = input("object_detection1.py")
                run_python_file(filename)
            else:
                print("Command not recognized.")

if __name__ == "__main__":
    main()
