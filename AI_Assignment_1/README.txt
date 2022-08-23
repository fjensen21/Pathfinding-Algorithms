Finn Jensen (faj21)
Jane McGrath (ljm209)
Andres Uribe (aju24)


---Running the Program---
The program can be run through the command line by calling the main.py file
with 2 arguments (a test file and a specification of which algorithm to run)

For the last parameter specify either "a" or "t". To display the a* path or
the theta* path.

MAKE SURE TO RUN PYTHON3

Ex:
    python3 main.py "test.txt" "a"

---Viewing Vertex Info---
You can view information about a vertex by clicking on it.
The vertex h-val, f-val, and g-val will be displayed in the console
when a node is clicked.

---Termination---

Program is terminated by exiting the visualization.


---Generating Tests---

Tests can be generated using the generatetests.py file and specififying the
number of tests you wish to generate

Ex:
    python3 generatetests.py 5

    ^ This would generate 5 test files in a folder called automated_tests.
    Numbered test0-testn

