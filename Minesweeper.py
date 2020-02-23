from tkinter import *
from tkinter import messagebox
import random

class App():
    
    def __init__(self):
        self.board = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            ]
        self.board_cover = [
            [True,True,True,True,True,True,True,True, True],
            [True,True,True,True,True,True,True,True, True],
            [True,True,True,True,True,True,True,True, True],
            [True,True,True,True,True,True,True,True, True],
            [True,True,True,True,True,True,True,True, True],
            [True,True,True,True,True,True,True,True, True],
            [True,True,True,True,True,True,True,True, True],
            [True,True,True,True,True,True,True,True, True],
            [True,True,True,True,True,True,True,True, True],
            [True,True,True,True,True,True,True,True, True],
            ]
        self.counter = 0
        self.mines = []
        self.window = Tk()
        self.window.title('Minesweeper')
        self.canvas = Canvas(self.window, bg='white', height=450, width=450)
        self.canvas.pack()
        self.menubar = Menu(self.window)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.about)
        self.filemenu.add_command(label="New Game", command=self.new_game)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.window.destroy)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.window.config(menu=self.menubar)
        self.set_mines()
        self.create_canvas()
        self.window.mainloop()
        
    def about(self):
        messagebox.showinfo('About', 'Made by Jason Alencewicz!')
        return

    def new_game(self):
        self.counter = 0
        self.mines = []
        for row, value1 in enumerate(self.board):
            for column, value2 in enumerate(value1):
                self.board[row][column] =  0
        for row, value1 in enumerate(self.board_cover):
            for column, value2 in enumerate(value1):
                self.board_cover[row][column] =  True
        self.set_mines()
        self.canvas.delete("all")
        self.create_canvas()
        return

    def set_mines(self):
        while len(self.mines) < 10:
            row = random.randint(0,8)
            column = random.randint(0,8)
            mine = 'r'+str(row)+'c'+str(column)
            if mine not in self.mines:
                self.mines.append(mine)
                self.board[row][column] = 'X'
            else:
                continue
        return self.set_numbers()

    def set_numbers(self):
        for row in range(len(self.board)):
            self.check_left_right(row)
            if row != 0:
                self.check_upper_row(row)
            if row != 8:
                self.check_lower_row(row)
        return

    def check_left_right(self, row):
        for column in range(len(self.board)):
            if self.board[row][column] == 'X':
                continue
            elif column == 0:
                left = None
                right = self.board[row][column+1]
            elif column == 8:
                left = self.board[row][column-1]
                right = None
            else:
                left = self.board[row][column-1]
                right = self.board[row][column+1]

            if left == 'X':
                self.board[row][column] += 1
            if right == 'X':
                self.board[row][column] += 1
        return

    def check_upper_row(self, row):
        for column in range(len(self.board)):
            if self.board[row][column] == 'X':
                continue
            elif column == 0:
                above = self.board[row-1][column]
                upper_left = None
                upper_right = self.board[row-1][column+1]
            elif column == 8:
                above = self.board[row-1][column]
                upper_left = self.board[row-1][column-1]
                upper_right = None
            else:
                above = self.board[row-1][column]
                upper_left = self.board[row-1][column-1]
                upper_right = self.board[row-1][column+1]

            if above == 'X':
                self.board[row][column]+=1
            if upper_left == 'X':
                self.board[row][column]+=1
            if upper_right == 'X':
                self.board[row][column]+=1
        return

    def check_lower_row(self, row):
        for column in range(len(self.board)):
            if self.board[row][column] == 'X':
                continue
            elif column == 0:
                below = self.board[row+1][column]
                lower_left = None
                lower_right = self.board[row+1][column+1]
            elif column == 8:
                below = self.board[row+1][column]
                lower_left = self.board[row+1][column-1]
                lower_right = None
            else:
                below = self.board[row+1][column]
                lower_left = self.board[row+1][column-1]
                lower_right = self.board[row+1][column+1]

            if below == 'X':
                self.board[row][column]+=1
            if lower_left == 'X':
                self.board[row][column]+=1
            if lower_right == 'X':
                self.board[row][column]+=1
        return

    def create_canvas(self):
        location = [0,-50, 0, 0]
        for x in range(len(self.board)):
            location[0] = 0
            location[1]+= 50
            location[2] = 50
            location[3]+=50
            for y in range(len(self.board)):
                tag_id = 'r'+str(x)+'c'+str(y)
                self.canvas.create_rectangle(location[0], location[1], location[2], location[3],  outline="darkgray", fill="lightgrey", tag=tag_id)
                self.canvas.tag_bind(tag_id, '<1>', self.on_click)
                location[0]+=50
                location[2]+=50
        return 

    def on_click(self, event):
        item = self.canvas.itemcget(self.canvas.find_closest(event.x, event.y), "tag").replace(' current','')
        row = int(item[1])
        column = int(item[3])
        self.config_square(row, column, item)
        return

    def config_square(self, row, column, item):
        if self.board_cover[row][column] == True:
            self.counter += 1
            if self.check_game_over(row, column, item):
                return
            else:
                self.draw_number(row, column, item)
        else:
            return
        return

    def draw_number(self, row, column, item):
        number = self.get_number(row,column)
        color = self.get_color(number)
        location = list(self.canvas.bbox(self.canvas.find_withtag(item)))
        coordinates = self.get_location(location)
        x = location[0]+25
        y = location[1]+25
        self.canvas.create_text((x, y), text=number, fill=color,font=24)
        return
        
    def get_color(self, number):
        if not number:
            color = ''
        elif number <= 1:
            color ='blue'
        elif number == 2:
            color = 'green'
        elif number == 3:
            color = 'red'
        elif number >= 4:
            color = 'purple'
        return color
            
    def get_location(self, location):
        location[0]+=1
        location[1]+=1
        location[2]-=1
        location[3]-=1
        return location

    def get_number(self, row, column):
        number = self.board[row][column]
        if number == 0:
            number = ''
            self.clear_squares(row, column)
            return number
        else:
            return number
        
    def clear_squares(self, row, column):
        surrounding = [[row,column-1], [row,column+1], [row-1,column], [row+1,column]]
        for x in surrounding:
            row = x[0]
            column = x[1]
            if (row < 0 or row > 8) or (column < 0 or column > 8):
                continue
            item = 'r'+str(row)+'c'+str(column)
            self.config_square(row, column, item)
        return
        
    def check_game_over(self, row, column, item):
        self.uncover_square(row, column, item)
        if self.board[row][column] == 'X':
            self.draw_bomb(row, column, item)
            refresh = messagebox.askyesno("Boom!", "Player loses! Would you like to play again?")
            if refresh:
                self.new_game()
                return True
            else:
                self.window.destroy()
                return True
        elif self.counter == 71:
            self.draw_number(row, column, item)
            self.draw_flags()
            refresh = messagebox.askyesno("Congratulations!", "Player wins! Would you like to play again?")
            if refresh:
                self.new_game()
                return True
            else:
                self.window.destroy()
                return True
        else:
            return False
            
    def uncover_square(self, row, column, item):
        self.board_cover[row][column] = False
        self.canvas.itemconfig(self.canvas.find_withtag(item), fill="white", outline="lightgray")
        return
                                            
    def draw_bomb(self, row, column, item):
        location = list(self.canvas.bbox(self.canvas.find_withtag(item)))
        coordinates = self.get_location(location)
        x = location[0]+25
        y = location[1]+25
        self.canvas.create_text((x, y), text='!', fill='orange',font=24)
        return

    def draw_flags(self):
        for item in self.mines:
            location = list(self.canvas.bbox(self.canvas.find_withtag(item)))
            coordinates = self.get_location(location)
            x = location[0]+23
            y = location[1]+12
            self.canvas.create_polygon((x, y, x, y+20, x+15, y+10),fill='red')
            self.canvas.create_line(x, y+2, x, y+39, fill='black')
        return
                   
App()
