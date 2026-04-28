# Task 3: program to plot benchmarking data

import numpy as np
import pandas as pd
import seaborn as sb


def plot(data):
    data.plot(x="size", ylabel="Time (sec)", loglog=False)


def log_plot(data):
    data.plot(x="size", ylabel="Time (sec)", loglog=True)


def log_fit(data, column):
    x = np.log10(data["size"])
    y = np.log10(data[column])
    slope, _ = np.polyfit(x, y, deg=1)
    print(f"Log-log best fit for {column}: slope={slope:.3f}")


def linear_regression(data, column):
    sb.regplot(data, x="size", y=column, order=1)


def quadratic_regression(data, column):
    sb.regplot(data, x="size", y=column, order=2)


if __name__ == "__main__":
    data = pd.read_csv("bubblesort.csv")
    # call functions here
    log_fit(data, "Python")
    log_fit(data, "C")
