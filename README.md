# make10solver

## Overview

This is a tool to solve the famous number puzzle game "make10".

## What is "make10"?

"make10" is the game to make the number '10' from 4 digits.
You can use '+' (add), '-' (sub), '*' (mul), and '/' (div) as a binary operator.
You can change the order of digits as you like.

For example, from 4 digits '1', '2', '3', and '4',
you can make the number '10' as follows:

 - 1 + 2 + 3 + 4
 - 1 * 2 * 3 + 4
 - (3 - 1) * 4 + 2

## How to use this program

~~~
./make10.py <number>
~~~

### Generating answer mode

If you specify 0 or positive number as the first argument, the program will make all possible answers for that digits.

For example, if you specify "1234", the program displays the all solutions of 4 digits '1', '2', '3', and '4'.

### Find difficult numbers mode

If you specify a negative number, the program will display all sets of numbers which have solutions equal or less than the absolute number of specified numbers.

For example, if you specify "-1", the program displays the set of numbers which has only 1 solution, e.g. '1', '1', '5', '8'.
