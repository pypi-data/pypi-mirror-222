

class Tools:
    @staticmethod
    def str2date(date_str):
        import datetime

        return datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')


