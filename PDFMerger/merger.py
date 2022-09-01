import PyPDF2
from tkinter.filedialog import *


class PDFMerger:

    def openFiles(self):
        print('>>> Select the pdf files to merge')
        files = askopenfilenames()
        if len(files) < 2:
            print('>>> Kindly Select more than one pdf file')
            return self.openFiles()
        else:
            return files

    def mergeFiles(self):
        pdfFiles = self.openFiles()
        pdfWriter = PyPDF2.PdfFileWriter()

        for filename in pdfFiles:
            pdfFileObj = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

            for pageNum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
        print('>>> Merging Done!!!')
        return pdfWriter

    def save(self):
        pdfWriter = self.mergeFiles()
        outputFileName = input('>>>Enter Output File name: ')
        print('>>> Select Output Directory')
        outputDir = askdirectory()
        pdfOutput = open(f"{outputDir}\\{outputFileName}.pdf", 'wb')
        pdfWriter.write(pdfOutput)
        pdfOutput.close()
        print('>>> Saved Successfully!!!')
