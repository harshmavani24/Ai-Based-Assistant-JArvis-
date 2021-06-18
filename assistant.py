from time import time
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyautogui as pg
import random
from wikipedia import exceptions
import pyjokes
from wikipedia.wikipedia import languages
import time , requests
edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
google = "https://www.google.com"
ss = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100']
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("i am your personal assistant . Please tell me how may I help you")       
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
#Mail 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nk6xzoyrsp7@gmail.com', 'Harsh@2454')
    server.sendmail('nk6xzoyrsp7@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'are you male' in query:
            speak("no i not male i am female and i am your personal assistant")
        elif 'what is your birth date' in query:
            speak("Well Mhm Security's Birthday is July 24th,and i wouldn't be here without Mhm Security,so i guess that's my birth date")
        elif 'how old are you' in query:
            speak("cannot determine the age")
#Random USe:--
        elif 'roll one dice' in query:
            nums = 1,2,3,4,5,6
            a = random.choices(nums)
            print(a)
            speak(a)
        elif 'roll two dice' in query:
            nums = 2,3,4,5,6,7,8,9,10,11,12
            a = random.choices(nums)
            print(a)
            speak(a)
        #open File And Application On My Pc
        elif 'cmd' in query:
            cmdPath = "C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(cmdPath)
        elif 'open code' in query:
            codePath = "C:\\Users\Harsh Mavani\\AppData\Local\\Programs\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'sleep' in query:
            pg.keyDown('win')
            pg.press('x')
            pg.keyUp('win')
            pg.press('up', presses=2)
            pg.press('enter')
            pg.press('down')
            pg.press('enter')
        elif 'log out' in query or 'sign out' in query:
            pg.keyDown('win')
            pg.press('x')
            pg.keyUp('win')
            pg.press('up', presses=2)
            pg.press('enter', presses=2)
        elif 'shutdown' in query or 'turn off' in query:
            pg.keyDown('win')
            pg.press('x')
            pg.keyUp('win')
            pg.press('up', presses=2)
            pg.press('enter')
            pg.press('down' , presses=2)
            pg.press('enter')
        elif 'restart' in query:
            pg.keyDown('win')
            pg.press('x')
            pg.keyUp('win')
            pg.press('up', presses=2)
            pg.press('enter')
            pg.press('up')
            pg.press('enter')

        elif 'take screenshot' in query:
            speak('oohk')
            myScreenshot = pg.screenshot()
            myScreenshot.save(r'H:\\Python Coding Projects\\pyss\\'+random.choice(ss)+'.png')
            speak('done')
            speak('Tell Me More ')
        #Youtube Special Keys And Search
        elif 'my video' in query:
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('edge').open("youtube.com")
            pg.hotkey('f4',interval = '0.35')
            pg.press('tab' , presses=2, interval= '0.35')
            pg.write("tbomb ka baap" , interval='0.01')
            pg.press('enter')
        elif 'open youtube' in query:
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('edge').open("youtube.com")
            pg.hotkey('f4',interval = '0.35')
            pg.press('tab' , presses=2, interval= '0.35')
        elif 'open youtube with mic' in query:
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('edge').open("youtube.com")
            pg.hotkey('f4' , interval= '0.25')
            pg.press('tab' , presses=4 , interval='0.25')
            pg.press('enter')
        elif 'open stack overflow' in query:
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('edge').open("stackoverflow.com")   
        elif 'open new tab' in query or 'open google' in query:
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('edge').open('google.com')
        elif 'open my site' in query or 'my website' in query :
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('edge').open('mhmsecurity.ml')
#windows Fecture
        elif 'minimize window' in query or 'minimise window' in query:
            speak("minimizing windows")
            pg.keyDown('win')
            pg.press('m')
            pg.keyUp('win')
        elif 'open settings' in query:
            speak("opaning settings")
            pg.keyDown('win')
            pg.press('i')
            pg.keyUp('win')
        elif 'switch window' in query or 'switch window' in query:
            speak("switching windows")
            pg.keyDown('alt')
            pg.press('tab')
            pg.keyUp('alt')
        elif 'close this' in query or 'close these' in query:
            speak("closed window")
            pg.keyDown('alt')
            pg.press('f4')
            pg.keyUp('alt')
        #elif 'delete file' in query or 'delete folder' in query:

#joke with python
        elif 'joke' in query or 'jok' in query or 'juke' in query:
            a = pyjokes.get_joke(language='en', category='all')
            print(a)
            speak(a)
            while True:
                    speak("Do You Want one More")
                    content3 = takeCommand()
                    if content3 == "yes":
                        b = pyjokes.get_joke()
                        print(b)
                        speak(b)
                    elif content3 == "no":
                        speak("Thanks for listining my jokes.")
                        break
#calculator
        elif 'open calcultor' in query:
            os.startfile("C:\\Windows\\System32\\calc.exe")
        elif 'open kali' in query:
            os.startfile("C:\\Windows\\System32\\bash.exe")

        elif 'news' in query:
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('edge').open("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
#friends 
        elif 'my friend site' in query:
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('edge').open('omsangani.ml')
        elif 'my all friend website' in query:
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('edge').open('omsangani.ml')
            webbrowser.get('edge').open('princekhunt.com')
            webbrowser.get('edge').open('aboutkelvis.gq')
        elif 'my all friend in instagram' in query:
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('edge').open('https://www.instagram.com/omsangani29/')
            webbrowser.get('edge').open('https://www.instagram.com/prince._khunt/')
            webbrowser.get('edge').open('https://www.instagram.com/aryan_03.12/')
            webbrowser.get('edge').open('https://www.instagram.com/harshvirani09/')
            webbrowser.get('edge').open('https://www.instagram.com/7.yug__/')
            webbrowser.get('edge').open('https://www.instagram.com/smit_1803/')
            webbrowser.get('edge').open('https://www.instagram.com/kelvis__k/')
            webbrowser.get('edge').open('https://www.instagram.com/vats_0712/')
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'mail to harsh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harshmavani000786@gmail.com"    
                sendEmail(to, content)
                speak("Email Has Been Sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend harsh bhai. I am not able to send this email")    
        elif 'mail to om' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "omsangani29@gmail.com"    
            except Exception as e:
                print(e)
                speak("Sorry my friend harsh bhai. I am not able to send this email")   
        elif 'open whatsapp' in query:
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('edge').open("web.whatsapp.com")
        elif 'send file to sangani' in query:
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('edge').open("mail.google.com")
            pg.sleep(5)
            pg.press('tab' , presses=12)
            pg.press('enter')
            pg.sleep(1)
            pg.press('tab' , presses=5)
            pg.press('enter')
        elif 'send message to venom' in query:
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
            webbrowser.get('edge').open("https://web.whatsapp.com")
            pg.sleep(6)
            pg.press('tab' , presses=4, interval='0.50')
            try:
                speak('What Should I Say !!')
                content1 = takeCommand()
                pg.write(content1)
                pg.press('enter')
                while True:
                    speak("Tell me More")
                    content2 = takeCommand()
                    pg.write(content2)
                    pg.press('enter')
                    if 'close this' in content2:
                       pg.hotkey('alt', 'f4')
                       pg.press('enter')
                       break
            except exceptions as e:
                print(e)
                speak("Sorry Sir, I can't send your message.")

#Whether in AI
        elif "weather" in query:
            api_key = "6cdda53a809c9476d52c4493939e538f"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +str(current_temperature) +"\n humidity in percentage is " +str(current_humidiy) +"\n description " + str(weather_description))
                print(" Temperature in kelvin unit = " + str(current_temperature) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))

        
        else:
            if  ' in youtube' in query:
                speak('According To Youtube')
                webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
                webbrowser.get('edge').open("https://www.youtube.com/results?search_query="+query)
                
            else:
                speak('According to google')
                webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
                webbrowser.get('edge').open('https://www.google.com/search?q='+query)
                
