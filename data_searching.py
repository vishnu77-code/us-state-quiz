import pandas
from main import *
data=pandas.read_csv("C:/Users/ENFRAS/Downloads/us-states-game-start/us-states-game-start/50_states.csv")
k=data.state
print(list(k))
l=0
no=0
scrn=scr()
while no<5:


    def func():
        exit()


    guess_state = (screen.textinput(f"founded us states{l}/{50}", prompt="type the states of usa")).title()
    print(guess_state)
    j = data[k == guess_state]
    no += 1


    for i in k:

      if guess_state==i:

          get_x = int(j.x)
          get_y = int(j.y)
          scr.state_turtle(get_x,get_y,guess_state)
          print("yes")

          l+=1

      if guess_state=="exit":
          screen.exitonclick()






screen.exitonclick()
