import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

# adding image to the background
IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# getting data from the csv file
data = pandas.read_csv("50_states.csv")
state = data["state"]
x_cor = data["x"]
y_cor = data["y"]
state_list = pandas.Series.to_list(state)
x_cor_list = pandas.Series.to_list(x_cor)
y_cor_list = pandas.Series.to_list(y_cor)

# initializing the game variables
score = 0


while score < len(state_list):
    if score == 0:
        user_answer = screen.textinput(title=f"Guess the states", prompt="Enter a state name").title()
    else:
        user_answer = screen.textinput(title=f"{score}/50 answered right", prompt="What's another state name?").title()

    if user_answer in state_list:
        index = state_list.index(user_answer)
        writer.goto(x_cor_list[index], y_cor_list[index])
        writer.write(user_answer)
        score += 1

writer.goto(0,0)
writer.write("You Won!!", align="Center", font= ("Arial", 30, "normal"))


turtle.mainloop()
