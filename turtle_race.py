import turtle
import random
screen = turtle.Screen()
def new_line():
    timmy =turtle.Turtle()
    timmy.teleport(x=230,y=160)
    timmy.setheading(270)
    timmy.forward(300)
    timmy.hideturtle()

new_line()

color_list = ['red', 'orange', 'black', 'green', 'blue', 'indigo', 'violet']
players = ['tim1','tim2','tim3','tim4','tim5','tim6','tim7']
speed_list = [5,10,15,20,25,30,35]
is_race_on = False
turtles = []
screen.setup(width=500,height=400)
i = -100
for name in players:
    player = turtle.Turtle()
    player.shape('turtle')
    player.penup()
    color = random.choice(color_list)
    player.color(color)
    player.goto(x=-230,y = i)
    speed = random.choice(speed_list)
    color_list.remove(color)
    player.speed(speed)
    speed_list.remove(speed)
    i += 40
    turtles.append(player)


user_bet = screen.textinput("Make Your Bet","Which turtle will win the race? Enter the color")
if user_bet:
    is_race_on = True

while is_race_on:
    for tut in turtles:
        if tut.xcor()>=215:
            is_race_on = False
            winning = tut.pencolor()
            print(winning)
            if user_bet == winning:
                print(f"You have won! The {winning} turtle is the winner!")
            else:
                print(f"You have lost! The {winning} turtle is the winner!")
            break
        dis = random.randint(1,10)
        tut.forward(dis)
        
    
screen.exitonclick()
