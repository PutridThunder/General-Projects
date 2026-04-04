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
StudentLines = []
for studentgrades in GradesMatrix:
    line = plt.plot([x+1 for x in range(NumOfAssignments)], studentgrades, marker= 'o', color = "grey", alpha = 0.2)
    StudentLines.append(line)

plt.title("Student Grades Chart", family = "arial", fontsize = 20)
plt.ylabel("Precentage")
plt.xlabel("Assignment")
plt.yticks([x * 5 for x in range(21)])
plt.xticks([x+1 for x in range(NumOfAssignments)])
plt.grid()
plt.ion()
plt.show()

def GetStudentIndex(name):
    First, Last = name.split(" ")
    mask = (Dataframe["FirstNames"] == First) & (Dataframe["LastNames"] == Last) 
    if mask.any():
        index = np.where(mask)[0][0]
        return index
    else:
        print("Student not found")        
    
def AllToGray():
    for line in StudentLines:
        l = line[0]
        l.set_color('grey')
        l.set_alpha(0.2)
    plt.draw()

def HighlightSelectStudent(index):
    line = StudentLines[index][0]     
    line.set_color('blue')             
    line.set_alpha(1)                  
    plt.draw()                         

def ShowStudentList():
    for first, last in zip(Dataframe["FirstNames"], Dataframe["LastNames"]):
        print(first, last)

while True:
    print("COMMANDS")
    print("S: SELECT SINGLE STUDENT")
    print("C: CLEAR")
    print("L: TERMINAL BASED LIST OF ALL STUDENTS")

    UserInput = input("INPUT: ").upper()

    if UserInput =="S":
        x = input("Select a student(first and last name(e.g. Jane Doe)): ")
        index = GetStudentIndex(x)
        HighlightSelectStudent(index)
    elif UserInput =="C":
        AllToGray()
    elif UserInput =="L":
        ShowStudentList()
