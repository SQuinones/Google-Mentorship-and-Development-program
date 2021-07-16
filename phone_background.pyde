#phone backgrounds

size(700, 900)
background(0)
# img = loadImage('https://www.pngkey.com/png/full/170-1706944_our-mission-cartoon-earth-transparent-background.png')
img = loadImage('https://c.tadst.com/gfx/600x337/full-moon.png?1')
img.resize(0,100)

x = 0
y = 0


while y < height:
    while x < width:
        image(img, x, y)
        x = x + 100
        
    x = 0    
    y = y + 100  
    
      









    
