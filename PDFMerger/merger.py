import PyPDF2
from tkinter.filedialog import *


class PDFMerger:

    def openFiles(self):
        print('>>> Select the pdf files to merge')
        files = askopenfilenames()

        # prompt user to select more than 1 file

        if len(files) == 1:
            print('>>> Kindly Select more than one pdf file')
            return self.openFiles()

        elif len(files) == 0:
            # no file is selected
            files = None

        else:

            # more than 1 file selected...
            # check if files are in pdf format

            for item in files:
                if item[-4:] != '.pdf':
                    print('Only .pdf files are supported!!! ')
                    return self.openFiles()

            print(f'{len(files)} files selected')

        return files

    def mergeFiles(self):
        pdfFiles = self.openFiles()
        if pdfFiles is not None:
            pdfWriter = PyPDF2.PdfFileWriter()

            # read, extract and merge the content of each selected file

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
            outputFileName = input('>>> Enter Output File name: ')
            print('>>> Select Output Directory')
            outputDir = askdirectory()
            pdfOutput = open(f"{outputDir}\\{outputFileName}.pdf", 'wb')
            pdfWriter.write(pdfOutput)
            pdfOutput.close()
            print('>>> Merging successful, file saved to ', outputDir)
