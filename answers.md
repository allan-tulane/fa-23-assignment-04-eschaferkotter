# CMPS 2200 Assignment 4
## Answers

**Name:**Ethan Schaferkotter


Place all written answers from `assignment-04.md` here for easier grading.
1a) Starting with the highest denomination of coin that is <= of N, we continuously take this highest denomination away from N until N is 0.

1b) Because the coins in this context are powers of 2, the greedy solution also eventually leads to the optimal solution. The coin chosen is always 2^c for a positive number c, and this number can be continuously taken away.

The greedy choice says that what is optimal in one case will lead to an optimal solution for all cases. Since the greedy solution is optimal for all subcases it is optimal in general.

The optimal substructure property says that an optimal solution contains optimal solutions to other subproblems. This is true as the greedy solution is also optimal for subproblems, e.g. N - 2^c

1c) 
Work is O(n), since subtracting the coins is linear
Span is sequential so it is also O(n)

2a) The greedy algorithm doesnt work here in cases like as if the target N is 7, and the denominations you are given are 1, 3, 4, and 5. The greedy algorithm will pick up one 5 and two 1's. However, the optimal choice here is one 4 and one 3, thereby reducing the number of coins from 3 to 2.

2b) The problem has the optimal substructure property ecause the optimal solution also contains optimal solutions to other subproblems. The subproblems would be the remaining amount of money needed after any subtractions, which can ideally be solved with an optimal algorithm.

2c) We would have to use a bottom-up approach for this, so we'd have to compute all the solutions for the subproblems. To do this a 2d array of the solutions could be made.
The subproblems would be k*n so, work would be O(nk)
The span is the longest path in the DAG which would be depth O(n) therefore the span is O(n) 
