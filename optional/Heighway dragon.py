import turtle

def heighway_dragon(N,L):   

    t = turtle.Turtle()
    t.hideturtle()


    move = [1]
    for i in range(N):
        walks = [-x for x in move]
        walks.reverse()
        walks = [1] + walks
        for j in walks:
            t.right(90*j)
            t.forward(L)
        move += walks


N = int(input('Enter the number of steps : '))
L = int(input('Enter the length of each segment : '))
heighway_dragon(N,L)

