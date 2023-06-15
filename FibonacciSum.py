from tkinter import*
root = Tk()
root.title("Fibonacci Sum")
root.geometry("600x200")
root.configure(bg = "red1")

number_of_digits = Entry(root)
digits = number_of_digits.get()
series = Label(root, font = ("Comic Sans MS", 12, "bold"), text = "The First " + str(digits) + "Terms Of The Fibonacci Series Are ")
fibonacci_sum = Label(root, font = ("Comic Sans MS", 12, "bold"))
def Fibonacci():
    num = int(number_of_digits.get())
    n1 = 0
    n2 = 1
    sum = 0
    i = 1
    total_sum = n1 + n2
    while(i<=num):
        series["text"] += str(sum) + ", "
        sum = n1 + n2
        n1 = n2
        n2 = sum
        total_sum += n2
        fibonacci_sum["text"] = "The Sum Of The First " + str(num) + "Terms Of The Fibonacci Series Is " + str(total_sum)
        
show_button = Button(root, command = Fibonacci, text = "Show Fibonacci Series and Sum", fg = "black", font = ("Comic Sans MS", 12, "bold"), bg = "red2")
  
number_of_digits.place(relx = 0.5, rely = 0.3, anchor = CENTER)
show_button.place(relx = 0.5, rely = 0.5, anchor = CENTER)
series.place(relx = 0.5, rely = 0.7, anchor = CENTER)
fibonacci_sum.place(relx = 0.5, rely = 0.9, anchor = CENTER)


root.mainloop()