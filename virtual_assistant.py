import pyttsx3
import datetime 
import speech_recognition as sr
import random
import wikipedia
import keyboard
import webbrowser

engine = pyttsx3.init()

# setting up the voice of the virtual assistant
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[14].id)
engine.setProperty('rate', 170)

# edit the path accordingly
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

greet_lst = ["hello", "hey", "hi", "hey there", "hey buddy", "howdy"]
greet_lst_two = ["how are you", "how are things going", "how have you been", "what's up", "what's new", "what's shaking"]

def speak(audio):
    '''function through which the virtual assistant will speak its response'''

    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''to greet the user according to the time'''

    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good morning sir")
    
    elif 12 <= hour < 18:
        speak("Good afternoon sir")
    
    else:
        speak("Good evening sir ")
        
    speak("How may i help you")

def takeCommand():
    '''To listen to the query'''

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

    lst = ["what is the mean    ing of ", "what is ", "who is ", "meaning of "]
    
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
    time = now.strftime("%I:%M %p")
    
    return "It is " + time

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
    lst = ["i am doing fine. ", "everyone is good. ", "things are going great. ", "everything is awesome. ", "good. thanks. "]
    lst_two = ["And you?", "How about yourself?"]
    return random.choice(lst) + random.choice(lst_two)

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
    lst = ["sweet dreams sir", "good night sir", "see you tomorrow sir"]
    return random.choice(lst)    

def Goodbye():
    lst = ["see you later", "take care", "have a good one", "great to see you sir", "goodbye sir"]
    return random.choice(lst)

if __name__ == "__main__":
    
    wishMe()
    
    while True:
        
        query = takeCommand().lower()
        response = ""
        
        if query == "":
            speak("Could you please repeat that")
            continue

        if "on youtube" in query or "in youtube" in query:
            response += youtube_search()
            speak(response)
            continue
        
        if "on google" in query or "in google" in query:
            response += search_on_google()
            speak(response)
            continue

        if "search" in query or "find" in query:
            lst = query.split()
            query_lst = lst[lst.index("search") + 1:]
            string = " ".join(query_lst)
            webbrowser.get(chrome_path).open("https://www.google.com/search?q=" + string)
            speak(f"Searching {string} on google")

        if "how are you" in query or "what's up" in query:
            response += how_are_you_reply()

        if "date" in query:
            get_date = getDate()
            response = response + " Today is " + get_date
        
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

        elif "on chrome" in query or "on google" in query or "in chrome" in query:
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
        
        
        

