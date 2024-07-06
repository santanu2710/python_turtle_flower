import turtle

pen = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
s.title("flower")

number_of_petal = 12                        # change the number of petals accordoing to your choice

pen.speed(20)

def fun(angle_ofleaf, r):
    pen.left(angle_ofleaf)
    pen.circle(200-r,90)
    pen.left(90)
    pen.circle(200-r,90)                    # function to draw a single petal
    

pen.penup()
pen.goto(300,-300)
pen.pendown()    
pen.left(90)
pen.color("green")
pen.pensize(15)
pen.circle(300,90)                          # drawing the green stick of the flower


col = ["pink", "red", "purple", "cyan", "violet", "gold"]

pen.pensize(1)
for i in range(16):    
    for j in range(number_of_petal):
        pen.color(col[j%6])
             
        fun(360/number_of_petal, i*5)
        pen.left(90)
        
    
turtle.done()