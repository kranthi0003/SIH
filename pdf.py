'''import PyPDF2 as pd
from PyPDF2 import PdfFileReader 
  
# creating a pdf file object 
pdfFileObj = open('/home/kranthi-kiran/Desktop/test.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = pd.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
print(pdfReader.numPages) 
  
# creating a page object 
pageObj = pdfReader.getPage(0) 
  
# extracting text from page 
print(pageObj.extractText()) 
  
# closing the pdf file object 
pdfFileObj.close() '''

'''from tika import parser
parsed = parser.from_file('/home/kranthi-kiran/Desktop/test.pdf')
print(parsed["content"])
'''

'''import PyPDF2 as pd

pdfFileObj = open('/home/kranthi-kiran/Desktop/test.pdf', 'rb')

pdfReader = pd.PdfFileReader(pdfFileObj) 

text_chupi = pdfReader.numPages()

pageObject = pdfReader.getPage(text_chupi-1)

text = pageObject.extractText()
print(text)'''

'''EOF_MARKER = b'%%EOF'
file_name = '/home/kranthi-kiran/Desktop/test.pdf'

with open(file_name, 'rb') as f:
    contents = f.read()

# check if EOF is somewhere else in the file
if EOF_MARKER in contents:
    # we can remove the early %%EOF and put it at the end of the file
    contents = contents.replace(EOF_MARKER, b'')
    contents = contents + EOF_MARKER
else:
    # Some files really don't have an EOF marker
    # In this case it helped to manually review the end of the file
    print(contents[-8:]) # see last characters at the end of the file
    # printed b'\n%%EO%E'
    contents = contents[:-6] + EOF_MARKER

with open(file_name.replace('.pdf', '') + '_fixed.pdf', 'wb') as f:
    f.write(contents)'''

import PyPDF2 as pd
with open("/home/kranthi-kiran/Desktop/test.pdf", "rb") as infile:
    input1 = pd.PdfFileReader(infile)
    print("document1.pdf has %d pages." % input1.getNumPages())