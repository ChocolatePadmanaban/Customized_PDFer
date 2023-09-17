from PyPDF2 import PdfReader, PdfWriter
import sys ,os
from datetime import datetime

def front_Back(input_file_name):
    reader = PdfReader(input_file_name, strict=False)
    writer = PdfWriter()
    input_file=open(input_file_name,'rb')
    writer.append(input_file)
    total_file_length=len(writer.pages)

    front_back_length = total_file_length//2
    if total_file_length % 2 != 0:
        front_back_length += 1
        blank_pages_needed = total_file_length % 2
        for _ in range(blank_pages_needed):
            writer.add_blank_page()
    
    front_writer, back_writer = PdfWriter(),PdfWriter()
    for i in range(front_back_length):
        front_writer.add_page(writer.pages[2*i])
        back_writer.add_page(writer.pages[2*i+1])
    
    with open(input_file_name.replace('.pdf','_front.pdf'),mode='wb') as output_file:
        front_writer.write(output_file)
    with open(input_file_name.replace('.pdf','_back.pdf'),mode='wb') as output_file:
        back_writer.write(output_file)



if __name__=="__main__":
    front_Back(sys.argv[1])