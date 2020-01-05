import PyPDF2

class text_Convertor():
    print('Hi1')
    pdfFileObj = open('G:/SIH/Project/SIH/uploads/sample.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print("Number of pages:-"+str(pdfReader.numPages))
    num = pdfReader.numPages
    i =0
    file_res = open('G:/SIH/Project/SIH/converts/sample1.txt','w',encoding='UTF-8')
    while(i<num):
        pageObj = pdfReader.getPage(i)
        text=pageObj.extractText()
        print(text)
        file_res.write('\n\nPage: '+str(i+1)+'\n\n'+text)
        i=i+1