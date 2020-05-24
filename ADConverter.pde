int[] yPos = new int[800];
int bitDepth = 40;
int bitRate = 100;
int prevYPos = 0, yoff;
boolean overRate, overDepth, locked;

void setup() {
 size(800, 800);
}

void draw() {
  textAlign(CENTER);
  textSize(32);
  background(0);
  stroke(255);
  line(0, 300, 800, 300);
  line(0, 500, 800, 500);
  line(200, 350, 200, 450);
  int posx = 200, posy = 350 + bitRate / 2;
  if (dist(mouseX, mouseY, posx, posy) < 20) {
    fill(200);
    overRate = true;
  }
  
  else {
   fill(255);
   overRate = false;
  }
  circle(posx, posy, 20);
  text("Sample Rate", 100, 375);
  text(Math.round(800f / bitRate), 100, 425);
  
  line(600, 350, 600, 450);
  posx = 600;
  posy = 350 + bitDepth / 4 * 5;
  if (dist(mouseX, mouseY, posx, posy) < 20) {
    fill(200);
    overDepth = true;
  }
  
  else {
   fill(255);
   overDepth = false;
  }
  circle(posx, posy, 20);
  text("Sample Depth", 700, 375);
  text(Math.round(300f / bitDepth), 700, 425);
  
  fill(255);
  text("Analog Input", 400, 340);
  text("Digital Output", 400, 475);
 
  noStroke();
  for (int i = 0; i < yPos.length; i++) {
   circle(i, yPos[i], 5); 
  }
  
  for (int i = 0; i < yPos.length; i += bitRate) {
    int average = 0;
    for (int j = i; j < i + bitRate; j++) {
      if (j < 800) {
       average += yPos[j];  
      }
    }
    average /= bitRate;
    int newYPos = bitDepth * Math.round(average / bitDepth) + 500;
    if (i > 0) {
      stroke(255);
      line(i - bitRate / 2, prevYPos, i + bitRate / 2, newYPos);
    }
    noStroke();
    circle(i + bitRate / 2, newYPos, 5);
    prevYPos = newYPos;
  }
}

void mousePressed() {
  if (overRate) {
    locked = true;
    yoff = mouseY - 350 - bitRate / 2;
    println(yoff);
  }
  
  else if (overDepth) {
    locked = true;
    yoff = mouseY - 350 - bitDepth / 4 * 5;
    println(yoff);
  }
}

void mouseDragged() {
  if (mouseY < 300 && mouseX > -1 && mouseX < 800) {
   yPos[mouseX] = mouseY; 
  }
  
  else if (overRate && locked) {
    bitRate = (mouseY - yoff - 350) * 2;
    if (bitRate < 1)
      bitRate = 1;
    else if (bitRate > 200)
      bitRate = 200;
  }
  
  else if (overDepth && locked) {
    bitDepth = (mouseY - yoff - 350) * 4 / 5;
    if (bitDepth < 1)
      bitDepth = 1;
    else if (bitDepth > 80)
      bitDepth = 80;
  }
}

void mouseReleased() {
  locked = false;
}
