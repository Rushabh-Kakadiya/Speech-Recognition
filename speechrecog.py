import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
import time
import wolframalpha
import requests
import webbrowser
import subprocess

def playaudio(audio):
    playsound(audio)
    
global n
def speaks_audio(output): 
    n=0
    n=n+1
    print("Nes : ",output)
    
    audio=gTTS(text=output,lang="en",slow=False)
    
    file=str(n)+".mp3"
   
    audio.save(file)
    
    playaudio(file)
    
    
def get_audio(): 
    rec_obj = sr.Recognizer() 
    audio = '' 
    with sr.Microphone() as source: 
        print("Speak...") 
        audio = rec_obj.listen(source, phrase_time_limit =5)  
        print("Stop.")
  
    try: 
        text = rec_obj.recognize_google(audio, language ='en-US') 
        print("You : ", text) 
        return text 
  
    except: 
        speaks_audio("Could not understand your audio, PLease try again !") 
        return 0
    
def process_text(input): 
    try: 
        if "hey" in input or "hi" in input or "hello" in input:
            speaks_audio("hi")
        elif "search" in input or "google" in input.lower() or "play" in input or "youtube" in input or "online" in input: 
            search_web(input) 
            return
        elif 'open' in input: 
            open_application(input.lower())  
            return
        elif 'what is your name' in input:
            speak="Nes."
            speaks_audio(speak)
            return
        elif 'how are you' in input.lower():
            speak="I am Fine"
            speaks_audio(speak)
            return
        elif "who are you" in input or "define yourself" in input: 
            speak= '''Hello, I am Nes. Your personal Assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks such as calculating sums or opening applications etcetra'''
            speaks_audio(speak) 
            return
        elif "who made you" in input or "created you" in input: 
            speak = "I have been created by someone like you,just smarter."
            speaks_audio(speak) 
            return
  
        elif "calculate" in input.lower(): 
            app_id = "WE6LL5-2A95EYT22P" 
            client = wolframalpha.Client(app_id) 
            indx = input.lower().split().index('calculate') 
            query = input.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            speaks_audio("The answer is " + answer) 
            return

        elif 'what time' in input.lower() or 'tell time' in input.lower():
            t=time.ctime()
            speaks_audio(t)

       

        elif 'joke' in input:
            res = requests.get('https://icanhazdadjoke.com/',headers={"Accept":"application/json"})
            if res.status_code == requests.codes.ok:
                speaks_audio(str(res.json()['joke']))
            else:
                speaks_audio('oops!I ran out of jokes')
    
        else: 
            speaks_audio("I can search the web for you, Do you want to continue?") 
            ans = get_audio() 
            if 'yes' in str(ans) or 'yeah' in str(ans): 
                search_web(input) 
            else: 
                return
    except : 
        speaks_audio("I don't understand, I can search the web for you, Do you want to continue?") 
        ans = get_audio() 
        if 'yes' in str(ans) or 'yeah' in str(ans): 
            search_web(input)
        elif 'no' in str(ans) or 'nope' in str(ans):
            exit
            
def search_web(input): 
    
    if 'youtube' in input.lower(): 
        speaks_audio("Opening in youtube") 
        indx = input.lower().split().index('youtube') 
        query = input.split()[indx + 1:] 
        url="http://www.youtube.com/results?search_query="+'+'.join(query) 
        webbrowser.get().open(url)
        return
  
    elif 'wikipedia' in input.lower(): 
        speaks_audio("Opening Wikipedia") 
        indx = input.lower().split().index('wikipedia') 
        query = input.split()[indx + 1:] 
        url="https://en.wikipedia.org/wiki/" + '_'.join(query)
        webbrowser.get().open(url)
        return
  
    else: 
        if 'google' in input or "Google" in input: 
            indx = input.lower().split().index('google') 
            query = input.split()[indx + 1:] 
            url="https://www.google.com/search?q="+'+'.join(query)
            webbrowser.get().open(url)
  
        elif 'search' in input: 
            indx = input.lower().split().index('search') 
            query = input.split()[indx + 1:] 
            url="https://www.google.com/search?q="+'+'.join(query)
            webbrowser.get().open(url)
  
        else: 
            url="https://www.google.com/search?q"+'+'.join(query)
            webbrowser.get().open(url)
        return

def open_application(input): 
    
    str2=input.split()
    i=0
    str3=""
    for j in str2:
        if i==0:
            i=i+1
            continue
        elif i==1:
            str3=str3+j
            i=i+1
        else:
            str3=str3+" "+j
        
    str4="/System/Applications/"+str3+".app"
    str5="/Applications/"+str3+".app"
    
    if os.path.exists(str4)==True:
        os.system(f"open {str4}")
        return
        
    elif os.path.exists(str5)==True:
        os.system(f"open {str5}")    
        return
    
    else:
        print("Could not find Application")
        return
    
if __name__ == "__main__":
    try :
        speaks_audio("What's your name?")
        name = get_audio()
        speaks_audio("hello "+name)
    except:
        speaks_audio("What's your name?")
        name = get_audio()
        speaks_audio("hello "+name)
    while(True): 
            speaks_audio("What can i do for you?") 
            text =get_audio()
    
            if text == 0: 
                continue
    
            if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text) or "nothing" in str(text): 
                speaks_audio("Ok bye, "+ name) 
                break
                
            process_text(text)

 








