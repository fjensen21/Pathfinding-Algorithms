Finn Jensen
Jane McGrath


---Project Overview---

This project is part of an exploration into classical artificial intelligence algorithms. Here we implement the classic A* and Theta* pathfinding algorithms. 
A* is used to find the shortest distance between two nodes along a graph's edges avoiding blocked cells in a grid. 
Theta* is also implemented here which finds the shortest any path distance between 2 nodes in a graph. 

The algorithms, structures and the full contents/code for the project writeup are implemented by me.
The UI was mainly developed by my partner Jane. Credit is commented at the top of each file in the project architecture.

Simple test cases can be found in the tests folder. 50x100 tests can be generated using the generatetests.py file. 

Photo examples of the program can be found in the writeup

--Contents--

    + Project Write Up (projectwriteup.txt)
        - This contains testing and discussion of optimizations made to this code. It also contains discussion of the theoretical differences
        in the two algorithms.
        - This project also includes some discussion of Local and Adversarial Search to show theoretical understanding  of classical search algorithms.
        
 -- Work Implemented by Me --
 
    + astar.py 
        - Implements the A* algorithm
    + generatetests.py
        - Randomly generates test grids for use with either algorithm. (Size is 50 x 100 by default but can be adjusted in the constants.
    + graph.py
        - Represents the grid that algorithms find paths for.
    + readin.py
        - Reads in the grids from txt representation
    + thetastar.py
        - Implements theta* algorithm. Note: LineOfSight function is adapted from pseduocode not created by me.
    + vertex.py
        - Represents a vertex in a grid.

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

