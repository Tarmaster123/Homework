import turtle as t

t.clear()
t.speed(20)

d=0

def tri():
    t.rt(30)
    t.fd(20)
    for j in range(2):
        t.lt(120)
        t.fd(20)

def antigen():
    t.fd(20)
    tri()

t.circle(100)
for i in range (18):
    t.pu()
    t.goto(0,100)
    t.setheading(0)
    t.lt(d)
    t.fd(100)
    t.pd()
    antigen()
    d+=20   
    


