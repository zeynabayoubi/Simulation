import turtle as t

def Drawing_the_triangle(points,color,t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0],points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0],points[1][1])
    t.goto(points[2][0],points[2][1])
    t.goto(points[0][0],points[0][1])
    t.end_fill()

def middle_of_points(point1,point2):
    return ( (point1[0]+point2[0]) / 2 , (point1[1] + point2[1]) / 2 )

def Drawing_the_sierpinski(points , step , t):
    
    colormap = ['blue','red','green','white','yellow','violet','orange']
    
    Drawing_the_triangle(points , colormap[step] , t)
    
    if step > 0:
        Drawing_the_sierpinski( [points[0] , middle_of_points( points[0], points[1] ) , middle_of_points(points[0], points[2])] , step-1 , t )
        
        Drawing_the_sierpinski( [points[1] , middle_of_points( points[0], points[1] ) , middle_of_points(points[1], points[2])] , step-1 , t )
        
        Drawing_the_sierpinski( [points[2] , middle_of_points( points[2], points[1] ) , middle_of_points(points[0], points[2])] , step-1 , t )

#main code:

number_of_steps = int(input("Enter the number of steps: "))        
t = t.Turtle()
corners = [[-200,-100],[0,200],[200,-100]]
Drawing_the_sierpinski(corners,number_of_steps,t)

