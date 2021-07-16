a= 0 
b= 0
c= 0
lineWidth = 1

def setup():
    size(800, 650)
    background(255)
    
    
def draw():
    stroke(a,b,c)
    strokeWeight(lineWidth)
    if (mousePressed and mouseY < height-50) :
        line(pmouseX, pmouseY, mouseX, mouseY)
    drawControls()
    chooseColor()
    lineSize()
    eraseDraw()

def eraseDraw():
    global a, b, c
    fill(255, 255, 255)
    rect (550, height-50, 250, 50)  
    fill(0)
    textSize(20)
    text("ERASE", 670, height-25)

        
def lineSize():
    global lineWidth
    ellipse(400,height-25, 50, 50) 
    ellipse(460,height-25, 25, 25)
    ellipse(490,height-25, 8, 8)
    ellipse(510,height-25, 2, 2)
    
    if mousePressed and mouseX > 400 -10 and mouseX < 400 + 10 and mouseY > height-50 :
        lineWidth = 50
    if mousePressed and mouseX > 460 -10 and mouseX < 460 + 10 and mouseY > height-50 :
        lineWidth = 25
    if mousePressed and mouseX > 490 -10 and mouseX < 490 + 10 and mouseY > height-50 :
        lineWidth = 8
    if mousePressed and mouseX > 510 -10 and mouseX < 510 + 10 and mouseY > height-50 :
        lineWidth = 1
        
        
def chooseColor():
    global a, b, c
    if mousePressed and mouseX < 50 and mouseY > height-50 :
        #yellow
        a= 255
        b = 255
        c = 0
    if mousePressed and mouseX > 50 and mouseX < 100 and mouseY > height-50 :
        #blue
        a= 0
        b = 57
        c = 230
    if mousePressed and mouseX > 100 and mouseX < 150 and mouseY > height-50 :
        #red
        a= 255
        b = 0
        c = 0
    if mousePressed and mouseX > 150 and mouseX < 200 and mouseY > height-50 :
        #green
        a= 0
        b = 128
        c = 32
    if mousePressed and mouseX > 200 and mouseX < 250 and mouseY > height-50 :
        #black
        a= 26
        b = 26
        c = 26
    if mousePressed and mouseX > 250 and mouseX < 300 and mouseY > height-50 :
        #white
        a= random(255)
        b = random(255)
        c = random(255)
    if mousePressed and mouseX >300 and mouseX < 400 and mouseY > height-50 :
        #pink
        a= 255
        b = 0
        c = 255
    #erase
    if mousePressed and mouseX > 550 and mouseX < 800 and mouseY > height-50:
        a= 255
        b=255
        c=255
            
def drawControls():
    strokeWeight(3)
    line(0, height-50, width, height-50)
    stroke(0)
    strokeWeight(1)
    fill(255, 255, 0)#yellow
    rect(0, height-50, 50, 50)
    fill(0, 57, 230)#blue
    rect(50, height-50, 50, 50)
    fill(255, 0, 0)#red
    rect(100, height-50, 50, 50)
    fill(0, 128, 32)#green
    rect(150, height-50, 50, 50)
    fill(26, 26, 26)#black
    rect(200, height-50, 50, 50)
    fill(255, 255, 255)# white
    rect(250, height-50, 50, 50)
    fill(255, 0, 255)#pink
    rect(300, height-50, 50, 50)
    textSize(32)
    fill(0)
    text("?",268,height-14)

# def keyPressed():
#     global lineWidth
#     if key == '+' or keyCode == UP:
#             lineWidth += 1
#     if key == '-' or keyCode == DOWN:
#             lineWidth -= 1#lineWidth = lineWidth - 1 
#     if lineWidth < 0:
#         lineWidth = 0 
        
