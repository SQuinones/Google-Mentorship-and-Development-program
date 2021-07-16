LrectY = 350 #initial left paddle position
RrectY = 350

X = 700/2 # initial ball value
Y = 700/2

moveRight = True #this means move left is false 
moveDown = True

speedX = 3
speedY = 3

countR = 0 #score for right size
countL = 0 # score for left size


def setup():
    global font
    size(700,700)
    background(255)
    font = loadFont("Monospaced-48.vlw")
    
    
def draw():
    background(255)
    global LrectY, RrectY,X,Y,moveRight
    global moveDown,speedX,speedY,countR, countL,font
    textFont(font)
    drawTable()
    drawBall()
    drawPaddles()

    if keyPressed == True and keyCode == UP:
        LrectY = LrectY - 6
        speedSide = 1
    
    if keyPressed == True and keyCode == DOWN:
        LrectY = LrectY + 6
        speedSide = 1
        
    if keyPressed == True and key == 'a':
        RrectY = RrectY - 6
        speedSide = 1

    if keyPressed == True and key == 'z':
        RrectY = RrectY + 6
        speedSide = 1
        
        
    if moveRight == True:
        X = X + speedX
        
    else:
        X = X - speedX
    
    if moveDown == True:
        Y = Y + speedY
        
    else:
        Y = Y - speedY
        
        
    if Y <= 10:
        moveDown = True
        speedSide = random(1,3)
        
    if Y >= 690:
        moveDown = False
        speedSide = random(1,3)
        
    if X >= 690:
        countL = countL + 1
        X = 700/2
        Y = 700/2 #restablece the elpise in the center    
    
        
    if X <= 10:
        countR = countR + 1
        X = 700/2
        Y = 700/2
            
    if X >= 615 and Y > RrectY and Y < (RrectY + 100): # contact ball with paddle 
         moveRight = False
    
    if X <= 75 and Y > LrectY and Y < (LrectY + 100):
         moveRight = True
         speedSide = random(1,3)
    
        
    if X >= 690:
        moveRight = False
        speedSide = random(1,3)
        
    if X <= 10:
        moveRight = True
        speedSide = random(1,3)
        
        
def drawBall():
    global X, Y    
    fill(255, 0, 0)
    ellipse(X, Y, 50, 50)
    text("Score", 300, 40) 
    
def drawPaddles():
    global LrectY, countL, RrectY,countR
    
    fill(255, 102, 0)
    rect(10, LrectY, 30, 120)
    text(countL, 200, 50)
    
    fill(0,0,255)
    rect(660, RrectY, 30, 120)
    text(countR, 500, 50)
    
                                        
def drawTable():
    fill(255, 0, 0)
    circle(350, 350, 100)
    fill(255, 255, 255)
    circle(350, 350, 90)
    fill(255, 0, 0)
    circle(350, 350, 10)
    rect(350,60, 2, 240)
    rect(350, 395,2, 290)   
 

    
        
