import datetime
import speedtest
import csv

s  = speedtest.Speedtest()
print('Connected to: ' + s.get_best_server().get('sponsor'))
print('Ping: ' + str(s.get_best_server().get('latency')))

with open('test.csv', mode='w', newline='') as speedcsv:
    csv_writer = csv.DictWriter(speedcsv,
                                fieldnames=['time', 'downspeed', 'ping'])
    csv_writer.writeheader()
    while True:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        downspeed = round((round(s.download()) / 1048576), 2)
        ping = s.get_best_server().get('latency')
        print(time)
        print(downspeed)
        print(ping)
        print('-----')
        csv_writer.writerow({
            'time': time,
            'downspeed': downspeed,
            "ping": ping
        })
        speedcsv.flush()