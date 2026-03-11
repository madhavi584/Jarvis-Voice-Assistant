import tkinter as tk
import pyttsx3
import datetime
import webbrowser
import wikipedia

# Text to Speech Engine
engine = pyttsx3.init()

def speak(text):
    output_box.insert(tk.END, "Jarvis: " + text + "\n")
    engine.say(text)
    engine.runAndWait()

# Greeting
def greet():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning Madhavi")
    elif hour < 18:
        speak("Good Afternoon Madhavi")
    else:
        speak("Good Evening Madhavi")

    speak("I am Jarvis. How can I help you?")

# Command processing
def process_command():
    query = entry_box.get().lower()
    output_box.insert(tk.END, "You: " + query + "\n")

    if "hello" in query:
        speak("Hello Madhavi")

    elif "time" in query:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("The time is " + time)

    elif "date" in query:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)

    elif "open youtube" in query:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open google" in query:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "search" in query:
        search = query.replace("search", "")
        webbrowser.open("https://www.google.com/search?q=" + search)
        speak("Here are the search results")

    elif "wikipedia" in query:
        topic = query.replace("wikipedia", "")
        result = wikipedia.summary(topic, sentences=2)
        speak(result)

    elif "exit" in query:
        speak("Goodbye Madhavi")
        root.quit()

    else:
        speak("Sorry I did not understand")

    entry_box.delete(0, tk.END)

# GUI Window
root = tk.Tk()
root.title("Jarvis AI Assistant")
root.geometry("500x500")
root.configure(bg="black")

title = tk.Label(root, text="JARVIS AI ASSISTANT", font=("Arial", 18, "bold"), fg="cyan", bg="black")
title.pack(pady=10)

output_box = tk.Text(root, height=20, width=55)
output_box.pack()

entry_box = tk.Entry(root, width=40)
entry_box.pack(pady=10)

button = tk.Button(root, text="Send Command", command=process_command)
button.pack()

# Start greeting
greet()

root.mainloop()