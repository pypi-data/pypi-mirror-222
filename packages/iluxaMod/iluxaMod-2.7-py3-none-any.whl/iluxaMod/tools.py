
class postgreSQL:
    def __init__(self, user="postgres", password="password", database=None, host="localhost"):
        import psycopg2

        self.db = psycopg2.connect(database=database, user=user, password=password, host=host)
        self.sql = self.db.cursor()
        self.init_DB()

    def init_DB(self, stages=False, sub=False, settings=False, staff=False, balance=False, stdout=True):
        if stages:
            self.sql.execute(f"""CREATE TABLE IF NOT EXISTS stages(
            user_id TEXT PRIMARY KEY,
            stage TEXT
            )""")
            self.db.commit()
            if stdout:
                print(f'[+] Table "stages" init...')
        if settings:
            self.sql.execute(f"""CREATE TABLE IF NOT EXISTS settings(
            setting TEXT PRIMARY KEY,
            status TEXT
            )""")
            self.db.commit()
            if stdout:
                print(f'[+] Table "settings" init...')
        if staff:
            self.sql.execute(f"""CREATE TABLE IF NOT EXISTS staff(
            user_id TEXT PRIMARY KEY,
            status TEXT
            )""")
            self.db.commit()
            if stdout:
                print(f'[+] Table "staff" init...')
        if balance:
            self.sql.execute(f"""CREATE TABLE IF NOT EXISTS balance(
            user_id TEXT PRIMARY KEY,
            balance TEXT
            )""")
            self.db.commit()
            if stdout:
                print(f'[+] Table "balance" init...')
        if sub:
            self.sql.execute(f"""CREATE TABLE IF NOT EXISTS subs(
            user_id TEXT PRIMARY KEY,
            last_update TEXT,
            reg_time TEXT
            )""")
            self.db.commit()
            if stdout:
                print(f'[+] Table "balance" init...')

    def stages(self, user_id, stage=None):
        self.sql.execute(f"SELECT * FROM stages WHERE user_id = '{str(user_id)}'")
        if self.sql.fetchone() is None:
            if stage != None:
                self.sql.execute(f"INSERT INTO stages VALUES('{str(user_id)}', '{stage}')")
                self.db.commit()
                return stage
            else:
                return "None"

        else:
            if stage != None:
                self.sql.execute(f"UPDATE stages SET stage = '{str(stage)}' WHERE user_id = '{str(user_id)}'")
                self.db.commit()
            self.sql.execute(f"SELECT * FROM stages WHERE user_id = '{str(user_id)}'")
            for i in self.sql.fetchall():
                return i[1]

    def settings(self, setting, new=None):
        self.sql.execute(f"SELECT * FROM settings WHERE setting = '{str(setting)}'")
        if self.sql.fetchone() is None:
            if new != None:
                self.sql.execute(f"INSERT INTO settings VALUES('{str(setting)}', '{new}')")
                self.db.commit()
                return new
            else:
                return "None"

        else:
            if new != None:
                self.sql.execute(f"UPDATE settings SET status = '{str(new)}' WHERE setting = '{str(setting)}'")
                self.db.commit()
            self.sql.execute(f"SELECT * FROM settings WHERE setting = '{str(setting)}'")
            for i in self.sql.fetchall():
                return i[1]

    def staff(self, user_id, status=None, remove=False):
        if status == None:
            if remove == False:
                s = None
                self.sql.execute(f"SELECT * FROM staff WHERE user_id = '{str(user_id)}'")
                if self.sql.fetchone() is None:
                    pass
                else:
                    self.sql.execute(f"SELECT * FROM staff WHERE user_id = '{str(user_id)}'")
                    for i in self.sql.fetchall():
                        s = i[1]
                return s
            elif remove == True:
                self.sql.execute(f"SELECT * FROM staff WHERE user_id = '{str(user_id)}'")
                if self.sql.fetchone() is None:
                    pass
                else:
                    self.sql.execute(f"DELETE FROM staff WHERE user_id = '{str(user_id)}'")
                    self.db.commit()
        elif status != None:
            self.sql.execute(f"SELECT * FROM staff WHERE user_id = '{str(user_id)}'")
            if self.sql.fetchone() is None:
                self.sql.execute(f"INSERT INTO staff VALUES('{str(user_id)}','{str(status)}')")
                self.db.commit()
            else:
                self.sql.execute(f"UPDATE staff SET status = '{str(status)}' WHERE user_id = '{str(user_id)}'")
                self.db.commit()

    def balance(self, user_id, new_balance=None):
        self.sql.execute(f"SELECT * FROM balance WHERE user_id = '{str(user_id)}'")
        if self.sql.fetchone() is None:
            if new_balance != None:
                self.sql.execute(f"INSERT INTO balance VALUES('{str(user_id)}', '{str(new_balance)}')")
                self.db.commit()
                return int(new_balance)
            else:
                return 0
        else:
            if new_balance != None:
                self.sql.execute(f"UPDATE balance SET balance = '{str(new_balance)}' WHERE user_id = '{str(user_id)}')")
                self.db.commit()
            self.sql.execute(f"SELECT * FROM balance WHERE user_id = '{str(user_id)}'")
            for i in self.sql.fetchall():
                return int(i[1])

    def sub_update(self, user_id):
        import datetime

        self.sql.execute(f"SELECT * FROM subs WHERE user_id = '{str(user_id)}'")
        if self.sql.fetchone() is None:
            self.sql.execute(f"INSERT INTO subs VALUES('{str(user_id)}', '{str(datetime.datetime.now())}', '{str(datetime.datetime.now())}')")
            self.db.commit()
        else:
            self.sql.execute(f"UPDATE subs SET last_update = '{str(datetime.datetime.now())}' WHERE user_id = '{str(user_id)}'")
            self.db.commit()

    def sub_view(self, user_id):
        import datetime

        self.reg_time = None
        self.last = None
        self.sql.execute(f"SELECT * FROM subs WHERE user_id = '{str(user_id)}'")
        if self.sql.fetchone() is None:
            pass
        else:
            self.sql.execute(f"SELECT * FROM subs WHERE user_id = '{str(user_id)}'")
            for i in self.sql.fetchall():
                self.reg_time = Tools.str2date(i[2])
                self.last = Tools.str2date(i[1])

        return {
            "user_id": int(user_id),
            "last_update": self.last,
            "reg_time": self.reg_time
        }

    def drop_table(self, table, stdout=False):
        try:
            self.sql.execute(f"DROP TABLE {str(table)}")
            self.db.commit()
            if stdout:
                print(f'[+] Table "{str(table)}" dropped')
        except:
            if stdout:
                print(f'[-] Error with table "{str(table)}" drop')

    class Connector:
        def __init__(self, host, port, user, password, database):
            self.host = host
            self.port = port
            self.user = user
            self.password = password
            self.database = database
            self.db = None
            self.sql = None

        def connect(self):
            import psycopg2
            self.db = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.sql = self.db.cursor()

        def disconnect(self):
            if self.db is not None:
                self.db.close()

        def __enter__(self):
            self.connect()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is not None:
                print(f"Exception: {exc_val}")
            self.disconnect()

    class CRM(Connector):
        def createCRM(self):
            with self:
                self.sql.execute("""CREATE TABLE IF NOT EXISTS crm (
                user_id SERIAL PRIMARY KEY, 
                first_name TEXT, 
                last_name TEXT,
                id_number TEXT,
                phone_number TEXT,
                country TEXT,
                city TEXT,
                address TEXT,            
                email VARCHAR(255)
                )""")
                self.db.commit()

        def add_lead(self, **kwargs):
            with self:
                columns = ', '.join(kwargs.keys())
                placeholders = ', '.join(['%s'] * len(kwargs))
                values = tuple(kwargs.values())
                query = f"INSERT INTO crm ({columns}) VALUES ({placeholders})"
                self.sql.execute(query, values)
                self.db.commit()

        def remove_lead(self, **kwargs):
            with self:
                columns = ' OR '.join([f"{column} = %s" for column in kwargs.keys()])
                values = tuple(kwargs.values())
                query = f"DELETE FROM crm WHERE {columns}"
                self.sql.execute(query, values)
                self.db.commit()

        def get_lead(self, **kwargs):
            with self:
                columns = ' OR '.join([f"{column} = %s" for column in kwargs.keys()])
                values = tuple(kwargs.values())
                query = f"SELECT * FROM crm WHERE {columns}"
                self.sql.execute(query, values)
                result = self.sql.fetchall()
                return [{
                    'user_id': i[0],
                    'first_name': i[1],
                    'last_name': i[2],
                    'id_number': i[3],
                    'phone_number': i[4],
                    'country': i[5],
                    'city': i[6],
                    'address': i[7],
                    'email': i[8]
                } for i in result]

        def update_lead_contact(self, user_id, **kwargs):
            with self:
                columns = ', '.join([f"{column} = %s" for column in kwargs.keys()])
                values = tuple(kwargs.values()) + (user_id,)
                query = f"UPDATE crm SET {columns} WHERE user_id = %s"
                self.sql.execute(query, values)
                self.db.commit()

        def __enter__(self):
            super().__enter__()
            return self


