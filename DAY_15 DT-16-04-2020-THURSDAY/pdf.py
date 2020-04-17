import PyPDF2

with open("11.3 dummy.pdf.pdf","rb") as file:
    print(file)
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    print(reader.getPage(0c))
