# Coding challenge: Deepest Pit

## Description
A non-empty zero-indexed array `B` consisting of `M` integers is given. A pit in this array is any triplet of integers `(X, Y, Z)` such that:
```
0 ≤ X < Y < Z < M
```
Sequence `[B[X], B[X+1], ..., B[Y]]` is strictly decreasing, i.e. `B[X] > B[X+1] > ... > B[Y]`\
Sequence `B[Y], B[Y+1], ..., B[Z]` is strictly increasing, i.e. `B[Y] < B[Y+1] < ... < B[Z]`\
The depth of a pit `(X, Y, Z)` is the number `min{B[X] − B[Y], B[Z] − B[Y]}.`

For example, consider array `B` consisting of 10 elements such that:
```
B[0] = 0
B[1] = 2
B[2] = 7
B[3] = -4
B[4] = 0
B[5] = 4
B[6] = 0
B[7] = -6
B[8] = 4
B[9] = 6
```
Triplet `(2, 3, 4)` is one of pits in this array, because sequence `[B[2], B[3]]` is strictly decreasing `(7 > −4)` and sequence `[B[3], B[4]]` is strictly increasing `(−4 < 0)`. Its depth is `min{B[2] − B[3], B[4] − B[3]} = 4`. Triplet `(2, 3, 5)` is another pit with depth 8. Triplet `(5, 7, 8)` is yet another pit with depth 10. There is no pit in this array deeper (i.e. having depth greater) than 10.

Write a function:

```
function deepest_pit(B)
```
that, given a non-empty zero-indexed array `B` consisting of `M` integers, returns the depth of the deepest pit in array `B`. The function should return −1 if there are no pits in array `B`.

For example, for the above array `B`, the function should return 10, as explained above.

Write an efficient algorithm for the function.

Assume that:

`M` is an integer within the range `[1..1,000,000]`;
each element of array B is an integer within the range `[−100,000,000..100,000,000]`.