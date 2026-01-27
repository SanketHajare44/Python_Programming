# Duck Typing : It is concept where the type of an object is determined
# by its behaviour , not by its class

class InjetPrinter:
    def printdocument(self,Document):
        print("Injet Printer printing : ",Document)


class LaserPrinter:
    def printdocument(self,Document):
        print("Laser Printer printing : ",Document)


class PDFWriter:
    def printdocument(self,Document):
        print(f"Saving {Document} as PDF")
    
def StartPrinting(Device):
    Device.printdocument("Marvellous Notes")

def main():
    StartPrinting(InjetPrinter())
    StartPrinting(InjetPrinter())
    StartPrinting(PDFWriter())

main()