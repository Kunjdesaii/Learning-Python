import speech_recognition as k
import pyttsx3
import webbrowser
from openai import OpenAI

music = {
    "monkey": "https://www.youtube.com/watch?v=qU9mHegkTc4&pp=ygUINW81IHNvbmc%3D",
    "light": "https://www.youtube.com/watch?v=siO6dkqidc4",
    "tum ho": "https://www.youtube.com/watch?v=gkCKTuR-ECI&pp=ygUGdHVtIGhv"
}


def process_command(c):
    c = c.lower()
    
    if "open youtube" in c:
        webbrowser.open("https://www.youtube.com")
    elif "open google" in c:
        webbrowser.open("https://www.google.com")
    elif "open github" in c:
        webbrowser.open("https://github.com")
    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in c:
        webbrowser.open("https://www.instagram.com")
    elif "open twitter" in c:
        webbrowser.open("https://www.twitter.com")      
    elif "open whatsapp" in c:
        webbrowser.open("https://web.whatsapp.com")
    elif "open gmail" in c:
        webbrowser.open("https://mail.google.com")
    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com")
    elif "open spotify" in c:
        webbrowser.open("https://www.spotify.com")  
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "", 1).strip()
        link=music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I don't have that song in my playlist.")
    else:
        output = aai(c)
        speak(output)


recognizer= k.Recognizer()
engine= pyttsx3.init()
    
def speak(text):            
    engine.say(text)
    engine.runAndWait()

def aai(command):
    client = OpenAI(api_key="AIzaSyC_VEEIzf70LL9E8zR7Tbyx7fJuseYCVwo",)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content":command}
        ]
    )
    return completion.choices[0].message.content       

if __name__ == "__main__":
    speak("jarvis at your service")

    while True:
        r = k.Recognizer()
        # print("recognizing...")
        try:
            with k.Microphone() as source:
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                # print("listening...")
            word = r.recognize_google(audio)
            if(word.lower() == "jimmy" or word.lower() == "jarvis" or word.lower() == "jervis" or word.lower() == "friday"):
                speak("yes Boss give me a order")
                
                with k.Microphone() as source:
                    print("jarvis is activated, listening for command...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("You said: " + command)
                    

                    process_command(command)


                    


        except Exception as e:
            print("error:".format(e))

        
                                
