from Dodo_SubEngine import *

print("\t\t----Program Started----")
flag = False
while True:
    with sr.Microphone() as source:
        input("---------------------------------\nPress Enter to Start listening >>")
        print("Listening...")
        cmd = r.listen(source)
        print("Recognizing")
        cmd = r.recognize_google(cmd).lower()
        print("<< " + cmd)
        for i in db:
            if i in cmd:
                speak(db[i][db[i].index(choice(db[i]))])
                flag = True
                break
            elif "how is weather" in cmd:
                speak(str(weather("hyderabad", "telangana", "65194939386cd54dc720b99f764446a9")))
                flag = True
                break
            elif "open google" in cmd:
                speak("Opening Google")
                webbrowser.open("www.google.com")
                flag = True
                break
            elif "on wikipedia" in cmd:
                speak("Searching")
                cmd = cmd.replace("on wikipedia", "")
                speak(wiki(cmd))
                flag = True
                break
            else:
                flag = False
        if not flag:
            speak("NO results")
