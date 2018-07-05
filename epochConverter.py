#Epoch Time Converter

import time

epoch_number = int(input("Enter epoch time number: "))

def print_converted_time(z):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(z))))

if len(str(epoch_number)) > 10:
    proper_timestamp = str(epoch_number)[0:10]
    print_converted_time(proper_timestamp)

else:
    print_converted_time(epoch_number)
