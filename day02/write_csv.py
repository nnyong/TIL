lunch={
    '돈까스':'054-454-2343',
    '떡볶이':'054-451-2222',
    '해물찜':'054-454-9384'
}

import csv

with open('lunch.csv','w',encoding='utf8',newline='') as f:
    csv_writer=csv.writer(f)
    for item in lunch.items(): # list [(key, value), ...]
        csv_writer.writerow(item)
        #f.write(f'{item[0]},{item[1]}\n')