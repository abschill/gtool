import pyttsx3,PyPDF2, sys
pdfreader = PyPDF2.PdfFileReader(open(sys.argv[1],'rb'))
speaker = pyttsx3.init()
for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    cleaned_text = text.strip().replace('\n',' ')
    print(cleaned_text)
    speaker.save_to_file(cleaned_text,sys.argv[2])
    speaker.runAndWait()
speaker.stop()
