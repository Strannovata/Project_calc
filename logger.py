# # это из примера с лекции
# В нашем случае нужны аргументы: дататайм, 
# первое и второе число, результат



# from datetime import datetime as dt
import model_sum as model
# from time import time

def sum_logger(data):
#    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};temperature;{}\n'
                    .format(time, data))

# def pressure_logger(data):
#     time = dt.now().strftime('%H:%M')
#     with open('log.csv', 'a') as file:
#         file.write('{};pressure;{}\n'
#                     .format(time, data))


# def wind_speed_logger(data):
#     time = dt.now().strftime('%H:%M')
#     with open('log.csv', 'a') as file:
#         file.write('{};wind_speed;{}\n'
#                     .format(time, data))
