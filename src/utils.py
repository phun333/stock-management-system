import datetime


class Utils:
    # A static method is a method that belongs to a class rather than an instance of the class.
    @staticmethod
    def format_date():
        # function to format the current date and time
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")
