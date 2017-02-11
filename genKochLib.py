import turtle as t

class Snowflake:

    nSides = 0 # number of sides of the polygon
    nIterations = 0 # number of wanted iterations
    side = 0 # length of the sides
    drawer = t.Turtle() # turtle to draw the figure
    
    # utils for graphical reasons
    angle = 0 # internal angle
    
    # ctor, takes as arguments
    #   ns = number of sides
    #   nit = number of iterations
    #   X = tuple (x,y) for the starting point
    def __init__(self, ns, nit, l, X):
        self.nSides = ns
        self.nIterations = nit
        self.side = l*1.0
        self.angle = (ns-2)*180.0/ns
        self.drawer.ht()
        self.drawer.pu()
        self.drawer.goto(X[0],X[1])
        self.drawer.pd()

    # draws one side of the wanted figure
    #   as a perfect polygon (so no iterations)
    #   l is the side length
    def ds(self, l):
        self.drawer.fd(l)
        self.drawer.lt(self.angle)
        
    # draws a "dented" side, i.e. a side with a certain 
    #   number of external bumps
    #   ni is the iteration number
    #   l is the side length  
    #   control is needed for the iterative process, 
    #       sometimes a right turn is needed at the end of a side
    def dd(self, ni, l, control=True):
        if ni==0:
            self.drawer.fd(l)
        else:
            self.dd(ni-1,l/self.nSides)
            for i in range(self.nSides-2):
                if i%2==0: # out bump
                    self.drawer.rt(self.angle)
                    for k in range(self.nSides-1):
                        self.dd(ni-1,l/self.nSides)
                        self.drawer.lt(180-self.angle)
                    self.drawer.rt(180)
                else: # in bump
                    self.drawer.lt(self.angle)
                    for k in range(self.nSides-1):
                        self.dd(ni-1,l/self.nSides,False)
                        self.drawer.rt(180-self.angle)
                    self.drawer.rt(180)       
            self.dd(ni-1,l/self.nSides)    

    # draws the snowflake
    def draw(self):
        for j in range(self.nSides):
            self.dd(self.nIterations,self.side)
            self.drawer.lt(180-self.angle)
        
        
        
        
        
        
