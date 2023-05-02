import pyttsx3 as p

text=p.init()
user=input("what you want to speech: ")

text.say(user)
text.runAndWait()


