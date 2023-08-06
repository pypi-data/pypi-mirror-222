

class Barcode:
    def __init__(self, frame):
        from PIL import Image
        self.frame = frame
        self.source_img = Image.open(frame)

    def scan(self):
        from pyzbar.pyzbar import decode
        self.decoded = decode(self.source_img)
        return self.decoded[0].data.decode('utf-8')
