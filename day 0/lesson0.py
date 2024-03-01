from turtle import

#we want to paint a house

#step 1: draw a square
speed(15)
width(7)

color("purple")
      
forward(200)
left(90)

foarward(200)
left(90)

foarward(200)
left(90)

foarward(200)
left(90)
#end of square

#drawing a door

forword(70) 
color("yellow")
left(90)

forward(120)  #height of the door
right(90)

forward(60)
right(90)

forward(120)

penup()
goto(200,200)
pendown()

color("black")
begin fill()
right(150)
forward(200)  
left(120)
forward(200)
end (fill)

exitnclick()