import datetime


class Utils:
    def format_date(date):
        # function to format a date about the current date
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")
