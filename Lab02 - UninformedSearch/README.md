# Exercise notes

## Exercise 1
**What is the effect of inserting successor nodes at the end of the fringe as a node is expanded? A depth or breadth-first search?**  
A breadth first search

Solution path:
```python
Solution path:
State: J - Depth: 3
State: G - Depth: 2
State: C - Depth: 1
State: A - Depth: 0
```


## Exercise 2
Solution path:
```python
Solution path:
State: ('B', 'Clean', 'Clean') - Depth: 3
State: ('B', 'Clean', 'Dirty') - Depth: 2
State: ('A', 'Clean', 'Dirty') - Depth: 1
State: ('A', 'Dirty', 'Dirty') - Depth: 0
```

# Homework notes
## Homework 1
**Modify your search-program to solve the following problem:**  
A `farmer` has a `goat`, `a cabbage` and `a wolf` to move across a river with a boat that can only hold himself and one other passenger.  
If the goat and wolf are alone, the wolf will eat the goat.  
If the goat and cabbage are alone, the goat will eat the cabbage.

**Define the state space for the problem.**   
* [x] Hint: Use a tuple to represent the side of the river each is located; for example ('W', 'E', 'W', 'W') can represent the (farmer, wolf, goat, cabbage) locations.

**Use a list of tuples for the successor states.**  
* [x] Include successor states that violate the problem constraints, that is ('W', 'W', 'E', 'E') which is the goat is alone with the cabbage; don't violate requirement that the boat can hold only two passengers (e.g all four passengers cannot move from one side to another at once, that is ('W', 'W', 'W', 'W') cannot become ('E', 'E', 'E', 'E')).

* [x] Define successor_fn to return a list of states that do not violate the problem constraints
