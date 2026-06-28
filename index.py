import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import random

# -----------------------------
# Text to Speech
# -----------------------------

engine = pyttsx3.init()
engine.setProperty("rate", 170)


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# -----------------------------
# Greeting Function
# -----------------------------

def wish_me():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good Morning Naveen!")

    elif 12 <= hour < 18:
        speak("Good Afternoon Naveen!")

    else:
        speak("Good Evening Naveen!")

    speak("How may I help you?")


# -----------------------------
# speech Recognition
# -----------------------------

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.pause_threshold = 1

        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-IN")
        print(f"You Said: {query}")

        return query.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
        return ""

    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

    except Exception as e:
        print(e)
        return ""


# -----------------------------
# Main Program
# -----------------------------

def main():

    wish_me()

    while True:

        query = take_command()

        if query == "":
            continue

        # Wikipedia
        if "wikipedia" in query:

            speak("Searching Wikipedia")

            query = query.replace("wikipedia", "").strip()

            try:
                result = wikipedia.summary(query, sentences=2)

                print(result)
                speak(result)

            except Exception:
                speak("Sorry, I couldn't find anything.")

        # YouTube
        elif "youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        # Facebook
        elif "facebook" in query:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")

        # Stack Overflow
        elif "stack overflow" in query:
            speak("Opening Stack Overflow")
            webbrowser.open("https://stackoverflow.com")

        # Google Search
        elif "google" in query:

            search = query.replace("google", "")
            search = search.replace("search", "").strip()

            speak(f"Searching Google for {search}")

            webbrowser.open(
                f"https://www.google.com/search?q={search}"
            )

        # Play Music
        elif "music" in query or "song" in query:

            music_dir = r"D:\OldSongs"

            if os.path.exists(music_dir):

                songs = os.listdir(music_dir)

                if songs:
                    song = random.choice(songs)
                    os.startfile(os.path.join(music_dir, song))

                else:
                    speak("No songs found.")

            else:
                speak("Music folder not found.")

        # Tell Time
        elif "time" in query:

            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        # Exit
        elif "sleep" in query or "so jao" in query or "exit" in query:

            speak("Thank you Boss. Goodbye!")
            break

        # Unknown Command
        else:
            speak("Sorry Boss, I don't know how to do that yet.")


if __name__ == "__main__":
    main()