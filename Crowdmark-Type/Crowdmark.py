import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open("Crowdmark.csv", "r") as f:

    Titles = f.readline().strip("\n").split(" ")

    ClassInfo = []

    for studentline in f.readlines():
        ClassInfo.append(studentline.strip("\n").split(" "))

Dict = {"FirstNames":[x[0] for x in ClassInfo], "LastNames":[x[1] for x in ClassInfo], "Grades":[x[2:] for x in ClassInfo]}

Dataframe = pd.DataFrame(Dict)
Grades = Dataframe.get("Grades")

for i in range(len(Grades)):
    x = np.array([x+1 for x in range(len(Grades[i]))])
    y = [int(g) for g in Grades[i]]

    plt.plot(x, y, marker = "o", label=f"{Dataframe.get('FirstNames')[i]}")

plt.legend(loc="upper left")
plt.show()
