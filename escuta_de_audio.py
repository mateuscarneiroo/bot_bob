import speech_recognition as sr
import os

def mainfunction(source):
        audio = r.listen(source)
        try:
                user = r.recognize_google(audio, language = 'pt')
                print("Você falou: " + user)
                for treino in os.listdir("C:\\Users\\Carneiroooo\\Desktop\\IA"):
                        if (treino == "speech_recognition.txt"):
                                frases = open("C:\\Users\\Carneiroooo\\Desktop\\IA" +'\\'+treino, 'a', encoding='utf-8')
                                frases.write(user + '\n')
                                frases.close()
        except sr.UnknownValueError:
                print('Não entendi')
        except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            
if True:
        if __name__ == "__main__":
                print('a')
                r = sr.Recognizer()
                print('b')
                with sr.Microphone() as source:
                        print('c')
                        while 1:
                                print('d')
                                mainfunction(source)
                                print('e')
