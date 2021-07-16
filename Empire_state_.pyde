
squareSize = 10
startX = 0
startY = 0

def setup():
    size(1500, 1500)
    background(128, 128, 128)

    
def draw():
  background(0,0,0)
  
  empire_Shape()
  star_Shape()
  top()
  empire_State()
  

  


    
def star():  
  fill(255, 255, 0)
  stroke(255)
  strokeWeight(2)
  beginShape();
  vertex(startX + squareSize * 0, startY + squareSize * (-5))
  vertex(startX + squareSize * 1.4, startY + squareSize * (-2))
  vertex(startX + squareSize * 4.7, startY + squareSize * (-1.5))
  vertex(startX + squareSize * 2.3, startY + squareSize * 0.7)
  vertex(startX + squareSize * 2.9, startY + squareSize * 4)
  vertex(startX + squareSize * 0, startY + squareSize * 2.5)
  vertex(startX + squareSize * (-2.9), startY + squareSize * 4)
  vertex(startX + squareSize * (-2.3), startY + squareSize * 0.7)
  vertex(startX + squareSize * (-4.7), startY + squareSize * (-1.5))
  vertex(startX + squareSize * (-1.4), startY + squareSize * (-2))
  endShape(CLOSE)
    
def empire_State():
  stroke(255);
  strokeWeight(2)
 
  fill(153, 153, 153) 
  rect(startX + squareSize * 4, startY + squareSize * 35, squareSize * 10.5, squareSize * 1.5) #base 
  rect(startX + squareSize * 5.7, startY + squareSize * 29, squareSize * 7.1, squareSize * 6)
  fill(0, 153, 204)
  rect(startX + squareSize * 8, startY + squareSize * 20 , squareSize * 2.5, squareSize * 9)
  fill(153, 153, 153)
  rect(startX + squareSize * 7, startY + squareSize * 23, squareSize * 1.4, squareSize * 12)
  rect(startX + squareSize * 10, startY + squareSize * 23, squareSize * 1.4, squareSize * 12)
  rect(startX + squareSize * 5.7, startY + squareSize * 31, squareSize * 2, squareSize * 4)
  rect(startX + squareSize * 10.8, startY + squareSize * 31, squareSize * 2, squareSize * 4)
  fill(0, 153, 204)
  rect(startX + squareSize * 4.7, startY + squareSize * 32, squareSize * 1, squareSize * 3)
  rect(startX + squareSize * 12.8, startY + squareSize * 32, squareSize * 1, squareSize * 3)
  fill(153, 153, 153)
  rect(startX + squareSize * 7, startY + squareSize * 21.5, squareSize * 1.4, squareSize * 1.8)
  rect(startX + squareSize * 10, startY + squareSize * 21.5, squareSize * 1.4, squareSize * 1.8)
  
def top():

  fill(random(255), random(255), random(255))  
  rect(startX + squareSize * 8.3, startY + squareSize * 19.5, squareSize * 1.8, squareSize * 0.5)
  rect(startX + squareSize * 8.6, startY + squareSize * 19.2, squareSize * 1.3, squareSize * 0.3)
  rect(startX + squareSize * 8.8, startY + squareSize * 18.9, squareSize * 0.9, squareSize * 0.3)
  rect(startX + squareSize * 9, startY + squareSize * 18.4, squareSize * 0.5, squareSize * 0.5)
  rect(startX + squareSize * 9.1, startY + squareSize * 16.4, squareSize * 0.3, squareSize * 2)
  delay(500)
    
def keyPressed():
    global squareSize
    squareSize = squareSize * 1.5
    
            
def empire_Shape():
      if key == 'a' :
        top()
        empire_State()
        
def star_Shape():
    if key == 'e':  
        star()   
    
    
def mouseWheel(event):
    global squareSize
    squareSize = squareSize / 1.5
    

    
def mousePressed():
    
    global squareSize
    squareSize = 15
    global startX, startY
    startX = mouseX
    startY = mouseY
    # star()