class distance:
    def __init__(self, lat1, lon1, lat2, lon2):
        self.lat1 = lat1
        self.lon1 = lon1
        self.lat2 = lat2
        self.lon2 = lon2

    def get_distance(self):
        from geopy.distance import great_circle

        locationA = (self.lat1, self.lon1)
        locationB = (self.lat2, self.lon2)
        return round(great_circle.geodesic(locationA, locationB).km, 3)


class tgBot:

    def __init__(self, token):
        import telebot
        self.token = token
        self.bot = telebot.TeleBot(self.token)

    def send(self, chat_id, msg, reply_markup=None, disable_notification=False):
        self.bot.send_message(chat_id, msg, reply_markup=reply_markup, disable_notification=disable_notification,
                         parse_mode='HTML')

    def kmarkup(self):
        from telebot import types

        return types.InlineKeyboardMarkup()

    def back(self, callback_data, bname="Back"):
        from telebot import types

        return types.InlineKeyboardButton(bname, callback_data=callback_data)

    def btn(self, button_id, callback_data=None, url=None):
        from telebot import types

        return types.InlineKeyboardButton(button_id, callback_data=callback_data, url=url)


class arduino:

    def __init__(self, board):
        from pyfirmata import Arduino, util
        self.board = Arduino(board)
        it = util.Iterator(board)
        it.start()

    def digital_port(self, port, status=None):
        if status == None:
            return self.board.digital[port].read()
        elif status in ['True', True, "on", 1]:
            return self.board.digital[port].write(1)
        else:
            return self.board.digital[port].write(0)

    def analog_port(self, port, status=None, enable_reporting=False):
        if enable_reporting:
            self.board.analog[port].enable_reporting()
        if status == None:
            return self.board.analog[port].read()
        elif status != None:
            return self.board.analog[port].write(status)


