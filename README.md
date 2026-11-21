# Student Performance Analyzer

This is a small Python project that uses NumPy to work with student grades. It starts with four sample students and three subjects: Maths, Chemistry, and Physics.

You can enter or update grades from 0 to 100 and see each student’s average, highest grade, lowest grade, and pass/fail status. The menu also shows subject averages, the class average, and a ranking of students who have all three grades entered.

## How to run

Open a terminal in the project folder and run:

```bash
python -m pip install numpy
python test.py
```

Choose `1` to enter a grade, `8` to see the full grade table, or `9` to exit.

## How grades work

A dash (`—`) means a grade hasn’t been entered. Missing grades are skipped when calculating averages, and a grade of `0` counts. A student’s status stays `Incomplete` until all three grades are entered. Once they’re entered, an average of 60% or higher is a pass.

The grades reset when you close the program.