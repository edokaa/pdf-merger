from PDFMerger.merger import PDFMerger

mergeObj = PDFMerger()


def run():
    while True:
        print("Press 1 to select and merge pdfs")
        print("Press 0 to cancel")
        enter = input()
        if enter == '1':
            mergeObj.save()
        elif enter == '0':
            break
        else:
            print("invalid input")
            run()