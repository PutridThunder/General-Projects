import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Access The CSV

# Take the titles from the first line
# File Parsing V.1 ###########################################################################

with open("Crowdmark.csv", "r") as f:

    Titles = f.readline().strip("\n").split()

    ClassInfo = []

    for studentline in f.readlines():
        ClassInfo.append(studentline.strip("\n").split())

##############################################################################################


# Dict V.1 ###########################################################################

# Split each lines info to firstname, last name, and an array of grades

# Dict = {
#     "FirstNames":[x[0] for x in ClassInfo],
#     "LastNames":[x[1] for x in ClassInfo],
#     "Grades":[x[2:] for x in ClassInfo]
#     }

# Dict V.2 ###########################################################################

Dict = {
    "FirstNames":[x[0] for x in ClassInfo],
    "LastNames":[x[1] for x in ClassInfo],
    "Grades":[[int(g) for g in x[2:]] for x in ClassInfo]
    }

# Place all the info into a pandas dataframe, each column named from the first line in the csv file
##############################################################################################


#pd.DataFrame V.1 ########################################################################################
"""
First use of AI, I had this:

Dataframe = pd.DataFrame(Dict)

and I attempted to use columns =
to give names to each column based
off of whatever the name was in the csv file:

Dataframe = pd.DataFrame(Dict, columns=[x for x in Titles])

turns out columns= takes from the
dictionary names and organises each
column position, if I wanted column
to hold a custom title i would have
to do:

Dict = {f"Titles[0]"":[x[0] for x in ClassInfo], f"Titles[1]":[x[1] for x in ClassInfo], f"Titles[2]":[x[2:] for x in ClassInfo]}

I don't really need that so I'll keep it as a string
"""

Dataframe = pd.DataFrame(Dict)

# Access the grade array from the pandas dataframe and create a chart for the first student
##############################################################################################


# Grades V.1 ###########################################################################
"""
found through random testing and looking
through possibilities, .get() gives you all
of a single column, you can access each row
by asking for an index
"""
Grades = Dataframe.get("Grades")
# Grades V.2 ###########################################################################
'''
Watched: "Learn NumPy in 1 hour!" by Bro Code on YouTube.

While learning NumPy, I realized
that storing grade data in arrays
makes accessing and manipulating
the data much easier. Converting
the grades into a NumPy matrix
allows efficient calculations for
statistics such as student averages,
assignment averages, class performance,
and identifying top scores.

===============================================================
This is how GradesMatrix was built

For each student's grade array, extend it with np.nan values
so that its length matches the total number of assignments.

Example:
x = [1,2,3]

total assignments = 5
len(x) = 3 → 2 assignments missing

row becomes:
[1,2,3] + [nan, nan] = [1,2,3,nan,nan]

'''
NumOfAssignments = max(len(x) for x in Dict["Grades"])
GradesMatrix = np.array([x + [np.nan] * (NumOfAssignments - len(x)) for x in Dict["Grades"]])

#############################################################################################

plt.ylim(0,100)


# Access multiple grade arrays from the pandas dataframe and chart them all side by side

# Graphing V.1 ###########################################################################

# for i in range(len(Grades)):
#     x = np.array([[x+1 for x in range(len(Grades[i]))]])
#     y = [int(g) for g in Grades[i]]

#     plt.plot(x, y, marker = "o", label=f"{Dataframe.get('FirstNames')[i]}")

# plt.show()

# add the names of each student to a line

'''Second use of AI, wanted to add the names of the students
after successfully printing all the charts onto one graph,
found out to do so all I had to do was add label= into the plotting
and add .legend() with a location '''

# plt.legend(loc="upper left")

# Graphing V.2 ###########################################################################

'''
Watched "Learn NumPy in 1 hour!" by Bro Code on YouTube.

same senario as listed in "Grades V.2", and thanks to those
changes I was able to optimise the graphing loop, also added
a list to store each students line for future graph transformations
'''

for studentgrades in GradesMatrix:
    plt.plot([x+1 for x in range(NumOfAssignments)], studentgrades, marker= 'o', color = "grey", alpha = 0.2)

plt.show()

# add in terminal based search bar to search for specific students
###############################################################################################


#Useful Stats V.1##############################################################################################

# Find Student Averages

Averages = []

for g in Grades:
    totalprecentage = 0
    assignmentcount = 0
    for t in g:
        assignmentcount += 1
        totalprecentage += int(t)

    Averages.append(totalprecentage/assignmentcount)

# print(Dataframe)
print(Averages)

# add student averages to panda library

'''Had to search up how to add a column, .loc does that'''

Dataframe.loc[:, 'Averages'] = Averages

# for i in range(len(Averages)):
#     x = np.array([i for i in range(len(Averages))])
#     y = np.array([Averages[i]])
#     plt.plot(x, y, label=f"{Dataframe.get('FirstNames')[i]}'s Average")

# Current problem, its too messy, I need to find a cleaner way to show information
'''
-   My idea for this is first learn how to update the graph based on what infos given
so if I'm looking for a certain student, I type in their name or index location
and a graph for them shows

-   Then, I want to be able to have all the graphs show, but different opacities
say I want Jane's info, the opacity for everyone else is lower, we only see jane's visibally'''
###############################################################################################


#Useful Stats V.2##############################################################################################
'''Watched "Learn NumPy in 1 hour!" by Bro Code on YouTube.

Same point stated in Grades V.2
'''

StudentAverages = np.nanmean(GradesMatrix, axis=1) # each student's average

AveragePerAssignment =np.nanmean(GradesMatrix, axis=0) # class average on any assignment

ClassAverage = np.nanmean(GradesMatrix) # total class's average

TopStudent = np.argmax(StudentAverages) # find student index by highest average
###############################################################################################

#Chart Design Stats V.1###############################################################################

'''
Had no clean way to display the info,
first step into that is to make the graph easier to read
now I implemented a design for the chart
'''

plt.title("Student Grades Chart", family = "arial", fontsize = 20)
plt.ylabel("Precentage")
plt.xlabel("Assignment")
plt.ylim(0,100)
plt.yticks([x * 5 for x in range(21)])
plt.xticks([x+1 for x in range(NumOfAssignments)])
plt.grid()
plt.show()
