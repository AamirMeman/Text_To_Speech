import win32com.client
if __name__ == '__main__':
    speaker=win32com.client.Dispatch("SAPI.spvoice")
    while True:
        print("Enter what u want to me to speak: ")
        s=input()
        if s=="q":
            break
        speaker.speak(s)

