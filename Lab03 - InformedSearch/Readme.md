# Exercise notes
**TODO**
1. Modify the program from last class to implement the greedy best first and A* search for this graph.
   1. Done
2. Compare the solution paths.
   1. `Greedy_best` = A,D,H,K
   2. `A*` = A,D,H,L
3. Play with the heuristics and see what different heuristic functions would yield as solutions.
4. Play with weighted A* with different weights and compare.

Prove a*:  
a:  
b = (1+5=6)  
c = (2+5=7)  
d = (4+2=6)  

a,d

b:  
f = (1+5+5=11)  
e = (1+4+4=9) 

a,b,e

e:  
g = (1+4+2+4=11)  
h = (1+4+3+1=9)  

a,b,e,h

h:  
k = (1+4+3+5+0=13)  
l = (1+4+3+6+0=14)

a,b,e,h,k  

d:  
h = (4+1+1=6)   
i = (4+4+2=10)  
j = (4+2+1=7)  

a,d,h  

h:  
l = (4+1+5+0=10)  
k = (4+1+6+0=11)

Kortest a*= a,d,h,l

# Homework notes
![Vacuum](/Other/Media/Vacuum.png)
The state of the search should be represented with three elements: a state, a path and a
cost. 

Ultimately, cost is defined as the number of moves taken to achieve the goal state from
the initial state.
