import math
from matplotlib import pyplot as plt
with plt.style.context('dark_background'):
    plt.figure("Trig")

#Theta in radians
def terminalAngle(theta):
    s = theta%(2*math.pi)
    if 0<=s<math.pi/2:
        quadrant = 1

    if math.pi/2<=s<math.pi:
        quadrant = 2
        s = math.pi - s

    if math.pi<=s<math.pi*(3/2):
        quadrant = 3
        s = s - math.pi

    if math.pi*(3/2)<=s<2*math.pi:
        quadrant = 4
        s = 2*math.pi - s

    return s, quadrant

def estimateSin(terminal):
    if terminal<=math.pi/4:
        sin = terminal - terminal**3/6 + terminal**5/120
    else:
        f = (math.pi/2-terminal)
        sin = 1 - f**2/2 + f**4/24 - f**6/720
    return sin

def otherTrigFunctions(terminal, q):
    xSign, ySign = signs(q)
    sin = estimateSin(terminal)
    cos = (1-sin**2)**(.5)
    sin = ySign*sin
    cos = xSign*cos
    tan = sin/cos
    return sin, cos, tan
    
def signs(q):
    if q == 1:
        x, y = +1, +1
    if q == 2:
        x, y = -1, 1
    if q == 3: 
        x, y = -1, -1
    if q == 4:
        x, y = 1, -1
    return x,y


def graphUnitCircle():
    theta = 0
    while True:
        if theta>=math.pi*2:
            break
        else:
            terminal, q = terminalAngle(theta)
            sin, cos, tan = otherTrigFunctions(terminal, q)
            with plt.style.context('dark_background'):
                plt.scatter(cos, sin, color = 'red')
            theta+=.01

def specificAngle():
    unit = input("Units (d for degrees and r for radians): ")
    theta = float(input("Enter theta: "))
    if unit == "d":
        theta = theta*math.pi/180
    terminal, q = terminalAngle(theta)
    sin, cos, tan = otherTrigFunctions(terminal, q)

    with plt.style.context('dark_background'):
        plt.scatter(cos, sin, color = 'red')

    with plt.style.context('dark_background'):
        plt.plot((cos,0), (sin, 0), 'bo', linestyle="--", color = 'orange')
            
        plt.plot((cos,cos), (0, sin),'bo', linestyle="--", color = 'blue')

        plt.plot((0, cos),(sin, sin), 'bo', linestyle="--", color = 'blue')

        plt.axhline(0, color='white')
        plt.axvline(0, color='white')

        plt.title("Angle: "+str(round(theta,2))+" (Rad); Sin: "+str(round(sin,4))+"; Cos: "+str(round(cos,4))+"; Tan: "+str(round(tan,4)))

#function is either 1->'sin', 2->'cos', or 3->'tan'
def grapher(lowerEnd, upperEnd, function, nameOfFunction, Color = 'red'):
    pointer = lowerEnd
    xVals = []
    yVals = []
    while pointer<upperEnd:
        terminal, q = terminalAngle(pointer)
        vals = otherTrigFunctions(terminal, q)
        xVals.append(pointer)
        yVals.append(vals[function-1])
        pointer+=.01
    with plt.style.context('dark_background'):
        plt.plot(xVals, yVals, label = nameOfFunction, color = Color)
        plt.axhline(0, color='white')
        plt.axvline(0, color='white')
        plt.legend()


    
graphUnitCircle()
specificAngle()
plt.show()

with plt.style.context('dark_background'):
    plt.figure("Trig")
grapher(-1.5, 1.5, 3, 'Tan')
plt.show()

with plt.style.context('dark_background'):
    plt.figure("Trig")
grapher(-10, 10, 2, 'Cos', Color = 'yellow')
plt.show()

with plt.style.context('dark_background'):
    plt.figure("Trig")
grapher(-10, 10, 1, 'Sin', Color = 'green')
plt.show()


