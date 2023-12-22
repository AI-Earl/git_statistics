import datetime
import pytz


class TimeManager:
    def __init__(self):
        self.datetime_now = datetime.datetime.now()

    def get_now_str(self):
        return self.datetime_now.strftime("%Y/%m/%d %T")


class TimeManagerUTC8(TimeManager):
    def __init__(self):
        super().__init__()
        self.datetime_now = self.datetime_now.astimezone(pytz.timezone('Asia/Taipei'))
