# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 20:04:37 2023

@author: HamzaEren
"""

def SolveSudoku(panel):
    find = FindEmpty(panel)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1, 10):
        if Valid(panel, i, (row, col)):
            panel[row][col] = i
        
            if SolveSudoku(panel):
                return True
        
            panel[row][col] = 0
        
    return False


def Valid(panel, num, pos):
    for i in range(len(panel[0])):
        if panel[pos[0]][i] == num and pos[1] != i:
            return False
    
    for i in range(len(panel)):
        if panel[i][pos[1]] == num and pos[0] != i:
            return False
    
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if panel[i][j] == num and (i, j) != pos:
                return False
            
    return True


def PrintBoard(panel):
    print("\n\n")

    for i in range(len(panel)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(panel[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(panel[i][j])
            else:
                print(str(panel[i][j]) + " ", end="")
                    
                    
def FindEmpty(panel):
    for i in range(len(panel)):
        for j in range(len(panel[0])):
            if panel[i][j] == 0:
                return (i, j)
            
    return None

panel = []
for x in range(1, 10):
    satir = input(f"{x}. satır: ")
    panel.append(list(satir))
    
for i in range(9):
    for j in range(9):
        panel[i][j] = int(panel[i][j])
        

SolveSudoku(panel)
PrintBoard(panel)