import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Access The CSV

# Take the titles from the first line

with open("Crowdmark.csv", "r") as f:

    Titles = f.readline().strip("\n").split(" ")

    ClassInfo = []

    for studentline in f.readlines():
        ClassInfo.append(studentline.strip("\n").split(" "))


# Split each lines info to firstname, last name, and an array of grades
Dict = {"FirstNames":[x[0] for x in ClassInfo], "LastNames":[x[1] for x in ClassInfo], "Grades":[x[2:] for x in ClassInfo]}

# Place all the info into a pandas dataframe, each column named from the first line in the csv file

"""
First use of AI, I had this:

Dataframe = pd.DataFrame(Dict)

and I attempted to use columns= to give names to each column based
off of whatever the name was in the csv file:

Dataframe = pd.DataFrame(Dict, columns=[x for x in Titles])

turns out columns= takes from the dictionary names 
and organises each column position, if I wanted column
to hold a custom title i would have to do:

Dict = {f"Titles[0]"":[x[0] for x in ClassInfo], f"Titles[1]":[x[1] for x in ClassInfo], f"Titles[2]":[x[2:] for x in ClassInfo]}

I don't really need that so I'll keep it as a string
"""

Dataframe = pd.DataFrame(Dict)

# Access the grade array from the pandas dataframe and create a chart for the first student
"""
found through random testing and looking through possibilities,
.get() gives you all of a single column, you can access each row by asking for an index

"""
Grades = Dataframe.get("Grades")

y = [int(g) for g in Grades[0]]

x = np.array([x+1 for x in range(len(Grades[0]))])

plt.plot(x, y, marker ="o")

plt.ylim(0,100)

plt.show()

# Access multiple grade arrays from the pandas dataframe and chart them all side by side


# add the names of each student to a line