class barcode:
    def __init__(self, frame):
        from PIL import Image
        self.frame = frame
        self.source_img = Image.open(frame)

    def scan(self):
        from pyzbar.pyzbar import decode
        self.decoded = decode(self.source_img)
        return self.decoded[0].data.decode('utf-8')


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


class Pickle:
    def __init__(self, filename):
        self.filename = filename

    def pick(self, data):
        import pickle as old_pickle
        with open(self.filename, 'wb') as f:
            old_pickle.dump(data, f)

    def unpick(self):
        import pickle as old_pickle
        with open(self.filename, 'rb') as f:
            return old_pickle.load(f)

    def remove(self):
        import os

        os.remove(self.filename)


class Convertors:
    """
    Класс для работы с конвертерами различных форматов файлов
    """

    def __init__(self, input_file):
        self.input_file = input_file

    def webp2png(self, output_file: str):
        """
        Функция для конвертации из формата .webp в формат .png
        :param output_file: str
        :return:
        """
        from PIL import Image

        # Открываем исходный файл в формате .webp
        with Image.open(self.input_file) as im:
            # Сохраняем изображение в формате .png
            im.save(output_file, 'PNG')

    def webp2jpeg(self, output_file: str):
        """
        Функция для конвертации из формата .webp в формат .jpeg

        :param output_file:
        :return:
        """
        from PIL import Image

        with Image.open(self.input_file) as im:
            # Конвертируем изображение в формат JPEG
            im.convert('RGB').save(output_file, 'JPEG')

    def png2jpeg(self, output_file: str):
        """
                Функция для конвертации из формата .png в формат .jpeg

                :param output_file:
                :return:
                """
        from PIL import Image

        with Image.open(self.input_file) as im:
            # Конвертируем изображение в формат JPEG
            im.convert('RGB').save(output_file, 'JPEG')

    def jpeg2png(self, output_file: str):
        """
               Функция для конвертации из формата .jpeg в формат .png
               :param output_file: str
               :return:
               """
        from PIL import Image

        # Открываем исходный файл в формате .webp
        with Image.open(self.input_file) as im:
            # Сохраняем изображение в формате .png
            im.save(output_file, 'PNG')

    def png2ico(self, output_file: str):
        """
       Функция для конвертации из формата .png в формат .ico
       :param output_file: str
       :return:
       """
        from PIL import Image

        # Открываем изображение в формате PNG
        with Image.open(self.input_file) as im:
            # Конвертируем изображение в формат ICO
            im.save(output_file, format='ICO')

    def jpeg2ico(self, output_file: str):
        """
               Функция для конвертации из формата .jpeg в формат .ico
               :param output_file: str
               :return:
               """
        from PIL import Image

        # Открываем изображение в формате PNG
        with Image.open(self.input_file) as im:
            # Конвертируем изображение в формат ICO
            im.save(output_file, format='ICO')


