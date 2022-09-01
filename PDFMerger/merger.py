import PyPDF2
from tkinter.filedialog import *


class PDFMerger:

    def openFiles(self):
        print('>>> Select the pdf files to merge')
        files = askopenfilenames()
        if len(files) == 1:
            print('>>> Kindly Select more than one pdf file')
            return self.openFiles()
        elif len(files) == 0:
            files = None
        else:
            for item in files:
                if item[-4:] != '.pdf':
                    print('Only .pdf files are supported!!! ')
                    return self.openFiles()
        return files

    def mergeFiles(self):
        pdfFiles = self.openFiles()
        if pdfFiles is not None:
            pdfWriter = PyPDF2.PdfFileWriter()

            for filename in pdfFiles:
                pdfFileObj = open(filename, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

                for pageNum in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(pageNum)
                    pdfWriter.addPage(pageObj)
            print('>>> Merging Done!!!')
            return pdfWriter
        return None

    def save(self):
        pdfWriter = self.mergeFiles()
        if pdfWriter is not None:
            outputFileName = input('>>>Enter Output File name: ')
            print('>>> Select Output Directory')
            outputDir = askdirectory()
            print('output: ', outputDir)
            pdfOutput = open(f"{outputDir}\\{outputFileName}.pdf", 'wb')
            pdfWriter.write(pdfOutput)
            pdfOutput.close()
            print('>>> Saved Successfully!!!')
        
