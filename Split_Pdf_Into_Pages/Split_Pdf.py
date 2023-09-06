# Usage:
# python Split_Pdf.py "/Users/padmanabanpr/Documents/Pradeep_official/Page_no.pdf"

from PyPDF2 import PdfReader, PdfWriter
import sys ,os
from datetime import datetime


def split_Pdf(file_name):
    """
    Input: InputFileName
    Output :
    - Dir with each page as list
    """
    reader = PdfReader(file_name, strict=False)
    directory_name= datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
    try:
        os.mkdir(directory_name)
    except:
        pass
    for i in range(len(reader.pages)):
        writer = PdfWriter()
        with open(directory_name+"/"+str(i+1)+".pdf", mode='wb') as output_file:
            writer.add_page(reader.pages[i])
            writer.write(output_file)

if __name__=="__main__":
    split_Pdf(sys.argv[1])