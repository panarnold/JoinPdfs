#! python
# joinpdfs.py - usage:
# script will join all pdf documents into one from cwd
# it will search for every pdf file in cwd, sort them by name, and put them into one

import PyPDF2, os

pdf_files = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_files.append(filename)
pdf_files.sort(key=str.lower)

pdf_writer = PyPDF2.PdfFileWriter()

for filename in pdf_files:
    pdf_file_obj = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    for page_num in range(1, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)

pdfOutput = open('allpdfsarehereyo.pdf', 'wb')
pdf_writer.write(pdfOutput)
pdfOutput.close()