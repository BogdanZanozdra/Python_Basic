# 3. Создайте программу для игры в ""Крестики-нолики""

# from tkinter import *
# import random, time

# window = Tk()
# window.title('BZ')
# label = Label(width=30, text = "Играем в крестики - нолики!", font=('Arial', 15, 'bold'))

# def push(b):
#     global game
#     global game_left
#     turn = 1
    
#     if turn % 2 == 0:
#         game[b] = 'X'
#         buttons[b].config(text='X', state='disabled')
#         # game_left.remove(b)
#         turn += 1
#         # print(i)
#         if turn % 2 != 0:
#             game[b] = 'O'
#             buttons[b].config(text='O', state='disabled')
#             # game_left.remove(b)
#             turn += 1
#             # print(i)
        
# game = [None] * 9 # создаю список ходов
# game_left = list(range(9)) # список оставшихся ячеек в игре

# buttons = [Button(width=5, height=2, font=('Arial', 30, 'bold'), command=lambda x=i: push(x)) for i in range(9)]

# label.grid(row=0, column=0, columnspan=3)

# roww = 1; col = 0
# for i in range(9):
#     buttons[i].grid(row=roww, column=col)
#     col += 1
#     if col == 3:
#         roww += 1
#         col = 0

# window.mainloop()



# 2. RLE

def encode(s):
 
    encoding = "" # сохраняет выходную строку
 
    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1
 
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
 
        # добавляет к результату текущий символ и его количество
        encoding += str(count) + s[i]
        i = i + 1
 
    return encoding
 
 
if __name__ == '__main__':
 
    s = 'ABBCCCDAAA'
    print(encode(s))
