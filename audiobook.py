import pyttsx3
import PyPDF2
import OpenCV2
book = open("C:\\Users\\hp\\Desktop\\401853005_RaghavWadhwa.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(1, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
