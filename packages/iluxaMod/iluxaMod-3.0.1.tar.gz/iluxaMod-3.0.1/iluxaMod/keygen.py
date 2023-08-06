

class KeysGen:
    def __init__(self, upper=False):
        self.lst = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if upper:
            self.lst = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def generate(self):
        from random import choice as cho

        def prgf():
            return cho(self.lst) + cho(self.lst) + cho(self.lst) + cho(self.lst) + cho(self.lst) + cho(self.lst)

        return str(f"{prgf()}-{prgf()}-{prgf()}-{prgf()}-{prgf()}-{prgf()}")
