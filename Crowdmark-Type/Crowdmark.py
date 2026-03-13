import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open("Crowdmark.csv", "r") as f:
    Titles = f.readline().strip("\n").split()
    ClassInfo = [studentline.strip().split() for studentline in f]

Dict = {
    "FirstNames":[x[0] for x in ClassInfo],
    "LastNames":[x[1] for x in ClassInfo],
    "Grades":[x[2:] for x in ClassInfo]
    }

Dataframe = pd.DataFrame(Dict)
NumOfAssignments = max(len(x) for x in Dict["Grades"])
GradesMatrix = np.array([x + [np.nan] * (NumOfAssignments - len(x)) for x in Dict["Grades"]])

plt.ylim(0,100)
for studentgrades in GradesMatrix:
    plt.plot([x+1 for x in range(NumOfAssignments)], studentgrades, marker= 'o', color = "grey", alpha = 0.2)

plt.title("Student Grades Chart", family = "arial", fontsize = 20)
plt.ylabel("Precentage")
plt.xlabel("Assignment")
plt.yticks([x * 5 for x in range(21)])
plt.xticks([x+1 for x in range(NumOfAssignments)])
plt.grid()
plt.show()