class Automation:
    class NoIp:
        def __init__(self):
            import random

            self.session_id = random.randint(1, 100000)
            self.driver = None

        def open_browser(self):
            from selenium import webdriver

            self.driver = webdriver.Chrome()

        def update(self, username: str, password: str, threaded=False, looped=False, days_delay=0):
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.common.action_chains import ActionChains
            from selenium.webdriver.common.keys import Keys
            import time, threading, os, datetime

            def action():
                self.open_browser()

                self.driver.get("https://no-ip.com/")
                self.driver.implicitly_wait(10)

                self.driver.find_element(By.CSS_SELECTOR, "#topnav > li:nth-child(1)").click()
                self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys(username)
                self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
                self.driver.find_element(By.CSS_SELECTOR, "#clogs-captcha-button").click()

                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, ".border-noip-logo-dark-grey.border-0 > strong > a"))
                )
                time.sleep(2)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ESCAPE).perform()

                self.driver.find_element(
                    By.CSS_SELECTOR,
                    "div.grid-row.mb-30 > div:nth-child(1) > div"
                ).click()

                input("Нажмите Enter для продолжения")

            def action_loop():
                result = False

                update = Pickle("noip_update.sbdt")
                if "noip_update.sbdt" not in os.listdir():
                    update.pick(datetime.datetime.now() - datetime.timedelta(days=days_delay + 1))

                while True:
                    if update.unpick() + datetime.timedelta(days=days_delay) < datetime.datetime.now():
                        update.pick(datetime.datetime.now())
                        action()
                        result = True
                    if not looped:
                        break

                    time.sleep(60 * 60 * 12)

                return result

            if threaded:
                #
                threading.Thread(target=action_loop, daemon=True).start()

            else:
                return action_loop()

    class Requests:
        def __init__(self):
            pass

        def post(self, url: str, data: dict):
            import requests

            return requests.post(url, data=data)

    class CRM:
        def __init__(self):
            pass


class Termux:
    def __init__(self):
        pass

    @staticmethod
    def execute(command: str) -> str:
        import subprocess

        return subprocess.check_output(command, shell=True)

    @staticmethod
    def buttery_check():
        result = Termux.execute("termux-buttery-status")
        result = str(result)
        result = result.split('"percentage": ')[1]
        result = result.split(',')[0]
        return int(result)


class Tools:
    @staticmethod
    def str2date(date_str):
        import datetime

        return datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')


