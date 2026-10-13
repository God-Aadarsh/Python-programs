
import tkinter as tk
import random 
collection = "abscdefghijklmnopqrstuvwxyz1234567890!#$%^&*"
window = tk.Tk()
length_entry = tk.IntVar()
def submit():
    length = length_entry.get()
    password = ""
    for x in range(length):

          password += random.choice(collection) 
    result.config(text=f'Password = {password}')
        
main_frame = tk.Frame(window, padx= 20, pady=20)
main_frame.place(relx= 0.5 , rely= 0.5 , anchor= "center")
lbl = tk.Label(main_frame, text= "Password Generator", font = ("arial", 20, "bold"), bg = "light blue", fg = "dark blue", width= 20, height= 4 , relief= "raised" )
lbl_2 = tk.Label(main_frame, text= "Enter the length of the password: ", font= ("arial" , 12 , "bold"), bg ="light yellow", fg = "dark blue")
entry = tk.Entry(main_frame, textvariable= length_entry )
button = tk.Button(main_frame, text="Submit", command= submit, width= 20, height= 2)
result = tk.Label(main_frame, text= "")




lbl.grid(row = 0 , column= 0 ,columnspan= 2 , pady= (0,25))
lbl_2.grid(row = 1 , column= 0, padx= 5, pady= 10 , sticky= "e")
entry.grid(row = 1 , column= 1,padx= 5,  pady = 10)
button.grid(row =2 , column= 0, columnspan=2 , pady= 10 )
result.grid(row = 3, column= 0, columnspan= 2 , pady = 10 )
window.geometry('600x400')
window.mainloop()
