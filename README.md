# multiples-a-b
The purpose of the program is to find all the multiples of the first two integers provided up to the limit of the third number provided. The numbers are expected to be provided in an input file as a list of strings of 3 integers with a space between them.  The output, on screen and to a file provided as the second argument, is a sorted list of the multiples of the integers.  The integers are sorted ascending within the line and the whole list is sorted ascending according to how many integers.

Prerequisites: python3.  The program was created with Python 3.10.7

## How to run
At the command prompt run:
`python3 multiples-a-b.py input.txt output.txt`

The output file can be defined as preferred.  The input file should be text file containing lines with 3 integers with a space between them

## Improvements
- Add error handling to verify input file data is of the expected format
- Add error handling for cases where output file is not provided
