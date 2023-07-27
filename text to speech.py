import pyttsx3
speech_text=pyttsx3.init()
fo=open("C:\\Users\\Prabhakar reddy\\Desktop\\1.txt","r")
ip=fo.read()
fo.close()
speech_text.setProperty("rate",150)
speech_text.setProperty("volume",1)
'''speech_text.save_to_file(ip,"C:\\Users\\Prabhakar reddy\\Desktop\\1.mp3")'''
speech_text.say(ip)
speech_text.runAndWait()
