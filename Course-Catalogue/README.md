```md
# Course Grade Tracker (Work in Progress)

This project is a C++ program that allows students to track their courses, define grading breakdowns (syllabus), and calculate their current grades and overall GPA.

The program is built using manual memory management and custom dynamic arrays to store courses and related data.

---

## Status: This project is still in progress and under active development.

The current objective is to fully implement course management, including adding and removing courses, and expanding the system to handle syllabus structures and assignment tracking.

---

## How the Program Works

1. The user inputs their courses  
2. Each course is stored in a dynamically resizing array  
3. The system allows expansion when capacity is reached (custom array resizing)  
4. Each course will later support:
   - Custom grading categories (e.g., Homework, Midterms, Exams)  
   - User-defined weight distribution (must total 100%)  
5. The program will calculate:
   - Category averages  
   - Weighted course grades  
   - Overall GPA across all courses  

---

## Planned Syllabus Format

Each course will allow the user to define grading weights like:

```

Homework: 25%
Midterm: 35%
Final Exam: 40%

```

- The user can create any number of categories  
- Each category contributes a percentage toward the final grade  
- The system will validate that total weight equals 100%  

---

## Assignment System (Planned)

For each category:
- The user can add multiple assignments  
- Each assignment has an associated grade  
- The program calculates the average for that category  

Example:
```

Homework Grades: 80, 90, 85

Average = 85
Contribution = 85 × 0.25 = 21.25%

````

---

## Technologies Used

- C++  
- Manual dynamic memory (`new[]`, `delete[]`)  
- Custom array resizing (no `std::vector`)  
- Deep copying using:
  - Copy constructor  
  - Assignment operator  
  - Destructor  

---

## How to Run

1. Compile the program:
   ```bash
   g++ main.cpp -o tracker
````

2. Run the executable:

   ```bash
   ./tracker
   ```

---

## Planned Features

* Remove courses from the list
* Implement syllabus/category system
* Add assignment storage per category
* Calculate weighted grades per course
* Compute overall GPA
* Display detailed course breakdowns
* Improve terminal interaction and usability

---

## Purpose

This project was created as a learning exercise to practice:

* Low-level memory management in C++
* Understanding object copying (Rule of 3)
* Building dynamic data structures from scratch
* Designing systems that handle structured, real-world data

The project is still under development and will continue to expand in functionality and complexity.

```
```
