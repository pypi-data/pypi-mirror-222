from tools import Tools


class postgreSQL:
    def __init__(self, user="postgres", password="password", database=None, host="localhost"):
        import psycopg2

        self.db = psycopg2.connect(database=database, user=user, password=password, host=host)
        self.sql = self.db.cursor()
        self.init_DB()

    def init_DB(self, stages: bool = False,
                sub: bool = False,
                settings: bool = False,
                staff: bool = False,
                balance: bool = False,
                stdout: bool = True) -> None:
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

    def stages(self, user_id, stage=None) -> str:
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

    def settings(self, setting, new=None) -> str:
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

    def staff(self, user_id, status=None, remove=False) -> str:
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

    def sub_update(self, user_id) -> None:
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
                self.reg_time = Tools().str2date(i[2])
                self.last = Tools.str2date(i[1])

        return {
            "user_id": int(user_id),
            "last_update": self.last,
            "reg_time": self.reg_time
        }

    def drop_table(self, table, stdout=False) -> None:
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

        def connect(self) -> None:
            import psycopg2
            self.db = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.sql = self.db.cursor()

        def disconnect(self) -> None:
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
        def createCRM(self) -> None:
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

        def add_lead(self, **kwargs) -> None:
            with self:
                columns = ', '.join(kwargs.keys())
                placeholders = ', '.join(['%s'] * len(kwargs))
                values = tuple(kwargs.values())
                query = f"INSERT INTO crm ({columns}) VALUES ({placeholders})"
                self.sql.execute(query, values)
                self.db.commit()

        def remove_lead(self, **kwargs) -> None:
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

        def update_lead_contact(self, user_id, **kwargs) -> None:
            with self:
                columns = ', '.join([f"{column} = %s" for column in kwargs.keys()])
                values = tuple(kwargs.values()) + (user_id,)
                query = f"UPDATE crm SET {columns} WHERE user_id = %s"
                self.sql.execute(query, values)
                self.db.commit()

        def __enter__(self):
            super().__enter__()
            return self
