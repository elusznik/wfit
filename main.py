import csv
import statistics
import matplotlib.pyplot as plt

if __name__ == '__main__':
    with open("accelerometer.csv") as accelerometer_file:
        accelerometer = csv.DictReader(accelerometer_file, delimiter=',')
        rows = []
        n = 0
        ns = []
        for row in accelerometer:
            ns.append(n)
            rows.append(float(row["Acceleration z (m/s^2)"]))
            print(f"n: {n} {rows[n]} m/s^2")
            n += 1
        plt.plot(ns, rows)
        # print(f"Średnie przyspieszenie to {s/n} m/s\N{SUPERSCRIPT TWO}")
        print(f"Średnia wartość przyspieszenia to {statistics.fmean(rows)} m/s^2")
        print(f"Maksymalna wartość przyepieszenia to {max(rows)} m/s^2")
        print(f"Minimalna wartość przyspieszenia to {min(rows)} m/s^2")
        print(f"Mediana wartości przyspieszenia to {statistics.median(rows)} m/s^2")
        plt.show(block=False)
        plt.savefig("plot.png")
