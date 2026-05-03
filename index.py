import speech_recognition as sr
import pyttsx3
import subprocess
import webbrowser
import os
import urllib.parse
import re
import time

os.environ["PATH"] += os.pathsep + "/opt/homebrew/bin"

# ---------------- SPEECH ENGINE (FIXED FOR MAC) ----------------
engine = pyttsx3.init("nsss")   # 🔥 IMPORTANT FIX
engine.setProperty('rate', 175)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print("Assistant:", text)
    try:
        engine.stop()
        time.sleep(0.1)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Speech Error:", e)

# ---------------- LISTEN ----------------
def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        engine.stop()

        r.adjust_for_ambient_noise(source, duration=0.8)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=6)
            command = r.recognize_google(audio)
            print("🧑 You:", command)
            return command.lower()
        except:
            return ""

# ---------------- AI ----------------
def ask_ai(prompt):
    process = subprocess.Popen(
        ["ollama", "run", "llama3"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    output, _ = process.communicate(input=prompt)
    return output.strip()

# ---------------- SHOPPING ----------------
def smart_shop_search(command, platform):
    text = command.lower()

    remove_words = [
        "search", "find", "buy", "get", "show", "me",
        "on", "in", "from", platform
    ]

    query = text
    for w in remove_words:
        query = query.replace(w, "")

    query = re.sub(r"\s+", " ", query).strip()

    if not query:
        return False

    query = urllib.parse.quote(query)

    urls = {
        "amazon": "https://www.amazon.in/s?k=",
        "flipkart": "https://www.flipkart.com/search?q=",
        "meesho": "https://www.meesho.com/search?q=",
        "myntra": "https://www.myntra.com/search?q="
    }

    webbrowser.open(urls[platform] + query)
    speak(f"Searching {query} on {platform}")
    return True

# ---------------- GPS ----------------
def jarvis_gps(command):
    text = command.lower()

    if not any(k in text for k in ["navigate", "route", "go to", "map", "direction"]):
        return False

    remove_words = ["open","maps","navigate","go","to","route","reach","find","travel","direction"]
    destination = text

    for w in remove_words:
        destination = destination.replace(w, "")

    destination = destination.strip()

    if not destination:
        webbrowser.open("https://maps.google.com")
        speak("Opening Google Maps")
        return True

    encoded = urllib.parse.quote(destination)

    webbrowser.open(f"https://www.google.com/maps/dir/?api=1&destination={encoded}")
    speak(f"Navigating to {destination}")
    return True

# ---------------- MAIN LOOP ----------------
while True:

    command = listen()
    if not command:
        continue

    # EXIT
    if command in ["stop", "exit", "quit", "bye"]:
        speak("Goodbye!")
        break

    # THANK YOU
    if "thank you" in command:
        speak("You're welcome")
        continue

    # ---------------- GOOGLE SEARCH ----------------
    if "search" in command and "youtube" not in command:
        q = command.replace("search", "").strip()
        speak(f"Searching {q}")
        webbrowser.open(f"https://google.com/search?q={q}")
        continue

    # ---------------- YOUTUBE ----------------
    if "youtube" in command:
        q = command.replace("youtube", "").replace("search", "").strip()

        if q:
            speak(f"Searching {q} on YouTube")
            webbrowser.open(f"https://youtube.com/results?search_query={q}")
        else:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")
        continue

    # ---------------- SHOPPING ----------------
    if "amazon" in command:
        if smart_shop_search(command, "amazon"):
            continue
        webbrowser.open("https://amazon.in")
        speak("Opening Amazon")
        continue

    if "flipkart" in command:
        if smart_shop_search(command, "flipkart"):
            continue
        webbrowser.open("https://flipkart.com")
        speak("Opening Flipkart")
        continue

    if "meesho" in command:
        if smart_shop_search(command, "meesho"):
            continue
        webbrowser.open("https://meesho.com")
        speak("Opening Meesho")
        continue

    if "myntra" in command:
        if smart_shop_search(command, "myntra"):
            continue
        webbrowser.open("https://myntra.com")
        speak("Opening Myntra")
        continue

    # ---------------- NETFLIX ----------------
    if "netflix" in command:
        q = command.replace("netflix", "").strip()

        if q:
            speak(f"Searching {q} on Netflix")
            webbrowser.open(f"https://www.netflix.com/search?q={q}")
        else:
            speak("Opening Netflix")
            webbrowser.open("https://netflix.com")
        continue

    # ---------------- PRIME VIDEO ----------------
    if "prime" in command:
        q = command.replace("prime", "").strip()

        if q:
            speak(f"Searching {q} on Prime Video")
            webbrowser.open(f"https://www.primevideo.com/search?phrase={q}")
        else:
            speak("Opening Prime Video")
            webbrowser.open("https://primevideo.com")
        continue

    # ---------------- HOTSTAR ----------------
    if "hotstar" in command or "disney" in command:
        q = command.replace("hotstar", "").replace("disney", "").strip()

        if q:
            speak(f"Searching {q} on Hotstar")
            webbrowser.open(f"https://www.hotstar.com/in/search?q={q}")
        else:
            speak("Opening Hotstar")
            webbrowser.open("https://hotstar.com")
        continue

    # ---------------- SPOTIFY ----------------
    if "spotify" in command:
        q = command.replace("play", "").replace("spotify", "").strip()

        if q:
            speak(f"Playing {q} on Spotify")
            webbrowser.open(f"https://open.spotify.com/search/{q}")
        else:
            speak("Opening Spotify")
            webbrowser.open("https://open.spotify.com")
        continue

    # ---------------- GPS ----------------
    if jarvis_gps(command):
        continue

    # ---------------- AI FALLBACK ----------------
    reply = ask_ai(command)
    speak(reply)