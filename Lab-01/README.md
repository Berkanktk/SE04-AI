# Exercise notes

## Exercise 1
1. Run the module (using `run()`)
   1. Done
2. Enter: `print(TABLE_DRIVEN_AGENT((B, 'Clean')), ' t', percepts)`
   1. See output below
```python
# Output
Action   Percepts
Suck 	 [('A', 'Clean')]
None 	 [('A', 'Clean'), ('A', 'Dirty')]
None 	 [('A', 'Clean'), ('A', 'Dirty'), ('B', 'Clean')]
```
**Explain the results**  
Each step appends current percept to list of percepts to determine what action to choose next.

**How many table entries would be required if only the current percept was used to select and
action rather than the percept history?**  
2^+2^=2^4

**How many table entries are required for an agent lifetime of T steps?**   
(2^4)^t

## Exercise 2
1. Run the module
   1. Done
2. Enter `run(10)`
   1. Done

**Should bogus actions be able to corrupt the environment? Change the
REFLEX_VACUUM_AGENT to return bogus action, such as Left when it should go Right etc.
Run the agent. Do the Actuators allow bogus actions?**  
Yes

## Exercise 3
1. Run the module
   1. Done
2. Enter `run(10)`
   1. Done

**Change the SIMPLE_REFLEX_AGENT condition action rules to return bogus actions, such as
Left when should go Right , or Crash , etc. Rerun the agent. Do the Actuators allow bogus
actions?**  
Yes

## Exercise 4
Done

# Homework notes

## Homework 1
Extend the REFLEX_VACUUM_AGENT (Exercise 2) program to have 4 locations (4 squares)
- The agent should only sense and act on the square where it is located
- Allow any starting square
- Use run(20) to test and display results
```python
      Current                       New
location    status  action  location    status
A           Dirty   Suck    A           Clean   
A           Clean   Right   B           Dirty   
B           Dirty   Suck    B           Clean   
B           Clean   Up      C           Dirty   
C           Dirty   Suck    C           Clean   
C           Clean   Left    D           Dirty   
D           Dirty   Suck    D           Clean   
D           Clean   Down    A           Clean   
A           Clean   Right   B           Clean   
B           Clean   Up      C           Clean   
C           Clean   Left    D           Clean   
D           Clean   Down    A           Clean   
A           Clean   Right   B           Clean   
B           Clean   Up      C           Clean   
C           Clean   Left    D           Clean   
D           Clean   Down    A           Clean   
A           Clean   Right   B           Clean   
B           Clean   Up      C           Clean   
C           Clean   Left    D           Clean
```

## Homework 2
Extend the REFLEX_AGENT_WITH_STATE program to have 4 locations
- The agent should only sense and act on the square where it is located
- Allow any starting square
- Use run(20) to test and display results
```python
      Current                       New
location	status	action	location	status
A           Dirty   Suck    A           Clean   
A           Clean   Right   B           Dirty   
B           Dirty   Suck    B           Clean   
B           Clean   Up      C           Dirty   
C           Dirty   Suck    C           Clean   
C           Clean   Left    D           Dirty   
D           Dirty   Suck    D           Clean   
D           Clean   Down    A           Clean   
A           Clean   NoOp    A           Clean   
A           Clean   NoOp    A           Clean   
A           Clean   NoOp    A           Clean   
A           Clean   NoOp    A           Clean   
A           Clean   NoOp    A           Clean   
A           Clean   NoOp    A           Clean   
A           Clean   NoOp    A           Clean   
A           Clean   NoOp    A           Clean   
A           Clean   NoOp    A           Clean   
A           Clean   NoOp    A           Clean   
A           Clean   NoOp    A           Clean
```
