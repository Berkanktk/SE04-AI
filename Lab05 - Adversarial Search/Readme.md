# Exercise notes
**1. What is the branching factor at depth 0? At depth 1?**  
Since there are 9 possible moves at depth 0, the answer is 9, and at depth 1, there are 9*9 possible moves.

**2. What is the maximal depth?**  
The maximal depth is 9, since there are 9 possible moves at depth 0.

**3. Will a MIN move attempt to minimize or maximize the utility?**   
The answer is to minimize the utility, since the goal is to maximize the utility.

**4. Are states after a terminal state explored?**  
The answer is yes, since the terminal state is the goal state.

**5. Are all possible states explored to a terminal state?**  
Yes. 

**6. Is this a depth-first or breadth-first search? How do you know?**  
The answer is depth-first search, since the depth is the number of moves.


**7. Run the MinMac tic-tac-toe program (you will play O)**  
The program will run and you will see the following output:
```python
Welcome to the game of Tic-Tac-Toe! Game starts in 3 seconds...
-----
X 1 2
3 4 5
6 7 8
Your move? 4
-----
X X 2
3 O 5
6 7 8
Your move? 2
-----
X X O
3 O 5
X 7 8
Your move? 3
-----
X X O
O O X
X 7 8
Your move? 7
-----
X X O
O O X
X O X
```
Its pretty much impossible to win the game since the AI is starting. So the best result is a draw.

# Homework notes
