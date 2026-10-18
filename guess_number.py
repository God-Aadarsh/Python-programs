import random
import os
import tkinter as tk
from tkinter import ttk

difficulty = {
        'Easy' : {
                'max_num': 50,
                'max_attempts': 10,
                'score': 10    
        },
        'Medium' : {
                'max_num': 100,
                'max_attempts': 7,  
                'score': 20       
        },        
        'Hard' : {
                'max_num': 200,
                'max_attempts': 5,
                'score': 30          
        },
}

best_score = 0
total = 0
score = 0
rand = 0
game_active = False
def play_game():
    global game_active, rand, max_attempts, score, total, best_score
    if not game_active: 
        settings= difficulty[dropdown.get()]
        max_number = settings['max_num']
        max_attempts = settings['max_attempts'] 
        score = settings['score']  
        rand = random.randint(1, max_number)
        game_active= True
        
    try:
                ch = int(num_entry.get())
    except ValueError:
            result.config(text="Please enter number..")
            
    if ch > rand:
            result.config(text="Your guess is high !!")
    elif ch < rand:
            result.config(text= "Your guess is low !!")
    else:
            result.config(text=f'You won. The number was {rand}....')
            game_active = False
            total+= score
            total_scores.config(text = f'Score: {total}')
            
                    
    

    max_attempts -= 1
    attempt.config(text=f'Attempts Remaining: {max_attempts }')
    if max_attempts == 0:
            result.config(text=f'You lose. The number was {rand}....') 
            game_active = False
    if os.path.exists("score.txt"):
        with open("score.txt", "r") as f:
            for lines in f:
                 line = lines.strip()
                 if not line:
                       continue
                 scores = int(line)
                 if scores > total :
                    best_score = scores
                    highest_score.config(text=f'High Score: {best_score}')
    if total > best_score:
             with open("score.txt", "w") as f:
                f.write(str(total) + "\n")
                highest_score.config(text=f'High Score: {total} Congrats New High Score!!')
    lbl3_entry.delete(0,tk.END)
    
def quit_game():
     
        
         window.destroy()

window = tk.Tk()
window.configure(bg="#0F172A")
diff_entry  = tk.StringVar()
num_entry = tk.StringVar()

main_frame = tk.Frame(window, padx= 20 , pady= 20)
main_frame.place(relx= 0.5, rely= 0.5, anchor="center" )
labl_1 = tk.Label(main_frame, text= "Guessing Game", font=("Minecraft", 20 , "bold"), bg= "#0F172A", fg = "#F8FAFC", width = 20 , height = 3, relief= "raised")
lbl_2 = tk.Label(main_frame, text = "Difficulty", font=("Minecraft", 15, "normal" ), bg= "#0F172A", fg="#F8FAFC", width = 10, height = 2)
dropdown = ttk.Combobox(main_frame, values = ['Easy', 'Medium','Hard'], state = "readonly")
dropdown.set("Easy")


lbl_3 = tk.Label(main_frame, text = "Guess the number ", font=("Minecraft", 15, "normal" ), bg= "#0F172A", fg="#F8FAFC", width = 20, height = 2)
lbl3_entry = tk.Entry(main_frame, textvariable= num_entry )

result= tk.Label(main_frame, text =" " , font= ("Minecraft", 17, "normal" ), width = 25, height = 2)
attempt = tk.Label(main_frame, text =" Attempts :  " , font= ("Minecraft", 17, "normal" ), bg= "#0F172A", fg="#F8FAFC", width = 25, height = 1)
total_scores = tk.Label(main_frame, text =" Score : 0 " , font= ("Minecraft", 17, "normal" ), bg= "#0F172A", fg="#F8FAFC", width = 20, height = 1)
highest_score = tk.Label(main_frame, text =" High Score: " , font= ("Minecraft", 17, "normal" ), bg= "#0F172A", fg="#F8FAFC", width = 25, height = 1)
button = tk.Button(main_frame, text="Submit",command= play_game ,width= 15 , bg = "#38BDF8", fg="#0F172A"  )
quit_button = tk.Button(main_frame, text= "Quit" ,command= quit_game, width = 15, bg = "#38BDF8", fg="#0F172A" )

labl_1.grid(row = 0 , column = 0 , columnspan= 2 , pady=(0,20))
lbl_2.grid(row = 1, column = 0 , padx = 10 , pady= 10 )
dropdown.grid(row =1 , column = 1 )
lbl_3.grid(row = 2, column = 0 , padx = 10 , pady= 10 )
lbl3_entry.grid(row = 2 , column = 1)
result.grid(row = 3, column = 0 , padx= 10, pady = 10 )
attempt.grid(row = 4, column = 0 , padx= 10, pady = 10 )
total_scores.grid(row = 5 , column= 0 ,padx = 10 , pady= 10)
highest_score.grid(row = 6 , column= 0 ,padx = 10 , pady= 10)
button.grid(row = 7, column = 0 , columnspan= 2 , pady=(0,20))
quit_button.grid(row = 8 , column =0 , columnspan = 2 , pady=(0,20))



window.geometry("600x400")
window.mainloop()        
            



        


