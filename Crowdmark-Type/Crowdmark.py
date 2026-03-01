import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open("StudentInfo.csv", "r") as f:

    Titles = f.readline().strip("\n").split(" ")

    ClassInfo = []

    for studentline in f.readlines():
        ClassInfo.append(studentline.strip("\n").split(" "))

Dict = {"FirstNames":[x[0] for x in ClassInfo], "LastNames":[x[1] for x in ClassInfo], "Grades":[x[2:] for x in ClassInfo]}

Dataframe = pd.DataFrame(Dict)
Grades = Dataframe.get("Grades")

y = [int(g) for g in Grades[0]]
x = np.array([x+1 for x in range(len(Grades[0]))])

plt.plot(x, y, marker ="o")
plt.ylim(0,100)
plt.show()
