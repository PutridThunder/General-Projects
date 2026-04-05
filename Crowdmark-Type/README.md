# Crowdmark CSV Data Visualizer

## Overview
This Python project reads student grade data from a CSV file and provides interactive visualizations and analysis. The program shows individual student grades, class averages, and assignment breakdowns using dynamic plots.

Key features:  
- Visualizes all students’ assignment grades with line plots.  
- Highlights individual students or groups above a grade threshold.  
- Displays student and class statistics including averages, ranks, and letter grades.  
- Pie charts show per-student assignment distributions.  

> **Note:** I am currently moving all project documentation into a Jupyter Notebook for cleaner visuals and better step-by-step explanations.

---

## CSV File Format
The CSV file (`Crowdmark.csv`) should follow this structure:

```
FirstName LastName Assignment1 Assignment2 Assignment3 ...
John Doe 85 90 78
Jane Smith 92 88 95
```

- The first row can contain column titles.  
- Each subsequent row represents a student.  
- Grades must be integers; missing grades can be left blank.  

---

## Features
- Calculates per-student averages and ranks.  
- Computes class average and per-assignment averages.  
- Highlights top/bottom performers.  
- Interactive console commands:  
  - **S**: Select a student to display detailed stats and pie chart.  
  - **C**: Clear highlighted students.  
  - **L**: List all students with top and lowest performers.  
  - **D**: Show class average and best/worst assignments.  
  - **T**: Highlight students above a specified grade threshold.  
  - **Q**: Quit program.  

---

## Skills Showcased
- **Python Programming:** Loops, functions, dictionaries, and arrays.  
- **Data Handling:** Using `pandas` and `NumPy` to process datasets and handle missing values.  
- **Data Visualization:** Dynamic line plots and pie charts with `matplotlib`.  
- **Interactive CLI:** User-friendly commands for selecting and filtering students.  
- **Problem Solving:** Organizing data, calculating averages/ranks, handling incomplete datasets.  

---

## Installation & Usage
1. Install dependencies:
```bash
pip install pandas numpy matplotlib
```

2. Place `Crowdmark.csv` in the same folder as the script.  

3. Run the script:
```bash
python StudentGradesVisualization.py
```

4. Use the command-line interface to navigate and analyze student grades.

---

## Project Status
✅ The project is complete and fully functional.  

⚠️ Ongoing improvements:  
- Full documentation is being transferred into a Jupyter Notebook.  
- Enhancements to student search and visualization clarity are planned.  

---

## Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  

---

## Purpose
This project demonstrates practical skills in:  
- File handling and CSV processing in Python.  
- Organizing and analyzing tabular data with `pandas`.  
- Data visualization for educational datasets.  
- Building interactive CLI tools for data exploration.  
