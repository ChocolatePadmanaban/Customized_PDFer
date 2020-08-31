from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

# pdf_path =(Path.home())
# print("pdf_path ",pdf_path)
# input_file_name= 'MIT14_01SCF11_soln01.pdf'
# pdf = PdfFileReader(input_file_name)

# print(pdf.getNumPages())
# #print(pdf.documentInfo.tile)

# output_file_name= input_file_name.replace(".pdf",".txt")

# with open(output_file_name,mode="w") as output_file:
#     # 3
#     title = output_file_name.replace(".txt","")
#     num_pages = pdf.getNumPages()
#     output_file.write(f"{title}\\nNumber of pages: {num_pages}\\n\\n")

#     # 4
#     for page in pdf.pages:
#         text = page.extractText()
#         output_file.write(text)


def Coutomized_extraction (input_file_name):
    """ this file will extract front pages and back pages and 
    put it as new files with the same name
    """
    input_pdf = PdfFileReader(input_file_name)
    pdf_front_writer = PdfFileWriter()
    pdf_back_writer = PdfFileWriter()
    def alternate():
        while True:
            yield 0
            yield 1
    alternate = alternate()
    pdf_writer_list = [pdf_front_writer,pdf_back_writer]
    temp_pdf_writer = pdf_writer_list[alternate.__next__()]
    for i in range(input_pdf.getNumPages()):
        temp_page = input_pdf.getPage(i)
        temp_pdf_writer.addPage(temp_page)
        if (i+1) %2 == 0 : temp_pdf_writer = pdf_writer_list[alternate.__next__()]
    with open(input_file_name.replace(".pdf", "_front.pdf"), mode='wb') as output_file:
        pdf_front_writer.write(output_file)
    with open(input_file_name.replace(".pdf", "_back.pdf"), mode='wb') as output_file:
        pdf_back_writer.write(output_file)

if __name__ == "__main__":
    Coutomized_extraction('MIT14_01SCF11_soln01.pdf')
