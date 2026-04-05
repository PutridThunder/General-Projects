import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open("Crowdmark.csv", "r") as f:
    Titles = f.readline().strip("\n").split()
    ClassInfo = [studentline.strip().split() for studentline in f]

Dict = {
    "FirstNames":[x[0] for x in ClassInfo],
    "LastNames":[x[1] for x in ClassInfo],
    "Grades":[[int(g) for g in x[2:]] for x in ClassInfo]
    }

Dataframe = pd.DataFrame(Dict)
NumOfAssignments = max(len(x) for x in Dict["Grades"])

FullNames = Dataframe["FirstNames"] + " " + Dataframe["LastNames"]

GradesMatrix = np.array([x + [np.nan] * (NumOfAssignments - len(x)) for x in Dict["Grades"]])
StudentAverages = np.nanmean(GradesMatrix, axis=1)
AveragePerAssignment =np.nanmean(GradesMatrix, axis=0)

ClassAverage = np.nanmean(GradesMatrix)

TopStudent = np.argmax(StudentAverages)
LowStudent = np.argmin(StudentAverages)

SortedIndices = np.argsort(-StudentAverages)
Ranks = np.empty_like(SortedIndices)
Ranks[SortedIndices] = np.arange(1, len(StudentAverages)+1)

fig, ax = plt.subplots()
StudentLines = []

for studentgrades in GradesMatrix:
    line, = ax.plot([x+1 for x in range(NumOfAssignments)], studentgrades, marker= 'o', color = "grey", alpha = 0.2)
    StudentLines.append(line)

ax.set_title("Student Grades Chart", family="arial", fontsize = 20)
ax.set_ylabel("Precentage")
ax.set_xlabel("Assignment")
ax.set_ylim(0,100)
ax.set_yticks([x * 5 for x in range(21)])

ax.grid()
plt.ion()
plt.show()

CurrentHighlight = None
ClassAverageLine = None

info_fig, (pie_ax, text_ax) = plt.subplots(2, 1, figsize=(5,6))
info_fig.suptitle("Student Info", fontsize=16)

def GetStudentIndex(name):
    parts = name.split(" ")
    if len(parts) != 2:
        print("Enter first and last name")
        return None
    First, Last = parts

    mask = (Dataframe["FirstNames"] == First) & (Dataframe["LastNames"] == Last)
    if mask.any():
        index = np.where(mask)[0][0]
        return index
    else:
        print("Student not found")        
    
def AllToGray():
    global CurrentHighlight
    for line in StudentLines:
        line.set_color('grey')
        line.set_alpha(0.2)
    CurrentHighlight = None
    fig.canvas.draw_idle()

def HighlightSelectStudent(index):
    global CurrentHighlight
    if CurrentHighlight is not None:
        previous = StudentLines[CurrentHighlight]
        previous.set_color('grey')
        previous.set_alpha(0.2)

    line = StudentLines[index]
    line.set_color('blue')
    line.set_alpha(1)
    CurrentHighlight = index
    fig.canvas.draw_idle()

def GetLetterGrade(avg):
    if avg >= 90: return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    else: return "F"

def UpdateStudentInfo(index):
    pie_ax.clear()
    text_ax.clear()
    grades = GradesMatrix[index]
    name = FullNames[index]
    avg = StudentAverages[index]
    letter = GetLetterGrade(avg)
    rank = Ranks[index]

    valid_grades = grades[~np.isnan(grades)]

    if len(valid_grades) == 0:
        pie_ax.text(0.5, 0.5, "No grades", ha='center')
        pie_ax.set_title(name)
    else:
        labels = [f"A{i+1}" for i in range(len(valid_grades))]
        pie_ax.pie(valid_grades, labels=labels, autopct='%1.1f%%')

        pie_ax.set_title(name)

    text_ax.axis('off')
    text_ax.text(0.5, 0.7, f"Average: {avg:.2f}% ({letter})", ha='center', fontsize=12)
    text_ax.text(0.5, 0.4, f"Rank: {rank}/{len(StudentAverages)}", ha='center', fontsize=12)

    if np.all(np.isnan(grades)):
        best = worst = None
    else:
        best = np.nanargmax(grades)
        worst = np.nanargmin(grades)

    if best is not None:
        text_ax.text(0.5, 0.1,f"Best: A{best+1} ({grades[best]:.2f}%) | Worst: A{worst+1} ({grades[worst]:.2f}%)",ha='center', fontsize=10)

    info_fig.canvas.draw_idle()

