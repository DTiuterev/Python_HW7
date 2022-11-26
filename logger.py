from datetime import datetime as dt

def log_info(data):
    time = dt.now().strftime('%D %H:%M')
    with open('log.txt', 'a') as file:
        file.write(f'{time} info: {data}\n')

def log_error(data):
    time = dt.now().strftime('%D %H:%M')
    with open('log.txt', 'a') as file:
        file.write(f'{time} error: {data}\n')