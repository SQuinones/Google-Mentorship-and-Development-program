def setup():
    size(1000, 1000)

    
def draw():
    img = loadImage('stephany.jpg')
    x = width
    y = height
    image(img, 0, 0, x, y)
    #image(img, 0, 0, 1000, 1000)
      
      
    loadPixels()
    
    for i in range(len(pixels)):
        Photo = pixels[i]

        r = red(Photo)
        g = green(Photo)
        b = blue(Photo)
        avg =(red(Photo) + green(Photo) + blue(Photo))/3
        pixels[i] = color(r,g,b)# normal color
        #pixels[i] = color(g,b,r)
        #pixels[i] = color(avg)#black and white filter
    
    updatePixels()



#
