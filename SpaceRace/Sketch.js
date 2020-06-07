let leftShip;
let rightShip; 
let allDebris = [];
 
let spaceshipImage; // this is gonna have our gorgeous ship
function setup() {
  createCanvas(400, 400);
   
  // get the spaceship image from your project-folder
  spaceshipImage = loadImage('spaceship.png');
   
  // pass the image into the ship object
  leftShip = new Ship(width * 0.33, spaceshipImage);
  rightShip = new Ship(width * 0.66, spaceshipImage);
   
  for (let i = 0; i < NUM_DEBRIS; i++) {
    allDebris.push(new Debris());
  }
 
  leftScore = new Score(width * 0.33 - 40);
  rightScore = new Score(width * 0.66 + 40);
 
 
   
}
// how hard do you want to make it? :D
const NUM_DEBRIS = 30;
 
function setup() {
  createCanvas(400, 400);
  leftShip = new Ship(width * 0.33);
  rightShip = new Ship(width * 0.66);
   
  // create the debris objects
  for (let i = 0; i < NUM_DEBRIS; i++) {
    allDebris.push(new Debris());
  }
}
 
function draw() {
  background(0);
   
  leftShip.update();
  rightShip.update();
   
  leftShip.display();
  rightShip.display();
   
  // sexy function call
  updateDebrisAndCheckCollisions();
   
}
 
 
// sexy function
function updateDebrisAndCheckCollisions() {
  for (let i = 0; i < allDebris.length; i++) {
    allDebris[i].update();
    allDebris[i].display();
     
    if (allDebris[i].hasHitShip(leftShip)) {
        leftShip.respawn();
    } else if (allDebris[i].hasHitShip(rightShip)) {
        rightShip.respawn();
    }
  }
}
 
 
function keyPressed() {
    if (keyCode == UP_ARROW) {
    rightShip.isUp = true;
    rightShip.isDown = false;
  } else if (keyCode == DOWN_ARROW) {
    rightShip.isDown = true;
    rightShip.isUp = false;
  }
   
   
  if (keyCode == 87) {
    // keycode is 'w'
    leftShip.isUp = true;
    leftShip.isDown = false;
  } else if (keyCode == 83) {
    // keycode is 's'
    leftShip.isDown = true;
    leftShip.isUp = false;
  }
}
 
 
function keyReleased() {
    if (keyCode == UP_ARROW) {
    rightShip.isUp = false;
  } else if (keyCode == DOWN_ARROW) {
    rightShip.isDown = false;
  }
   
  if (keyCode == 87) {
    leftShip.isUp = false;
  } else if (keyCode == 83) {
    leftShip.isDown = false;
  }
}
