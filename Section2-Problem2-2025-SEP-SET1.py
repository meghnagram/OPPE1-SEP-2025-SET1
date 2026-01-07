


nums = []
while True:
    line = input().strip()
    if line == 'stop':
        break
    if line == '':
        continue
    nums.append(int(line))

for a,b in zip(nums[::2],nums[1::2]):
    print(round((a+b)/2,2))
if len(nums)%2==1:
    print(nums[-1])


Print Average of Every Two Non-Empty Values Until Stop
You will be given a sequence of lines. Each line contains either:

a numeric value (an integer, possibly negative),
an empty line (which should be ignored), or
the word stop (which terminates the input).
Read the input until the word stop is encountered.
Collect all numeric values in the order they appear (ignoring empty lines).
For every pair of consecutive numbers, output the average of the pair (rounded to decimal places (use round(value,2))).
If the total number of numeric values is odd, output the last value itself (no averaging).

Each result should be printed on its own line.

NOTE: This is an I/O type question. You need to write the complete code to read the input and print the output.

Input Format
A sequence of lines, each line containing:

an integer,
an empty line, or
the string stop.
The input ends when the string stop is read.

Output Format
Print each result on a separate line with averages rounded to decimal places (use round(value,2))

Example
Input

1
2
3
4
5
stop
Output

1.5
3.5
5
Input

5
6
stop
Output

5
Input

   
10


20

30
stop
Output

15
30
