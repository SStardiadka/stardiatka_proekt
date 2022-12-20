# из txt файла конвертировать в pdf
import aspose.words as aw

# load TXT document
doc = aw.Document(r"C:\stardiatka_proekt-1\python\Wfiles\data111.txt")

# save TXT as PDF file
doc.save(r"C:\stardiatka_proekt-1\python\Wfiles\txt-to-pdf.pdf", aw.SaveFormat.PDF)