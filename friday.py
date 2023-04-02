import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import datetime
from gtts import gTTS
import PyPDF2
from bs4 import BeautifulSoup
import requests
from playsound import playsound
from googletrans import Translator
import pyautogui
import keyboard
import pyjokes
import speedtest
from pywikihow import search_wikihow
import os

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voice', voices[2].id)
Assistant.setProperty('rate', 180)

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    Assistant.runAndWait()

def wishme():
        hr = int(datetime.datetime.now().hour)
        if hr>=0 and hr<12:
            Speak("Good Morning Boss!")
        
        elif hr>=12 and hr<17:
            Speak("Good Afternoon Boss!")
        
        else:
            Speak("Good Evening Boss!")
            
        Speak("I Am Friday. Your Personal AI Assistant. Please Tell Me How Can I Help You?")

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1
        audio = command.listen(source)
        
        try:
            print("Recognizng.....")
            query = command.recognize_google(audio,language='en-in')
            
        except:
            return "none"
        
        return query.lower()

def TaskExe():
    wishme()
    def Music():
        Speak("Tell Me The Name Of The Song!")
        musicName = takecommand()
        if 'chere jeyona' in musicName:
            os.startfile('C:\\Users\\GOURAV\\Music\\Resso Music\\Chere Jeyona.mp3')
            
        elif 'oviman' in musicName:
            os.startfile('C:\\Users\\GOURAV\\Music\\Resso Music\\Oviman.mp3')
            
        else:
            pywhatkit.playonyt(musicName)
            Speak("Your Song Has Been Started!, Enjoy Boss..")
            
    def Whatsapp():
        Speak("Tell Me The Name Of the Person!")
        name = takecommand()
        
        if 'mine' in name:
            Speak("Tell Me The Messege!")
            msg = str(takecommand())
            Speak("Tell Me THe Time Boss!")
            Speak("Time In Hour")
            hour = int(takecommand())
            Speak("Time In Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+919883632781", msg, hour, min)
            Speak("Ok Boss, Sending Whatsapp Messege!")
            
        elif 'gourav' in name:
            Speak("Tell Me The Messege!")
            msg = takecommand()
            Speak("Tell Me THe Time Boss!")
            Speak("Time In Hour")
            hour = int(takecommand())
            Speak("Time In Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+919883432474",msg,hour,min)
            Speak("Ok Boss, Sending Whatsapp Messege!")
            
        elif 'suman' in name:
            pywhatkit.sendwhatmsg("+919883432474", "Hi", 21, 24)
            
        else:
            Speak("Tell Me The Number!")
            phone = int(takecommand())
            ph = +91 + phone 
            Speak("Tell Me The Messege!")
            msg = takecommand()
            Speak("Tell Me THe Time Boss!")
            Speak("Time In Hour")
            hour = int(takecommand())
            Speak("Time In Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
            Speak("Ok Boss, Sending Whatsapp Messege!")
            
    def OpenApps():
        Speak("Ok Boss, Wait A Second!")
        
        if 'code' in query:
            os.startfile("D:\\Visual Studio Code\\Application\\Microsoft VS Code\\Code.exe")
            
        elif 'bluestacks' in query:
            os.startfile("C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe")
            
        elif 'r studio' in query:
            os.startfile("C:\\Program Files\\RStudio\\bin\\rstudio.exe")
        
        elif 'sql' in query:
            os.startfile("C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\MySQLWorkbench.exe")
            
        elif 'word' in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
            
        elif 'excel' in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
            
        elif 'powerpoint' in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
            
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')
        
        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com/')
            
        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')
            
        elif 'flipkart' in query:
            webbrowser.open('https://www.flipkart.com/')
            
        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            
        Speak("Your Command Has Been Sucessfully Completed!")
            
    def CloseApps():
        Speak("Ok Boss, Wait A Second!")
        
        if 'code' in query:
            os.system("TASKKILL /F /im code.exe")
            
        elif 'bluestacks' in query:
            os.system("TASKKILL /F /im HD-Player.exe")
            
        elif 'r studio' in query:
            os.system("TASKKILL /F /im rstudio.exe")
            
        elif 'sql' in query:
            os.system("TASKKILL /F /im MySQLWorkbench.exe")
            
        elif 'word' in query:
            os.system("TASKKILL /F /im WINWORD.EXE")
            
        elif 'excel' in query:
            os.system("TASKKILL /F /im EXCEL.EXE")
            
        elif 'powerpoint' in query:
            os.system("TASKKILL /F /im POWERPNT.EXE")
            
        elif 'facebook' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        elif 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        elif 'flipkart' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        elif 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        Speak("Your Command Has Been Sucessfully Completed!")
        
    def YtAuto():
        Speak("Whats Your Command?")
        comm = takecommand()
        
        if 'pause' in comm:
            keyboard.press('k')
            
        elif 'play' in comm:
            keyboard.press('k')
            
        elif 'restart' in comm:
            keyboard.press('0')
            
        elif 'mute' in comm:
            keyboard.press('m')
            
        elif 'skip' in comm:
            keyboard.press('l')
            
        elif 'back' in comm:
            keyboard.press('j')
            
        elif 'full screen' in comm:
            keyboard.press('f')
            
        elif 'default' in comm:
            keyboard.press('f')
            
        elif 'film mode' in comm:
            keyboard.press('t')
            
        Speak("Done Boss!")
        
    def ChromeAuto():
        Speak("Chrome Automation Started")   
        
        command = takecommand()
        
        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')
            
        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')
            
        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')
            
        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')   
            
    def screenshot():
        Speak("Ok Boss, What Should I Name That File?")
        path = takecommand()
        path1name = path + ".png" 
        path1 = "E:\\Coding\\PythonCourse\\Jarvis\\ScreenShots\\"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("E:\\Coding\\PythonCourse\\Jarvis\\ScreenShots")
        Speak("Here Is Your Screenshot")
    
    def TakeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            command.pause_threshold = 1
            audio = command.listen(source)
        
            try:
                print("Recognizng.....")
                query = command.recognize_google(audio,language='hi')
                print(f"You Said : {query}")
            
            except:
                return "none"
        
            return query.lower() 
    
    def Tran():
        Speak("Tell Me The Line")
        line = TakeHindi()
        trans = Translator()
        result = trans.translate(line)
        Text = result.text
        Speak(Text)
    
    def Temp():
        search = "temperature in kolkata"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak(f"The Temperature Is {temperature}")
        
    def Reader():
        Speak("Tell Me The Name Of The Book!")
       
        name = takecommand()
        
        if 'methods of data collection' in name:
            os.startfile('E:\\Coding\\PythonCourse\\Jarvis\\books\\Methods Of Data Collection.pdf')
            book = open('E:\\Coding\\PythonCourse\\Jarvis\\books\\Methods Of Data Collection.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)    
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading?")
            # numPage = int(input("Enter The Page Number :"))
            numPage = int(takecommand())
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language, I have To Read?")
            lang = takecommand()
        
            if 'hindi' in lang:
                trans1 = Translator()
                textHin = trans1.translate(text, 'hi')
                textm = textHin.text
                speech = gTTS(text = textm)
                
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')
                    
                except:
                    playsound('book.mp3')
            
            else:
                Speak(text)
                
            book.close()
        
        elif 'sql' in name:
            os.startfile('E:\\Coding\\PythonCourse\\Jarvis\\books\\SQL.pdf')
            book = open('E:\\Coding\\PythonCourse\\Jarvis\\books\\SQL.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading?")
            # numPage = int(input("Enter The Page Number :"))
            numPage = int(takecommand())
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language, I have To Read?")
            lang = takecommand()
            
            if 'hindi' in lang:
                trans1 = Translator()
                textHin = trans1.translate(text, 'hi')
                textm = textHin.text
                speech = gTTS(text = textm)
                
                try:
                    speech.save('book1.mp3')
                    playsound('book1.mp3')
                    
                except:
                    playsound('book1.mp3')
                    
            else:
                Speak(text)
    
    def SpeedTest():
        Speak("Checking Speed....")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctDown =  int(downloading/800000)
        uploading = speed.upload()
        correctUp = int(uploading/800000)    
        
        if 'uploading' in query:
            Speak(f"The Uploading Speed Is {correctUp} mbp s")
            
        elif 'downloading' in query:
            Speak(f"The Downloading Speed Is {correctDown} mbp s")
            
        else:
            Speak(f"The Downloading Speed Is {correctDown} mbp s and The Uploading Speed Is {correctUp} mbp s")
               
    # def dict():
    #     Speak("Activated Dictionary")
    #     Speak("Tell Me The Problem")
    #     prb = takecommand()
        
    #     if 'meaning' in prb:
    #         prb = prb.replace("what is the","")
    #         prb = prb.replace("friday","")
    #         prb = prb.replace("of","")
    #         prb = prb.replace("meaning of","")
    #         results = Diction.meaning(prb)
    #         Speak(f"The Meaning For {prb} is {results}")
            
    #     elif 'synonym' in prb:
    #         prb = prb.replace("what is the","")
    #         prb = prb.replace("friday","")
    #         prb = prb.replace("of","")
    #         prb = prb.replace("meaning of","")
    #         results = Diction.synonym(prb)
    #         Speak(f"The Synonym For {prb} is {results}")
            
    #     elif 'antonym' in prb:
    #         prb = prb.replace("what is the","")
    #         prb = prb.replace("friday","")
    #         prb = prb.replace("of","")
    #         prb = prb.replace("meaning of","")
    #         results = Diction.antonym(prb)
    #         Speak(f"The Antonym For {prb} is {results}")
    #         Speak("Excited Dictionary!")
    
    while True:
        query = takecommand()
        
        if 'hello' in query:
            Speak("Hello Boss, I Am friday. Your Personal AI Assistant. How May I Help You?")
            
        elif 'how are you' in query:
            Speak("I Am Fine Boss!, Whats About You?")
            
        elif 'you need a break' in query:
            Speak("Ok Boss, You Can Call Me Anytime!")
            quit()
            
        elif 'bye' in query:
            Speak("Ok Boss, Bye!")
            quit()
            
        elif 'quit' in query:
            query = query.replace("friday","")
            Speak("Ok Boss, Bye!")
            quit()
            
        elif'youtube search' in query:
            Speak("Ok Boss, This Is What I Found For Your Search!")
            query = query.replace("friday","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)    
            Speak("Done Boss!")
            
        # elif 'google search' in query:
        #     Speak("Ok Boss, This Is What I Found For Your Search!")
        #     query = query.replace("friday","")
        #     query = query.replace("google search","")
        #     pywhatkit.search(query)
        #     Speak("Done Boss!")
            
        elif 'website' in query:
            Speak("Ok Boss, This Is What I Found For Your Search!")
            query = query.replace("friday","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched...")
            
        elif 'launch' in query:
            Speak("Tell me The Name of the Website")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Launched...")
           
        # elif 'facebook' in query:
        #     Speak("Ok Boss!")
        #     webbrowser.open("https://www.facebook.com")
        #     Speak("Done Boss!")
            
        elif 'music' in query:
            Music()
            
        elif 'wikipedia' in query:
            Speak("Searching Wikipedia....")
            query = query.replace("friday","")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            Speak("According To Wikipedia") 
            Speak(results)     
            
        elif 'whatsapp' in query:
            Whatsapp()
            
        elif 'screenshot' in query:
            screenshot()
            
        elif 'open code' in query:
            OpenApps()
            
        elif 'open bluestacks' in query:
            OpenApps()
            
        elif 'open r studio' in query:
            OpenApps()
            
        elif 'open sql' in query:
            OpenApps()
            
        elif 'open word' in query:
            OpenApps()
            
        elif 'open excel' in query:
            OpenApps()
            
        elif 'open powerpoint' in query:
            OpenApps()
            
        elif 'open facebook' in query:
            OpenApps()
            
        elif 'open instagram' in query:
            OpenApps()
            
        elif 'open youtube' in query:
            OpenApps()
            
        elif 'open flipkart' in query:
            OpenApps()
            
        elif 'open chrome' in query:
            OpenApps()
            
        elif 'close code' in query:
            CloseApps()
            
        elif 'close bluestacks' in query:
            CloseApps()
            
        elif 'close r studio' in query:
            CloseApps()
            
        elif 'close sql' in query:
            CloseApps()
            
        elif 'close word' in query:
            CloseApps()
            
        elif 'close excel' in query:
            CloseApps()
            
        elif 'close powerpoint' in query:
            CloseApps()
            
        elif 'close facebook' in query:
            CloseApps()
            
        elif 'close youtube' in query:
            CloseApps()
            
        elif 'close instagram' in query:
            CloseApps()
            
        elif 'close flipkart' in query:
            CloseApps()
            
        elif 'close chrome' in query:
            CloseApps()
            
        elif 'pause' in query:
            keyboard.press('k')
            
        elif 'play' in query:
            keyboard.press('k')
            
        elif 'restart' in query:
            keyboard.press('0')
            
        elif 'mute' in query:
            keyboard.press('m')
            
        elif 'skip' in query:
            keyboard.press('l')
            
        elif 'back' in query:
            keyboard.press('j')
            
        elif 'full screen' in query:
            keyboard.press('f')
            
        elif 'default' in query:
            keyboard.press('f')
            
        elif 'film mode' in query:
            keyboard.press('t')
            
        elif 'youtube tools' in query:
            YtAuto()
            
        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')
            
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')
            
        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
            
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')
            
        elif 'chrome atumation' in query:
            ChromeAuto()
            
        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)
            
        elif 'repeat my words' in query:
            Speak("Speak Boss!")
            jj = takecommand()
            Speak(f"You Said : {jj}")
            
        elif 'my location' in query:
            webbrowser.open('https://www.google.co.in/maps/@26.7271012,88.3952861,12z?hl=en&authuser=0')

        # elif 'dictionary' in query:
        #     dict()
            
        elif 'alarm' in query:
            Speak("Tell Me The Time!")
            time = input(": Enter The Tine :")
            
            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")
                
                if now == time:
                    Speak("Time To Wake Up Boss!")
                    playsound('E:\\Coding\\PythonCourse\\Jarvis\\ring.mp3')
                    Speak("Alarm Closed!")
                    
                elif now>time:
                    break

        elif 'translator' in query:
            Tran()
            
        elif 'remember that' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = query.replace("friday","")
            Speak("You Tell Me To Remind You That :"+rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()
            
        elif 'what do you remember' in query:
            remember = open('data.txt','r')
            Speak("You Tell Me That"+remember.read())
        
        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("friday","")     
            query = query.replace("google search","")     
            query = query.replace("google","")
            Speak("This is What I found On The Web")
            pywhatkit.search(query)
            
            try:
               result = googleScrap.summary(query,3) 
               Speak(result)
               
            except:
                Speak("No Speakable Data Available!")     

        elif 'temperature' in query:
            Temp()

        elif 'read book' in query:
            Reader()

        elif 'internet speed' in query:
            SpeedTest()
            
        elif 'uploading speed' in query:
            SpeedTest()
            
        elif 'downloading speed' in query:
            SpeedTest()
        
        elif 'how to' in query:
            Speak("Getting Data From The Internet!")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)
        
TaskExe()



