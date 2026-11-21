# Student Performance Analyzer

A Python and NumPy command-line program for entering grades and analyzing student performance. It starts with four sample students and three subjects: Maths, Chemistry, and Physics.

## Features

- Enter or update grades from 0 to 100.
- View each student's average, highest grade, lowest grade, and status.
- Calculate subject averages and the overall class average.
- Rank students with complete grades and show who has the highest and lowest averages.
- Display all grades in a table, using `—` for missing grades.

## How to run

Open a terminal in the project folder and run:

```bash
python -m pip install numpy
python test.py
```

Choose **1** to enter a grade, **8** to view the grade table, or **9** to exit.

## How grades are handled

Missing grades are excluded from averages, while a grade of `0` counts. A student is **Incomplete** until all three grades are entered. After that, an average of **60% or higher** is a **Pass**.

Grades are stored in memory and reset when the program closes.