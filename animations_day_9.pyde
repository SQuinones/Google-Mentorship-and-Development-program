face = {}


def setup():
    size(400,400)
    face['eye_size'] = 30
    makeSmileyFace()
 
def makeSmileyFace():
    fill(255,255,0)
    ellipse(200,200,200,200)
    fill(255)
    ellipse(160,160,20,50)
    ellipse(240,160,20,50)
    fill(0)
    ellipse(160,170,10,10)
    ellipse(240,170,10,10)
    noFill()
    arc(160,200, 200, 50, 0, PI / 2.0)
