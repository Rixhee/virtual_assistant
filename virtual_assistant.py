import pyttsx3
import datetime 
import speech_recognition as sr
import random
import wikipedia
import os
import keyboard
import webbrowser
import time

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[14].id)
engine.setProperty('rate', 170)
pyttsx3.voice.Voice(id, name= "Jarvis", gender="male", age=25)

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

greet_lst = ["hello", "hey", "hi", "hi there", "hey there", "hey man", "hey buddy", "howdy"]
greet_lst_two = ["how are you", "how are things going", "how's it going", "what's going on", "how have you been", "what's up", "what's new", "what's shaking"]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 4 <= hour < 12:
        speak("Good morning sir")
    
    elif 12 <= hour < 18:
        speak("Good afternoon sir")
    
    elif 18 <= hour or hour < 4:
        speak("Good evening sir ")
        
    speak("How may i help you")

def takeCommand():
    
    r = sr.Recognizer() 
    
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)

        if keyboard.is_pressed('Esc'):
            response = Goodbye()
            quit()
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language= "en")
            print(f"You said: {query}\n ")
        
        except Exception as e:
            print(e)
            return 'None'

    return query

def wikipedia_search(query):
    
    lst = ["what is the meaning of ", "what is ", "who is ", "meaning of "]
    
    for i in lst:
        if i in query:
            query = query.replace(i, "")
            print(query)
            
            return wikipedia.summary(query, sentences=2)

def getDate():
    
    now = datetime.datetime.now()
    date = now.strftime("%B %d %Y")
    
    return str(date)

def getTime():
    
    now = datetime.datetime.now()
    time = str(now.strftime("%H %M"))
    
    if int(time[:2]) == 00:
        time = "12" + time[2:] + "am"
    elif int(time[:2]) < 12:
        time = time + "am"
    elif int(time[:2]) == 12:
        time = time + "pm"
    elif int(time[:2]) > 12:
        time = str(int(time[:2]) % 12) + str(time[2:]) + "pm"
    
    return  "It is " + time

def open_in_web():
    lst = query.split()
    lst = lst[lst.index("open") + 1:-2]
    text = "".join(lst)
    webbrowser.get(chrome_path).open(f"https://www.{text}.com")
    return " Opening " + text

def search_on_google():
    lst = query.split()
    query_lst = lst[lst.index("search") + 1:-2]
    string = " ".join(query_lst)
    webbrowser.get(chrome_path).open("https://www.google.com/search?q=" + string)
    return f"Searching {string} on google"

def hey_reply():
    string = greet_lst[random.randrange(0, len(greet_lst))] + ". " + greet_lst_two[random.randrange(0, len(greet_lst_two))]
    return string

def how_are_you_reply():
    lst = ["i am doing fine. ", "everyone is good. ", "things are going great. ", "everything is awesome. ", "things are okay. ", "i am fine. ", "not bad. ", "good. thanks. "]
    lst_two = ["And you?", "How are you?", "How about yourself?"]
    return lst[random.randrange(0, len(lst))] + lst_two[random.randrange(0, len(lst_two))]

def youtube_search():
    word_lst = ["open", "play", "search"]
    wrd = ""
    lst = query.split()
    for word in word_lst:
        if word in query:
            query_lst = lst[lst.index(word) + 1:-2]
            wrd += word
            break
    string = " ".join(query_lst)
    webbrowser.get(chrome_path).open("https://www.youtube.com/results?search_query=" + string)
    return f"{word}ing {string} on youtube" 

def wishGoodnight():
    lst = ["sweet dreams sir", "sleep well sir", "good night sir", "see you tomorrow sir"]
    return lst[random.randrange(0, len(lst))]    

def Goodbye():
    lst = ["see you later", "take care", "have a good one", "see ya", "catch you later", "great to see you sir", "ciao", "cheerio", "goodbye sir"]
    return lst[random.randrange(0, len(lst))]

