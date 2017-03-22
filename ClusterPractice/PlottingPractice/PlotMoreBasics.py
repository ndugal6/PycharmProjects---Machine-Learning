import matplotlib.pyplot as plt
radius = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
area = [3.14159, 12.56636, 28.27431, 50.26544, 78.53975, 113.09724]
plt.plot(radius, area, marker='o', label='Circle')
plt.xlabel('Radius/Side')
plt.ylabel('Area')
plt.title('Area of Shapes')


#Comparing the area of circle vs radius to the area of a square vs it's side
square = [1.0,4.0,9.0,16.0,25.0,36.0]
#plot in red with dots for each point, and a dashed line connecting them
plt.plot(radius, square, marker='s', linestyle='--', color='r', label='Square')
            #COLOR CODES: r - red | b - blue | g - green | c - cyan | m - magenta | y - yellow | k - black | w - white
            #MARKER CODE: + plut sign | . Dot | o Circle | * Star | p Pentagon | s square | x X char | D diamond | h Hexagon | ^ Triangle
            #LINESTYLE CODE: - Solid | -- Dashed | : Dotted | -. Dash-Dotted | None None
#We add labels to the two plot calls in order to call the legend function which draws a legend
plt.legend()
plt.show()


