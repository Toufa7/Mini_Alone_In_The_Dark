from tkinter import *
import  os
import  subprocess
import  random

exam = Tk()
exam.title("Mini Alone In The Dark")
# exam.resizable(0,0)
exam.minsize(950,720)

def level_0():
    dir = os.listdir(".")
    file = random.choice(dir)
    run = (open(file).read())

    print_exam.delete('1.0', END)
    print_exam.insert(END, run)

# def level_1():
#     dir = os.listdir("./level1/")
#     file = random.choice(dir)
#     run = (open(file).read())

#     print_exam.delete('1.0', END)
#     print_exam.insert(END, run)

# def level_2():
#     dir = os.listdir("./level2/")
#     file = random.choice(dir)
#     run = (open(file).read())

#     print_exam.delete('1.0', END)
#     print_exam.insert(END, run)

# def level_3():
#     dir = os.listdir("./level3/")
#     file = random.choice(dir)
#     run = (open(file).read())

#     print_exam.delete('1.0', END)
#     print_exam.insert(END, run)


# def level_4():
#     dir = os.listdir("./level4/")
#     file = random.choice(dir)
#     run = (open(file).read())

#     print_exam.delete('1.0', END)
#     print_exam.insert(END, run)

# def level_5():
#     dir = os.listdir("./level5/")
#     file = random.choice(dir)
#     run = (open(file).read())

#     print_exam.delete('1.0', END)
#     print_exam.insert(END, run)


lvl0 = Button(exam, border=4, text="Level 0",bg='azure', padx=10, pady=7, command=level_0)
lvl0.place(x= 50, y=50)

# lvl1 = Button(exam, border=4, text="Level 1",bg='azure', padx=10, pady=7, command=level_1)
# lvl1.place(x= 200, y=50)

# lvl2 = Button(exam, border=4, text="Level 2",bg='azure', padx=10, pady=7, command=level_2)
# lvl2.place(x= 350, y=50)

# lvl3 = Button(exam, border=4, text="Level 3",bg='azure', padx=10, pady=7, command=level_3)
# lvl3.place(x= 500, y=50)

# lvl4 = Button(exam, border=4, text="Level 4",bg='azure', padx=10, pady=7, command=level_4)
# lvl4.place(x= 650, y=50)

# lvl5 = Button(exam, border=4, text="Level 5",bg='azure', padx=10, pady=7, command=level_5)
# lvl5.place(x= 800, y=50)

# gen = Button(exam, border=4 ,text="Generate Exercices", bg='LightBlue1',padx=10, pady=5, command=level_5)
# gen.place(x=450, y=200)

print_exam = Text(exam, width=130, height=25, border=4, relief=RAISED)
print_exam.pack()
print_exam.place(x=10, y=300)


exam['background'] = 'light yellow'

# file = get_randomfile("/Users/otoufah/Desktop/exercices/level0/")
# run = subprocess.run(["cat", file])
# print (run)

exam.mainloop()












# from tkinter import *
# import  os
# import  subprocess
# import  random

# exam = Tk()
# exam.title("Mini Alone In The Dark")
# # exam.resizable(0,0)
# exam.minsize(950,720)

# def level_0(path):
#     dir = os.listdir(path)
#     file = random.choice(dir)
#     run = (open(file).read())

#     print_exam.delete('1.0', END)
#     print_exam.insert(END, str(run))

# def level_1(path):
#     dir = os.listdir(path)
#     file = random.choice(dir)
#     run = (open(file).read())

#     print_exam.delete('1.0', END)
#     print_exam.insert(END, str(run))

# def level_2(path):
#     dir = os.listdir(path)
#     file = random.choice(dir)
#     run = (open(file).read())

#     print_exam.delete('1.0', END)
#     print_exam.insert(END, str(run))

# def level_3(path):
#     dir = os.listdir(path)
#     file = random.choice(dir)
#     run = (open(file).read())

#     print_exam.delete('1.0', END)
#     print_exam.insert(END, str(run))


# def level_4(path):
#     dir = os.listdir(path)
#     file = random.choice(dir)
#     run = (open(file).read())

#     print_exam.delete('1.0', END)
#     print_exam.insert(END, str(run))

# def level_5(path):
#     dir = os.listdir(path)
#     file = random.choice(dir)
#     run = (open(file).read())

#     print_exam.delete('1.0', END)
#     print_exam.insert(END, str(run))


# lvl0 = Button(exam, border=4, text="Level 0",bg='azure', padx=10, pady=7, command=level_0("."))
# lvl0.place(x= 50, y=50)

# lvl1 = Button(exam, border=4, text="Level 1",bg='azure', padx=10, pady=7, command=level_1)
# lvl1.place(x= 200, y=50)

# lvl2 = Button(exam, border=4, text="Level 2",bg='azure', padx=10, pady=7, command=level_2("."))
# lvl2.place(x= 350, y=50)

# lvl3 = Button(exam, border=4, text="Level 3",bg='azure', padx=10, pady=7, command=level_3("."))
# lvl3.place(x= 500, y=50)

# lvl4 = Button(exam, border=4, text="Level 4",bg='azure', padx=10, pady=7, command=level_4("."))
# lvl4.place(x= 650, y=50)

# lvl5 = Button(exam, border=4, text="Level 5",bg='azure', padx=10, pady=7, command=level_5("."))
# lvl5.place(x= 800, y=50)

# gen = Button(exam, border=4 ,text="Generate Exercices", bg='LightBlue1',padx=10, pady=5, command=level_5("."))
# gen.place(x=450, y=200)

# print_exam = Text(exam, width=130, height=25, border=4, relief=RAISED, font=('Verdana',8))
# print_exam.pack()
# print_exam.place(x=10, y=300)


# exam['background'] = 'light yellow'

# # file = get_randomfile("/Users/otoufah/Desktop/exercices/level0/")
# # run = subprocess.run(["cat", file])
# # print (run)

# exam.mainloop()