if __name__ == "__main__":
    
    wishMe()
    
    while True:
        
        query = takeCommand().lower()
        response = ""
        
        if query == "":
            speak("Could you please repeat that")
            continue

        if ("search" in query or "open" in query or "play" in query or "find" in query) and ("on youtube" in query or "in youtube" in query  or "at youtube" in query):
            response += youtube_search()
            speak(response)
            continue
        
        if ("search" in query or "find" in query) and ("on google" in query or "in google" in query):
            response += search_on_google()
            speak(response)
            continue

        if "search" in query or "find" in query:
            lst = query.split()
            query_lst = lst[lst.index("search") + 1:]
            string = " ".join(query_lst)
            webbrowser.get(chrome_path).open("https://www.google.com/search?q=" + string)
            speak(f"Searching {string} on google")

        if ("hello " in query or "hi " in query or "hey " in query) and ("how are you" in query or "what's up" in query):
            response += how_are_you_reply()

        else:
            for a in greet_lst_two:
                if a in query:
                    response += how_are_you_reply()
        
            for i in greet_lst:
                if i in query:
                    response += hey_reply()

        if "date" in query:
            get_date = getDate()
            response = response + " Today is " + get_date
            if "who is " in query or "meaning of " in query:
                response += ". and According to wikipedia " + wikipedia_search(query)
        
        elif "the time" in query:
            response += getTime()
        
        elif "what is " in query or "who is " in query or "meaning of " in query or "what is the meaning of " in query:
            response += " According to wikipedia " + wikipedia_search(query)
        
        if "thank you" in query:
            response = "My pleasure sir"
            speak(response)
            quit()
        
        if "open youtube" in query:
            speak("Do you want to search anything on youtube?")
            answer = takeCommand().lower()
            if "yes" in answer or "search" in answer:
                if "yes" in answer and "search" not in answer:
                    answer = answer[answer.index("yes") + 4:]
                else:
                    answer = answer[answer.index("search") + 7:]
                webbrowser.get(chrome_path).open("https://www.youtube.com/results?search_query=" + answer)
                response += f"Searching {answer}"
                speak(response)
                continue
            else:
                speak("Okay. Opening youtube")
                webbrowser.open("https://www.youtube.com")
                continue

        elif "open google" in query:
            speak("Do you want to search anything on google?")
            answer = takeCommand().lower()
            if "yes" in answer or "search" in answer:
                if "yes" in answer and "search" not in answer:
                    answer = answer[answer.index("yes") + 4:]
                else:
                    answer = answer[answer.index("search") + 7:]
                webbrowser.get(chrome_path).open("https://www.google.com/search?q=" + answer)
                response += f"Searching {answer}"
                speak(response)
                continue
            else:
                speak("Okay. Opening google")
                webbrowser.get(chrome_path).open("https://www.google.com")
                continue
        
        elif "open wikipedia" in query:
            speak("Do you want to search anything on wikipedia?")
            answer = takeCommand().lower()
            if "yes" in answer or "search" in answer:
                if "yes" in answer and "search" not in answer:
                    answer = answer[answer.index("yes") + 4:]
                else:
                    answer = answer[answer.index("search") + 7:]
                webbrowser.get(chrome_path).open("https://en.wikipedia.org/wiki/" + answer)
                response += f"Searching {answer} on wikipedia"
                speak(response)
                continue
            else:
                speak("Okay. Opening wikipidea")
                webbrowser.get(chrome_path).open("https://www.wikipedia.com")
                continue

        elif ("open" in query) and ("on chrome" in query or "on google" in query or "in chrome" in query):
            response += open_in_web()

        if "bye" in query:
            response = Goodbye()
            speak(response)
            quit()

        if "good night" in query or "goodnight" in query:
            response = wishGoodnight()
            speak(response)
            quit()

        if keyboard.is_pressed('Esc'):
            response = Goodbye()
            quit()

        if response == "":
            continue

        print(response)
        speak(response)
        
        
        

