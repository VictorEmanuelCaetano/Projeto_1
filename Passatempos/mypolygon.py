import turtle
import math
bob = turtle.Turtle()
julio = turtle.Turtle()
def square(t, lenght):
    for i in range(4):
        t.fd(lenght)
        t.lt(90)    
def polygon(t, lenght, n, angle):
    for i in range(n):
        t.fd(lenght)
        t.lt(angle / n)
        
def circle(t, r, angle):
    n = 100
    circuferencia = 2 * math.pi * r 
    comprimento = circuferencia * (angle / 360)
    lado = comprimento / n
    polygon(julio, lado, n, 30)


circle(julio, 30, 360)

square(bob, 10)
turtle.mainloop()