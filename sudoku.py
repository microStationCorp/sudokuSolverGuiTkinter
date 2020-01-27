import numpy as np
from tkinter import *



class sudoku:
    __root=Tk()
    variable=[]
    __board = np.zeros((9, 9))
    def __init__(self):
        self.__root.title("sudoku")
        self.__root.geometry("300x270")
        self.__root.resizable(0,0)
        self.__frame=Frame(self.__root)
        self.__frame.pack()
        self.entrys = []
        for i in range(81):
            self.variable.append(StringVar())
        for i in range(9):
            for j in range(9):
                self.entrys.append(Entry(self.__frame,width=3, textvariable=self.variable[(i*9)+j]))
                self.entrys[-1].grid(padx=0, pady=0, row=i, column=j)
        btn=Button(self.__root,text="Solve",command=self.main)
        btn.pack(pady=20,side=LEFT,padx=15)
        clear=Button(self.__root,text="clear",command=self.clear_cells)
        clear.pack(pady=20,side=LEFT)

    def clear_cells(self):
        for i in range(81):
            self.variable[i].set("")

    def make_board(self):
        for i in range(81):
            val=self.variable[i].get()
            if val=='':
                self.__board[int(i)//9,int(i)%9]=0
            else:
                self.__board[int(i) // 9, int(i) % 9] = val
        return self.__board


    def run(self):
        self.__root.mainloop()

    def print_board(self,brd):
        for i in range(len(brd)):  # catch row
            for j in range(len(brd[0])):  # catch column
                if self.variable[(i*9)+j].get()=='':
                    self.variable[(i * 9) + j].set(int(brd[i][j]))


    def check_row_column(self,array, num):
        for i in array:
            if i == num:
                return True
        return False


    def check_sub_group(self,pos, brd, num):
        for i in range(len(brd)):  # catch row
            if pos[0] // 3 == i // 3:
                for j in range(len(brd[0])):  # catch column
                    if pos[1] // 3 == j // 3:
                        if num == brd[i][j]:
                            return True
        return False


    def get_empty(self,brd):
        list = []
        for i in range(len(brd)):  # catch row
            for j in range(len(brd[0])):  # catch column
                if brd[i][j] == 0:
                    list.append((i, j))
        return list


    def main(self):
        brd=self.make_board()
        zeros = self.get_empty(brd)
        z = 0
        while z < len(zeros) and z>=0:
            num = brd[zeros[z]] + 1
            while num < 10:
                if not self.check_row_column(brd[zeros[z][0]], num) and not self.check_row_column(brd[:, zeros[z][1]],num) and not self.check_sub_group(zeros[z],brd,num):
                    brd[zeros[z]] = num
                    break
                else:
                    num += 1
            if num>=10:
                brd[zeros[z]] =0
                z-=1
            else:
                z+=1
        self.print_board(brd)


if __name__ == '__main__':
    sdk=sudoku()
    sdk.run()