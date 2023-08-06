
APP_NAME = "iluxaMod"
VERSION = "3.0.2"
MESSAGE = """Developed by Illya Lazarev (https://sbdt.pro)"""
SINCE = "Since 2022"

STDOUT = True


class App:
    @staticmethod
    def start():
        if STDOUT:
            print(f"""{APP_NAME} version {VERSION}

{MESSAGE}
{SINCE}
#################################################

        """)