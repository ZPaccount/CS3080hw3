'''
Homework 3-1
Name: Zachary Pace
Date: 2/22/2023
Description: reverse axis to show text art
'''

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for y in range(len(grid[0])):
    line = ''
    for x in range(len(grid)):
        line = line + grid[x][y]
    print(line)
