import csv

# import matplotlib.pyplot as plt

if __name__ == '__main__':
    with open("accelerometer.csv") as accelerometer_file:
        accelerometer = csv.DictReader(accelerometer_file, delimiter=',')
        for row in accelerometer:
            print(float(row["Acceleration z (m/s^2)"]))