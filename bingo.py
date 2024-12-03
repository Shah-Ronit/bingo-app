import turtle
import random

#First we will setup our main screen
screen = turtle.Screen()
screen.title("Bingo Game")
screen.bgcolor("Black")
screen.setup(width=1000, height=800)

#Then we initialize a turtle which will draw our grid
card_turtle = turtle.Turtle()
card_turtle.color("White")
card_turtle.penup()
card_turtle.hideturtle()
card_turtle.speed(0)

#This will draw the underline of our BINGO heading
card_turtle.goto(-130,275)
card_turtle.pendown()
card_turtle.goto(130,275)
card_turtle.penup()

#With this we will write the required text on our screen
card_turtle.goto(0, 270)
card_turtle.write("BINGO", align="center", font=("Georgia", 56, "bold"))

card_turtle.goto(-250, -270)
card_turtle.write("Player", align="center", font=("Georgia", 28, "normal"))

card_turtle.goto(250, -270)
card_turtle.write("Computer", align="center", font=("Georgia", 28, "normal"))

#Then we will initialize another turtle to write the drawn number as a text on our screen
drawn_num=turtle.Turtle()
drawn_num.color("White")
drawn_num.hideturtle()

#We will need another two turtles which will be used to update the bingo counter of our two grids
player_counter = turtle.Turtle()
player_counter.color("White")
player_counter.hideturtle()
player_counter.speed(0)
player_counter.penup()
player_counter.goto(-250,240)

computer_counter = turtle.Turtle()
computer_counter.color("White")
computer_counter.penup()
computer_counter.hideturtle()
computer_counter.speed(0)
computer_counter.goto(250,240)

#This will initialize the turtle required for slashing off the numbers that are drawn
slasher = turtle.Turtle()
slasher.color("white")
slasher.penup()
slasher.hideturtle()
slasher.speed(0)


#function required to continuously update the counter
def update_bingo_counter(turtle, count):
    turtle.clear()
    turtle.write(f"lines completed: {count}", align="center", font=("Arial", 16, "bold"))


#with this we will draw our two bingo grids
def draw_grid(x,y):
    card_turtle.goto(x, y)
    
    for i in range(6):
        card_turtle.pendown()
        card_turtle.forward(400)
        card_turtle.penup()
        card_turtle.backward(400)
        card_turtle.right(90)
        card_turtle.forward(80)
        card_turtle.left(90)
    card_turtle.goto(x, y)
    card_turtle.right(90)
    
    for i in range(6):
        card_turtle.pendown()
        card_turtle.forward(400)
        card_turtle.penup()
        card_turtle.backward(400)
        card_turtle.left(90)
        card_turtle.forward(80)
        card_turtle.right(90)


#with write_numbers func we will write random numbers in our grids
def write_numbers(numbers,x,y):
    
    for i in range(5):
        for j in range(5):
            card_turtle.goto(x + j * 80, y - i * 80)
            card_turtle.write(numbers[i][j], align="center", font=("Arial", 16, "normal"))


#this func will slash the numbers that are already drawn
def slash_number(x, y):
    
    slasher.penup()
    slasher.goto(x - 20, y + 20)
    slasher.pendown()
    slasher.goto(x + 20, y - 20)
    slasher.penup()
    slasher.goto(x + 20, y + 20)
    slasher.pendown()
    slasher.goto(x - 20, y - 20)


