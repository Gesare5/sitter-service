import datetime


def create_id_from_timestamp():
    current = datetime.datetime.now().timestamp()
    current = round(current * 1000000)
    return current