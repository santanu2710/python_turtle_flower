import turtle
 
# Set initial position

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("white")
s.title("flower")

col = ["red", "yellow", "gold", "green", "lime", "dark green", "purple"]


# making the leafs

t.color(col[4])
t.speed(20)

for i in range(4):
    t.goto(0,-22.5*(2*i))       # location for the leaf
    
    t.begin_fill()
    t.circle(100, 60)
    t.left(120)                      ## making the right side leaf using this block of code
    t.circle(100,60)
    t.end_fill()

    t.right(60)

    t.goto(0,-22.5*(2*i+1))     # location for the leaf
    
    t.begin_fill()
    t.circle(-100,60)
    t.right(120)                      ## making the left side leaf using this block of code
    t.circle(-100, 60)
    t.end_fill()
    
    t.left(60)


# Making the stick

t.color(col[5])
t.goto(0, -300)
t.left(90)                           # pen setup

t.pensize(7)
t.goto(0,150)                        # draw the stick


# making the petal of the flower

t.color(col[3])
t.pensize(0)
t.right(90)


for i in range(12):
    t.begin_fill()
    t.circle(200,20)
    t.left(160)
    t.circle(200,20)
    t.end_fill()
    t.left(10)




# Flower part

t.color(col[0])
t.left(30)


for j in range(50):
    
    if j<10:                                                   # col = ["red", "yellow", "gold", "green", "lime", "dark green", "purple"]
        t.color(col[4])                                        #          0       1        2        3        4         5            6
    elif j>=10 and j<27:
        t.color(col[0])
    else:
        t.color(col[6])
    
    for i in range(6):
        t.circle(2+(j*5), 60)
        t.left(120)
        t.circle(2+(j*5), 60)
        t.left(180)


                          # not a good looking flower

# for i in range(60):
#     t.left(6)
#     t.circle(100)
 
 
# t.color(col[1])   
# for i in range(90):
#     t.left(4)
#     t.circle(70)

t.color(col[2])
t.right(120)
t.goto(0, 135)
t.left(90)
t.begin_fill()
t.circle(15)
t.end_fill()



s.mainloop()