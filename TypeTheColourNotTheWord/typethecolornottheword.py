import tkinter
import random 
colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
score=0
timeleft=60

def startGame(event):
    if timeleft == 60:
        countdown()
    nextColour() 

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft)) #updates the time left label
        timeLabel.after(1000, countdown) #keeps updating the time left

def nextColour(): #function to choose next color and display color
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set() #so the entry box is editable        
        if e.get().lower() == colours[0].lower(): #checks if the colour entered is equal to the colour displayed
            score += 1        
        e.delete(0, tkinter.END) #clears the entry box so that it is ready for next entry
        random.shuffle(colours) #shuffles the list of colours        
        label.config(fg=str(colours[1]), text=str(colours[0])) #change the colour to type, by changing the text _and_ the colour to a random colour value  
        
        scoreLabel.config(text="Score: " + str(score)) #update the score on screen score board
    else:
        print("Score is: " + str(score))

    
root = tkinter.Tk() #open GUI window
root.configure(bg='gray')
root.title("Type The Color Not The Word") #Title the GUI window
root.geometry("500x400") #Set size of window

instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!", font=('Calibri', 15), fg = 'black', bg = 'gray') #add an instructions label.
instructions.pack()

instructions2 = tkinter.Label(root, text="Space Bar to enter" , font=('Calibri', 15), fg = 'black', bg = 'gray') #add an instructions2 label.
instructions2.pack()

scoreLabel = tkinter.Label(root, text="Press space bar to start", font=('Calibri', 15), fg = 'black', bg = 'gray') #add a score label
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Calibri', 15), fg = 'black', bg = 'gray') #add a time left label
timeLabel.pack()

label = tkinter.Label(root, font=('Calibri', 60), bg = 'gray') #add a displaying the colours label
label.pack()

e = tkinter.Entry(root) #add entry box so user can type the color

root.bind('<space>', startGame) #run the 'startGame' function when the space bar is pressed.
e.pack()

e.focus_set() #set focus

root.mainloop() #run gui
