# Google Foobar ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/44) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


## Level 1 (Basic Programming Knowledge) ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/100)
### Question 1 - "I Love Lance & Janice" :ballot_box_with_check:
The premise of this question was quite simple. 
Essentially all you had to do was 'flip' or 'mirror' each lowercase letter in a string along the axis m | n (for example, a => z, t => g). 
Solving this problem just required some simple addition and subtraction. If you know that every lowercase letter has an ASCII value of $96 < ord(c) < 123$, 
it can be deduced that the calculation to 'flip' any letter by ASCII value is simply 
$(27-(ord(c)-96))+96$ => $219-ord(c)$. and all you need to do at that point is to convert the ASCII value back into a character using chr(n), and add it to the 'translated' string.


## Level 2 (Simple Data Structures) ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/100)
### Question 2 - "Ion Flux Relabeling" :ballot_box_with_check:
The goal of this problem was to take a perfect binary tree of height h, labeled in post-order (example pictured below),
```

     7
   /   \
  3     6
 / \   / \
1   2 4   5
```
               
and find the parent of a given nodes in list q. Because it is binary tree, I elected to use binary search. A perfect binary tree of height $h$ has $2^h-1$ nodes, so the search space is $1$ to $2^h-1$, meaning each node of index $n$ has a a parent of index $n//2$ or $n-1$. My approach was for each node to find the 'halfway' point, and check whether the node was greater than the halfway point, changing the beginning or the end of the search space to the old 'halfway' point accordingly.

### Question 3 - "Don't Get Volunteered" :ballot_box_with_check:
This problem involved A BFS on a graph. The goal was to find the least amount of moves it took for a knight on a chessboard to get from a starting point to a destination. The board spaces are labeled from 0 to 63 like so:
```
-----------------------------------------
| 0  | 1  |  2 | 3  | 4  | 5  | 6  | 7  |
-----------------------------------------
| 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 |
-----------------------------------------
| 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
-----------------------------------------
| 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
-----------------------------------------
| 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 |
-----------------------------------------
| 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 |
-----------------------------------------
| 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 |
-----------------------------------------
| 56 | 57 | 58 | 59 | 60 | 61 | 62 | 63 |
-----------------------------------------
```
My initial approach was to have a list [0...63] and use moves like $+17$, $-15$, etc. to find the least amount of moves it took to get to the destination. Instead of doing this, I eventually elected to use a coordinate system (i.e. $(0, 1)$ would be the board square with index $1$) to find the shortest path, because it was a bit easier to visualize. This involved a very similar approach to my original idea. I used a list of all possible moves that the knight could make from the a given point for a move in each iteration, eventually finding the shortest path using a BFS algorithm. 

## Level 3 (Introduction to Higher-Level Math and Algorithms) ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/33)

### Question 4 - "The Grandest Staircase Of Them All" :ballot_box_with_check:
It was at this point in foobar that I encountered some topics I was not all too familiar with yet. Luckily, Wikipedia and Wolfram MathWorld exist and I was able to learn the mathematics behind this problem. What you had to do was find the number of ways that you could make a set of steps out of $n$ bricks, where each step must be taller than the last. I did a little bit of reading on [partition](https://en.wikipedia.org/wiki/Partition_(number_theory)) and was able to deduce that I needed to find the number of distinct partitions of $n$ bricks (partitions where no two integers are the same). This led me to [this](https://mathworld.wolfram.com/PartitionFunctionQ.html) Wolfram MathWorld article on the partition function $Q(n)$, which illustrates the generating function for for $Q(n)$ to be  
$$G(x) = \prod_{n=1}^{\infty}1+x^n$$ 
which means
$$G(x) = (1+x)(1+x^2)(1+x^3)...(1+x^{n-1}) = 1 + x + x^2 + 2x^3 + 2x^4+ 3x^5...$$
since the number of solutions for any $n$ is the number of ways the terms combine to make $x^n$, you can use the coefficent of $x^{n-1}$ to determine the number of distinct partitions of $n$. The code for this logic turns out to be quite simple, just needing a couple lines illustrating the polynomial multiplication. I'm extremely glad that I did not just try to impliment a brute force algorithm and instead learned the underlying theory, because it not only saved the runtime of my code, but also helped me learn something new in the process.



### Question 5
### Question 6

## Level 4 ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/0)
### Question 7
### Question 8

## Level 5 ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/0)
### Question 9
