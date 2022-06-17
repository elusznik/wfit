import csv

import matplotlib.pyplot as plt

if __name__ == '__main__':
    with open("accelerometer.csv") as accelerometer_file:
        accelerometer = csv.DictReader(accelerometer_file, delimiter=',')
        s = 0.0
        rows = []
        n = 0
        ns = []
        for row in accelerometer:
            s += float(row["Acceleration z (m/s^2)"])
            ns.append(n)
            rows.append(float(row["Acceleration z (m/s^2)"]))
            print(f"n: {n} {rows[n]} m/s^2")
            n += 1
        plt.plot(ns, rows)
        # print(f"Średnie przyspieszenie to {s/n} m/s\N{SUPERSCRIPT TWO}")
        print(f"Średnie przyspieszenie to {s / n} m/s^2")
        plt.show(block=False)
        plt.savefig("plot.png")
