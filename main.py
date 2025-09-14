from turtle import Turtle,Screen 
import time 
import random 

window=Screen ()
window.setup(400,400)
window.bgcolor("black")
angle=[90,180,270,0,360]
colors=["blue","red","purple","cyan","pink","yellow","DarkGray"]

class Snake :
  def __init__(self):
    self.position=[(-40,0),(-20,0),(0,0),(20,0)]
    self.turtles=[]
    self.create_snake()    
    self.direction=90
    
  def create_snake(self):
    for i in range(len(self.position)): 
      new_turtle=Turtle()
      new_turtle.shape("square")
      new_turtle.color("white")
      new_turtle.penup()
      self.turtles.append(new_turtle)   
      self.turtles[i].goto(self.position[i])
      
  def create_body(self):
      new_turtle=Turtle("square")
      new_turtle.penup()
      new_turtle.color("white")
      self.turtles.insert(0,new_turtle)  
      
  def move(self):    
      for x in range(len(self.turtles)-1):
        self.turtles[x].goto(self.turtles[x+1].pos())
      self.turtles[-1].setheading(self.direction)
      self.turtles[-1].forward(20)
  def change_direction(self, x, y):
    head_x, head_y = self.turtles[-1].pos()
    dx = x - head_x
    dy = y - head_y

    if abs(dx) > abs(dy):  
        new_direction = 0 if dx > 0 else 180  
    else:  
        new_direction = 90 if dy > 0 else 270  

    if (self.direction == 0 and new_direction != 180) or \
       (self.direction == 180 and new_direction != 0) or \
       (self.direction == 90 and new_direction != 270) or \
       (self.direction == 270 and new_direction != 90):
        self.direction = new_direction 
#  def change_direction(self, x, y):

#        head_x, head_y = self.turtles[-1].pos()
#        dx = x - head_x
#        dy = y - head_y
#        
#        if abs(dx) > abs(dy):  
#            self.direction = 0 if dx > 0 else 180          
#        else:  
#            self.direction = 90  
#        opposite_directions = {0: 180, 180: 0, 90: 270, 270: 90}
#        if abs(dx) > abs(dy):  
#           new_direction = 0 if dx > 0 else 180  
#        else:  
#           new_direction = 90 if dy > 0 else 270
#        if new_direction != opposite_directions[self.direction]:
#          
#           self.direction = new_direction

 
class Food(Turtle):
  def __init__(self):
    super().__init__()
    global randomx,randomy
    randomx= random.randint(-180,180)
    randomy=random.randint(-180,180)
    self.appear(randomx,randomy)
    
  def appear (self,randomx,randomy):
    self.shape("circle")
    self.color("red")
    self.penup()
    self.shapesize(0.5,0.5)
    #randomx= random.randint(-180,180)
#    randomy=random.randint(-180,180)
    self.goto(randomx,randomy)
    position=self.goto(randomx,randomy) 
    
  def disappear(self,randomx,randomy):
    self.hideturtle()
    self.goto(random.randint(-180,180),random.randint(-180,180))
    self.showturtle()
    
class Screen_board(Turtle):
    def __init__(self):
      super().__init__()
      self.color("white")
      self.hideturtle()
      self.penup()
      self.score=0
      self.goto(0,700)
      self.write_score()
      
    def write_score (self): 
      self.write(f"score : {self.score}", align="center", font=("arial",6,"normal"))
      
    def update_screen (self):
       self.clear()
       self.score+=1
       self.write_score()
    
    def game_over(self):
       self.goto(0,0)
       self.write(f"             GAME OVER \nyour maximum score is : {self.score}",align="center",font=("arial",6,"normal"))
       

window.tracer(0)

mon= Snake()
food=Food()
score= Screen_board()

window.onclick(mon.change_direction)
game_on=True
while game_on:
  
  mon.move()
  time.sleep(0.1);
  window.update()
  if mon.turtles[-1]. distance (food) <15:
      food.disappear(randomx,randomy)
      mon.create_body()
      score.update_screen()
  if mon.turtles[-1].xcor()>320 or mon.turtles[-1].xcor()<-320 or mon.turtles[-1].ycor()>720 or mon.turtles[-1].ycor()<-720:
    window.bgcolor("dark red")
    score.game_over()
    game_on=False 
  for i in mon.turtles[:-1]:
    if mon.turtles[-1].distance(i) <10:
      window.bgcolor("dark red")
      score.game_over()
      game_on=False  
  
window.exitonclick()
