import matplotlib.pyplot as plt
import csv
import matplotlib.ticker as ticker
times = []
download = []
ping = []

with open('test.csv', 'r') as csvfile:
     plots = csv.reader(csvfile, delimiter=',')
     next(csvfile)
     for row in plots:
         times.append(str(row[0]))
         download.append(float(row[1]))
         ping.append(float(row[2]))
print(times, "\n", download, "\n", ping)

plt.figure('speedtest', [30, 30])
plt.plot(times, download, label='download', color='r')
plt.plot(times, ping, label='ping', color='b')
plt.xlabel('time')
plt.ylabel('speed in Mb/s')
plt.title("Internet speed")
plt.legend()
plt.savefig('test_graph.jpg', bbox_inches='tight')