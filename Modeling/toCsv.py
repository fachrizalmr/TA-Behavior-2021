import csv

Waktu = '0:00:00-0:05:00'
Hari = 'senin'
Idrelay = 'relay1'
Status = 'off'

with open('rawData1.csv', 'a', newline='') as csv_file:
    # menentukan label
    fieldnames = ['Waktu', 'Hari', 'Idrelay', 'Status']

    # membuat objek writer
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writerow({'Waktu': Waktu, 'Hari': Hari,
                    'Idrelay': Idrelay, 'Status': Status})

print("Writing Done!")
