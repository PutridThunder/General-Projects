```markdown
# Crowdmark CSV Data Visualizer (Work in Progress)

This project reads student grade data from a CSV file and visualizes assignment scores using Python, Pandas, NumPy, and Matplotlib.

The program loads student names and grades from a CSV file, stores them in a Pandas DataFrame, and generates a line graph of assignment results.

Status: This project is still in progress and under active development.

---

## CSV File Format

The CSV file (`Crowdmark.csv`) must follow this structure:

```

FirstName LastName Assignments

John Doe 67 100 80 96 84

Jane Doe 71 40 30 24 13

(continue list of student names and grades)

````

- The first row contains column titles  
- Each following row represents one student  
- Grades must be integers  

---

## How the Program Works

1. Reads the first line of the CSV file to extract column titles  
2. Reads each student’s data and separates:
   - First name  
   - Last name  
   - A list of grades  
3. Stores the data in a dictionary and converts it into a Pandas DataFrame  
4. Extracts grade data from the DataFrame  
5. Uses Matplotlib to plot assignment grades for a student  

Currently, the program plots grades for the first student only.

---

## Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  

---

## How to Run

1. Install dependencies:
   ```bash
   pip install pandas
   pip install numpy
   pip install matplotlib
````

2. Place `Crowdmark.csv` in the same directory as the Python script.

3. Run the script:

   ```bash
   python Crowdmark.py
   ```

---

## Planned Features

* Plot multiple students on the same graph
* Add student names as labels and legends
* Improve CSV parsing using Pandas directly
* Add class statistics (average, median, etc.)
* Improve code structure and readability

---

## Purpose

This project was created as a learning exercise to practice:

* File handling in Python
* Working with Pandas DataFrames
* Data visualization with Matplotlib
* Processing real-world style datasets

The project is still under development and will continue to expand in functionality.

```
```
