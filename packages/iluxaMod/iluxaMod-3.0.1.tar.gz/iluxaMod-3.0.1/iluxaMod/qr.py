

class qr:
    def __init__(self, data):
        self.data = data

    def create(self, filename="qr_code.jpg", version=4, border=2):
        import qrcode
        qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=version, border=border,)
        qr.add_data(self.data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="green", back_color="black")
        img.save(filename, "JPEG")
