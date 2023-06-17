from turtle import Turtle,Screen
from random import randint

colors = ["violet","blue","green","yellow","orange","red"]
y_pos = [-70,-30,10,50,90,130]
turtle_list = []

screen =Screen()
screen.setup(width=500,height=600)
user_guess = screen.textinput(title="Make your bet",prompt="Which turtle will win? Make a guess ").lower()


for i in range(6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.setpos(x=-230,y=y_pos[i])
    turtle_list.append(new_turtle)

if user_guess:
    is_race_on = True

while(is_race_on):

    for turtle in turtle_list:
        
        if turtle.xcor() >=230:
            is_race_on =False
            win_color = turtle.pencolor()
            if win_color == user_guess:
                print(f"You won!! {win_color} won the race.")
            else:
                print(f"You lose!! {win_color} won the race.")
        forward_rand = randint(1,10)
        turtle.forward(forward_rand)



screen.exitonclick()