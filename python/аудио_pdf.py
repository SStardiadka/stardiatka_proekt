#  из файла pdf создать аудио файл

from text_to_speech import speak
from PyPDF2 import PdfFileReader
def pdf_audio(pdf_path):
    text = []
    with open(pdf_path,'rb') as f:
        pdf = PdfFileReader(f)
        for i in pdf.pages:
            text.append(i.extractText())
    speak(' '.join(text), save=True, file='audio_book1.mp3')


pdf_audio(r'C:\Users\user\Desktop\10.pdf')  

