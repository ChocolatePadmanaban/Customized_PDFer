from PyPDF2 import PdfReader, PdfWriter
import sys ,os
from datetime import datetime


def booklet_Prep(input_file_name):
    reader = PdfReader(input_file_name, strict=False)
    writer = PdfWriter()
    input_file=open(input_file_name,"rb")
    writer.append(input_file)
    total_file_length = len(writer.pages)
    
    
    
    booklet_length = total_file_length//4 +1
    if total_file_length % 4 != 0: 
        blank_pages_needed = 4 - total_file_length % 4
        for _ in range(blank_pages_needed):
            writer.add_blank_page()

    front_writer, back_writer = PdfWriter(), PdfWriter()
    for i in range(len(writer.pages)):
        if i %2 == 0 :
            front_writer.add_page(writer.pages[i])
        else:
            back_writer.add_page(writer.pages[i])
    flip_fwriter, flip_bwriter = PdfWriter(), PdfWriter()
    for i in range(booklet_length):
        flip_fwriter.add_page(front_writer.pages[i])
        flip_fwriter.add_page(back_writer.pages[-(i+1)])
        flip_bwriter.add_page(back_writer.pages[i])
        flip_bwriter.add_page(front_writer.pages[-(i+1)])
    with open(input_file_name.replace(".pdf", "_front.pdf"), mode='wb') as output_file:
        flip_fwriter.write(output_file)
    with open(input_file_name.replace(".pdf", "_back.pdf"), mode='wb') as output_file:
        flip_bwriter.write(output_file)

    # directory_name= datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    # try:
    #     os.mkdir(directory_name)
    # except:
    #     pass


    # with open(directory_name+"/"+directory_name+".pdf", mode='wb') as output_file:
    #     writer.write(output_file)

if __name__=="__main__":
    booklet_Prep(sys.argv[1])
    