def DisplayAverage():
    pie_ax.clear()
    text_ax.clear()

    name = "Class Average"
    letter = GetLetterGrade(ClassAverage)

    valid = AveragePerAssignment[~np.isnan(AveragePerAssignment)]

    if len(valid) == 0:
        pie_ax.text(0.5, 0.5, "No data", ha='center')
        pie_ax.set_title(name)
    else:
        labels = [f"A{i+1}" for i in range(len(valid))]
        pie_ax.pie(valid, labels=labels, autopct='%1.1f%%')
        pie_ax.set_title(name)

    text_ax.axis('off')
    text_ax.text(0.5, 0.7, f"Average: {ClassAverage:.2f}% ({letter})", ha='center', fontsize=12)

    if len(valid) > 0:
        best = np.nanargmax(AveragePerAssignment)
        worst = np.nanargmin(AveragePerAssignment)

        text_ax.text(
            0.5, 0.4,
            f"Assignments: {len(valid)}",
            ha='center', fontsize=12
        )

        text_ax.text(
            0.5, 0.1,
            f"Best: A{best+1} ({AveragePerAssignment[best]:.2f}%) | "
            f"Worst: A{worst+1} ({AveragePerAssignment[worst]:.2f}%)",
            ha='center', fontsize=10
        )

    info_fig.canvas.draw_idle()

def ShowClassData():
    global ClassAverageLine

    if ClassAverageLine is None:
        ClassAverageLine, = ax.plot(
            range(1, NumOfAssignments+1),
            AveragePerAssignment,
            marker='o',
            color='green',
            linewidth = 3,
            label="Class Average"
        )
        ax.legend()
    else:
        ClassAverageLine.remove()
        ClassAverageLine = None

        legend = ax.get_legend()
        if legend:
            legend.remove()

    fig.canvas.draw_idle()

    lowest = np.nanargmin(AveragePerAssignment)
    highest = np.nanargmax(AveragePerAssignment)

    print(f"\nClass Average: {ClassAverage:.2f}% ({GetLetterGrade(ClassAverage)})")
    print(f"Lowest Assignment: #{lowest+1} ({AveragePerAssignment[lowest]:.2f}%)")
    print(f"Highest Assignment: #{highest+1} ({AveragePerAssignment[highest]:.2f}%)")

def ShowStudentList():
    print("\n===================================\n")
    for i, name in enumerate(FullNames):
        print(f"{i+1}. {name}")
    print("\n===================================\n")

def HighlightAboveThreshold(threshold):
    global CurrentHighlight

    try:
        threshold = float(threshold)
    except:
        print("Enter a valid number")
        return

    AllToGray()

    mask = StudentAverages >= threshold

    if not mask.any():
        print("No students meet the threshold")
        return

    indices = np.where(mask)[0]

    for i in indices:
        line = StudentLines[i]
        line.set_color('blue')
        line.set_alpha(1)
        line.set_linewidth(2)

    print(f"{len(indices)} students ≥ {threshold}%")
    for i in indices:
        print(f"{FullNames[i]} | {StudentAverages[i]:.2f}%")

    fig.canvas.draw_idle()

while True:
    print("\n===================================\n")
    print("COMMANDS")
    print("S: SELECT STUDENT")
    print("C: CLEAR")
    print("L: LIST STUDENTS")
    print("D: CLASS DATA")
    print("T: HIGHLIGHT ABOVE THRESHOLD")
    print("Q: QUIT")
    print("\n===================================\n")

    UserInput = input("INPUT: ").upper()

    if UserInput == "S":
        while True:
            name = input("Enter name/ Enter Q to exit section: ")
            if name.upper() == "Q":
                break

            index = GetStudentIndex(name)
            if index is not None:
                HighlightSelectStudent(index)
                UpdateStudentInfo(index)
                avg = StudentAverages[index]
                print(f"{FullNames[index]} | {avg:.2f}% ({GetLetterGrade(avg)}) | Rank {Ranks[index]}")

    elif UserInput == "C":
        AllToGray()

    elif UserInput == "L":
        ShowStudentList()
        avg = StudentAverages[TopStudent]
        print(f"Top Student: {FullNames[TopStudent]} | {avg:.2f}% ({GetLetterGrade(avg)}) | Rank {Ranks[TopStudent]}")

        avg = StudentAverages[LowStudent]
        print(f"Lowest Student: {FullNames[LowStudent]} | {avg:.2f}% ({GetLetterGrade(avg)}) | Rank {Ranks[LowStudent]}")
        
        DisplayAverage()

    elif UserInput == "D":
        ShowClassData()

    elif UserInput == "T":
        while True:
            thresh = input("Enter percentage threshold/ Enter Q to exit section: ").strip()

            if thresh.upper() == "Q":
                break

            HighlightAboveThreshold(thresh)
    elif UserInput == "Q":
        break
