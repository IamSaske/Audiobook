import pyttsx3
import PyPDF2
engine=pyttsx3.init('sapi5')
newVoiceRate=150#voice speed
engine.setProperty('rate',newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def bookr(book):
 reader=PyPDF2.PdfFileReader(book)
 pages=reader.numPages
 print(pages)
 for i in range(6,pages):
    page=reader.getPage(i)
    text=page.extractText()
    print(text)
    speak(text)
speak("Welcome to Saske library")
num=int(input("enter book no:"))
if num==1:
    book = open('Ashlee Vance - Elon Musk; Tesla, SpaceX, and the Quest for a Fantastic Future.pdf', 'rb')
    speak("Ashlee Vance - Elon Musk; Tesla, SpaceX, and the Quest for a Fantastic Future.pdf")
    bookr(book)
#similarly you can add more books and if statements