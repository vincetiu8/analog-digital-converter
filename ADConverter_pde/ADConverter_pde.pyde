yPos = []
global bitDepth
global bitRate
prevYPos = 0
global yoff
global overRate
global overDepth
global locked

def setup():
 global bitRate
 global bitDepth
 global yoff
 bitRate = 100
 bitDepth = 40
 yoff = 0
 size(800, 800)
 count = 0
 while (count < 800):
     yPos.append(0)
     count += 1

def draw():
  global overRate
  global overDepth
  global locked
  global bitRate
  global bitDepth
  textAlign(CENTER)
  textSize(32)
  background(0)
  stroke(255)
  line(0, 300, 800, 300)
  line(0, 500, 800, 500)
  line(200, 350, 200, 450)
  posx = 200
  posy = 350 + bitRate / 2
  if (dist(mouseX, mouseY, posx, posy) < 20):
    fill(200)
    overRate = True
    if (mousePressed):
        locked = True
        yoff = mouseY - 350 - bitRate / 2
  
  else:
   fill(255)
   overRate = False
   
  circle(posx, posy, 20)
  textSize(20)
  text("Sample Rate", 100, 375)
  text(800 / bitRate, 100, 425)
  
  line(600, 350, 600, 450)
  posx = 600
  posy = 350 + bitDepth / 4 * 5
  if (dist(mouseX, mouseY, posx, posy) < 20):
    fill(200)
    overDepth = True
    if (mousePressed):
        locked = True
        yoff = mouseY - 350 - bitDepth / 4 * 5
  
  else:
   fill(255)
   overDepth = False
   
  circle(posx, posy, 20)
  text("Sample Depth", 700, 375)
  text(300 / bitDepth, 700, 425)
  
  fill(255)
  textSize(40)
  text("Analog Input", 400, 350)
  text("Digital Output", 400, 475)
 
  noStroke()
  for count, y in enumerate(yPos):
   circle(count, y, 5)
  
  average = 0
  for index, val in enumerate(yPos):
    average += val
    if (index % bitRate == bitRate - 1):
        average /= bitRate
        average = bitDepth * round(average / bitDepth)
        circle(index - bitRate / 2, average + 500, 5)
        if (index - bitRate * 2 + 1 >= 0):
            stroke(255)
            line(index - bitRate / 2 * 3, prevYPos + 500, index - bitRate / 2, average + 500)
        prevYPos = average
        average = 0

def mouseDragged():
  global overRate
  global overDepth
  global locked
  global yoff
  global bitRate
  global bitDepth
  print(overRate)
  if (mouseY < 300 and mouseX > -1 and mouseX < 800):
   yPos[mouseX] = mouseY
  
  elif overRate and locked:
    print(222)
    bitRate = (mouseY - yoff - 350) * 2
    if (bitRate < 1):
      bitRate = 1
    elif (bitRate > 200):
      bitRate = 200
  
  elif overDepth and locked:
    bitDepth = (mouseY - yoff - 350) * 4 / 5
    if (bitDepth < 1):
      bitDepth = 1
    elif (bitDepth > 80):
      bitDepth = 80

def mouseReleased():
  locked = False
