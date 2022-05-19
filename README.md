# Google Foobar ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/44) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


## Level 1 ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/100)
### Question 1 - "I Love Lance & Janice"
The premise of this question was quite simple. 
Essentially all you had to do was 'flip' or 'mirror' each lowercase letter in a string along the axis m | n (for example, a => z, t => g). 
Solving this problem just required some simple addition and subtraction. If you know that every lowercase letter has an ASCII value of 96 < ord(c) < 123, 
it can be deduced that the calculation to 'flip' any letter by ASCII value is simply 
(27-(ord(c)-96))+96 => 219-ord(c). and all you need to do at that point is to convert the ASCII value back into a character using chr(n), and add it to the 'translated' string.


## Level 2 ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/100)
### Question 2 - "Ion Flux Relabeling"
The goal of this problem was to take a perfect binary tree of height h, labeled in post-order (example pictured below),


                    7
                  /   \
                 3     6
                / \   / \
               1   2 4   5
               
and find the parent of a given nodes in list q. Because it is binary tree, I elected to use binary search. A perfect binary tree of height h has 2<sup>h</sup>-1 nodes, so the search space is 1 to 2<sup>h</sup> - 1, meaning each node of index n has a a parent of index n//2 or n-1. My approach was for each node to find the 'halfway' point, and check whether the node was greater than the halfway point, changing the beginning or the end of the search space to the old 'halfway' point accordingly.

### Question 3 - "Don't Get Volunteered"
This problem involved A BFS on a graph. The goal was to find the least amount of moves it took for a knight on a chessboard to get from a starting point to a destination. The board spaces are labeled from 0 to 63 like so:

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
My initial approach was to have a list [0...63] and use moves like +17, -15, etc. to find the least amount of moves it took to get to the destination. Instead of doing this, I eventually elected to use a coordinate system (i.e. (0, 1) would be the board square with index 1) to find the shortest path, because it was a bit easier to visualize. This involved a very similar approach to my original idea. I used a list of all possible moves that the knight could make from the a given point for a move in each iteration, eventually finding the shortest path using a BFS algorithm. 

## Level 3 ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/33)
### Question 4
### Question 5
### Question 6

## Level 4 ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/0)
### Question 7
### Question 8

## Level 5 ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/0)
### Question 9
