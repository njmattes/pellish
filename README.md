# Pellish
`pellish` generates a matrix of Pell-like series
based on minimum, maximum, and required values supplied by the user. Meaning
that at least one of the series will contain the required value, and all
values will be within the minimum and maximum specified.  

## Installation
Typical `python setup.py install` should suffice.
  
## Usage
`pellish -h` should show you the help screen.
  
`pellish min req max` creates a pellish matrix, where `min` is the minimum 
value in any series, `req` appears in at least one series, and `max` is 
the maximum value in all series.

`pellish ... -t` shows 'triplets' (three adjacent numbers, a, b, c 
where c / a = 1 + √2, c / b = √2 or (1 + √2) / √2)

`pellish ... -d` 'unravels' the diagonals of the series

`pellish ... -c -f PATH` writes the pellish matrix to a CSV file located 
at `PATH`.

## Examples
`pellish 1 29 500` will generate the Pell series up to 408, and then 
the pellish matrix of series that contain the differences of the prior 
series.

`pellish 2 6 500` will do the same but starting with the Pell-Lucas series.
 
`pellish 0 1 1000` will fail. Miserably.

## How it works
`pellish` generates an initial Pell-like sequence based on your required
value, x*(n)*, by finding suitable values for x*(n–1)* and x*(n–2)*, with 
x*(n)* = 2 * x*(n–1)* + x*(n–2)*, x*(n–2)* >= min. 

If possible, given your minimum, it will create multiple series of lesser 
values, based on the differences in the initial series. It will proceed
with this until the initial value of a series is less than your specified 
minimum. Then it generates series of larger values, again based on 
differences of prior series, until it reaches your maximum value and/or 
a series of fewer than 3 values.

## Et cetera
I've made up some silly lingo when I use Pell-like sequences in my design 
work. Very non-technical, but it's hard to understand some of the options
and internal methods without understanding them.

*Diagonals* are series of numbers in the pellish matrix,  whose
pairs converge towards 1 : √2.

*Triplets* refer to groups of three adjacent values whose pairs are in the 
(approximate) proportions 1 : √2, 1 : (1 + √2) / √2. and 1 : 1 + √2 

A *minor* triplet is one whose smallest numbers approximate the proportion 
1 : √2.

A *major* triplet's largest numbers approximate 1 : √2.