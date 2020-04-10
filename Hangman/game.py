import random
word = random.choice(open("WordsForGames.txt").read().split()))

guesses = ''

turns = 11
wrong = 0
while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:
            print char,    
        else:
            print "_",     
            failed += 1 
            
    if failed == 0:        
        print "You won"  
        break       
    guess = raw_input(" Guess a character:") 
    guesses += guess                
    if guess not in word:  
        turns -= 1        
        print "Wrong" 
        wrong += 1
        print "You have", + turns, 'more guesses' 
        if (wrong==1): 
          print"\n"
          print"      |"
          print"      |"
          print"      |"
          print"      |"
          print"      |"
        if wrong==2:
          print"\n"
          print"  +---+"
          print"      |"
          print"      |"
          print"      |"
          print"      |"
          print"      |"
        if wrong==3:
          print"\n"
          print"  +---+"
          print"      |"
          print"      |"
          print"      |"
          print"      |"
          print"      |"
          print"======"
        if wrong==4:
          print"\n"
          print"  +---+"
          print"  |   |"
          print"      |"
          print"      |"
          print"      |"
          print"      |"
          print"======="
        if wrong==5:
          print"\n"
          print"  +---+"
          print"  |   |"
          print"  O   |"
          print"      |"
          print"      |"
          print"      |"
          print"======="
        if wrong==6:
          print"\n"
          print"  +---+"
          print"  |   |"
          print"  O   |"
          print"  |   |"
          print"      |"
          print"      |"
          print"======="
        if wrong==7:
          print"\n"
          print"  +---+"
          print"  |   |"
          print"  O   |"
          print" /|   |"
          print"      |"
          print"      |"
          print"======="
        if wrong==8:
          print"\n"
          print"  +---+"
          print"  |   |"
          print"  O   |"
          print" /|\  |"
          print"      |"
          print"      |"
          print"======="
        if wrong==9:
          print"\n"
          print"  +---+"
          print"  |   |"
          print"  O   |"
          print" /|\  |"
          print"  |   |"
          print"      |"
          print"======="
        if wrong==10:
          print"\n"
          print"  +---+"
          print"  |   |"
          print"  O   |"
          print" /|\  |"
          print"  |   |"
          print" /    |"
          print"======="
        if wrong==11:
          print"\n"
          print"  +---+"
          print"  |   |"
          print"  O   |"
          print" /|\  |"
          print"  |   |"
          print" / \  |"
          print"======="
        if turns == 0:           
            print "You Lose"
            print "The word was ", word