#this function will draw random numbers and call bingo_check everytime a number is drawn 
def draw_random_numbers():
    num = random.randint(1, 35)
    while num in drawn_numbers:
        num = random.randint(1, 35)
    drawn_numbers.add(num)
    print(f"Drawn number: {num}")
    
    drawn_num.clear()
    drawn_num.goto(0,0)
    drawn_num.write(num, align="center", font=("Arial", 16, "normal"))

    for i in range(5):
        for j in range(5):
            if card_numbers1[i][j] == num:
                slash_number(-410 + j * 80, 160 - i * 80)
            if card_numbers2[i][j] == num:
                slash_number(90 + j * 80, 160 - i * 80)
    
    if check_bingo(player_counter,card_numbers1, drawn_numbers, -410, 160) and check_bingo(computer_counter,card_numbers2, drawn_numbers, 90, 160):
        print("It's a tie")
        screen.ontimer(lambda: game_over("NO WINNER"), 3000)  # Delay of 3 seconds
    
    elif check_bingo(player_counter,card_numbers1, drawn_numbers, -410, 160):
        print("You won Bingo!")
        screen.ontimer(lambda: game_over("YOU WON"), 3000)  # Delay of 3 seconds
    
    elif check_bingo(computer_counter,card_numbers2, drawn_numbers, 90, 160):
        print("Computer won Bingo!")
        screen.ontimer(lambda: game_over("YOU LOST"), 3000)  # Delay of 3 seconds

#This function will create a list with nested list of random numbers as columns for our bingo card
def generate_card():
    card = []
    A=list(range(1,36))
    k=34
    for i in range(5):
        column=[]
        for j in range(5):
            index = random.randint(0,k)
            column.append(A[index])
            A.pop(index)
            k-=1
        card.append(column)  
    return card  


#This is our check_bingo func which checks if condition for bingo is met or not
def check_bingo(turtle,card, drawn_numbers,x,y):
    k=0
    i=0
    
    for row in card:
        if all(number in drawn_numbers for number in row):
            card_turtle.goto(x,y-i*80)
            card_turtle.pendown()
            card_turtle.goto(x+4*80,y-i*80)
            card_turtle.penup()
            
            k+=1
        i+=1
    i=0
    
    if(k==5):
        update_bingo_counter(turtle, k)
        return True
    
    for col in range(5):
        if all(row[col] in drawn_numbers for row in card):
            card_turtle.goto(x+i*80,y)
            card_turtle.pendown()
            card_turtle.goto(x+i*80,y-4*80)
            card_turtle.penup()
            k+=1
        i+=1
    
    if(k==5):
        update_bingo_counter(turtle, k)
        return True
    
    if all(card[i][i] in drawn_numbers for i in range(5)):
        card_turtle.goto(x,y)
        card_turtle.pendown()
        card_turtle.goto(x+4*80,y-4*80)
        card_turtle.penup()
        k+=1
    
    if(k==5):
        update_bingo_counter(turtle, k)
        return True
    
    if all(card[i][4 - i] in drawn_numbers for i in range(5)):
        card_turtle.goto(x+4*80,y)
        card_turtle.pendown()
        card_turtle.goto(x,y-4*80)
        card_turtle.penup()
        k+=1
    
    if(k!=5):
        update_bingo_counter(turtle, k)

    elif(k>=5):
        update_bingo_counter(turtle, k)
        return True
    
    return False

#With this function we create our game over animation
def game_over(winner_text):
    card_turtle.clear()
    slasher.clear()
    drawn_num.clear()
    player_counter.clear()
    computer_counter.clear()
    
    screen.bgcolor("gold")
    
    font_style = ("Arial", 56, "bold")
    card_turtle.goto(0, 0)
    
    for i in range(10):
        
        card_turtle.color("red" if i % 2 == 0 else "white")
        
        card_turtle.write(winner_text, align="center", font=font_style)
        
        screen.bgcolor("white" if i % 2 == 0 else "gold")
        
        screen.update()
        turtle.time.sleep(0.3)  

    screen.bgcolor("gold")
    card_turtle.color("dark green")
    card_turtle.write(winner_text + "!", align="center", font=("Arial", 56, "bold"))
    
    turtle.time.sleep(3)
    screen.bye()  

#here we create all neccessary variables and call required function
card_numbers1 = generate_card()
card_numbers2 = generate_card()
draw_grid(-450, 200)

card_turtle.left(90)

draw_grid(50,200)
write_numbers(card_numbers1, -410, 150)
write_numbers(card_numbers2, 90, 150)

drawn_numbers = set()

#this is our main game loop which keeps the game going until it is over
def bingo_game_loop():
    screen.listen()
    screen.onkey(draw_random_numbers, "space")
    screen.mainloop()

bingo_game_loop()