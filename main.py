import csv

# import matplotlib.pyplot as plt

if __name__ == '__main__':
    with open("accelerometer.csv") as accelerometer_file:
        accelerometer = csv.DictReader(accelerometer_file, delimiter=',')
        s = 0.0
        n = 0.0
        for row in accelerometer:
            s += float(row["Acceleration z (m/s^2)"])
            n += 1
        print(s / n)
