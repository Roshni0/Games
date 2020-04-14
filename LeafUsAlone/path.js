/////////////////////////////////////////////////////////////////
///////////////	Global Variables  //////////////////////////////
///////////////////////////////////////////////////////////////
var c =0; 
var game = new Game(800, 600, "Leaf us alone");

var wave1 = [];
var wave2 = [];
var wave3 = [];
var wave4 = [];
var wave5 = [];
var waveDelay = [5000,5000];
var nextWave = 1;
var waveDelay = [5000,10000,15000,20000,25000,40000];
// time for last enemy to come out
var lastEnemy = 0;
//array to create lots of enemies
var enemies = [];
var wave1, wave2, wave3, wave4, wave5 = [];

var score =150;
var scoreText;

//increment turbines after a turbine is placed
var turbines = 0;
var oldTurbines = 0;
var helpLoaded = false;

var tur, turSide
var turSideX = 650;
var turSideY = 200;

var spaces = [["","","","","","","","","","","",""],
			["","","","","","P","P","P","P","P","",""],
			["","","","","","P","","","","P","",""],
			["P","P","P","P","","P","","","","P","",""],
			["","","","P","","P","L","L","","P","",""],
			["","","","P","","P","L","L","","P","",""],
			["","","","P","","P","L","L","","P","",""],
			["","","","P","","P","L","L","","P","",""],
			["L","L","","P","P","P","","","","P","",""],
			["L","L","","","","","","","","P","",""],
			["L","L","","","","","","","","P","",""],
			["L","L","","","","","","","","G","",""],];
var basicTower, tower;
var towers = [];
var keyboard, mouse, squares, clicked, selectedSquare, selected;
var updateDelay = 500;
var towerSideX = 650;
var towerSideY = 150;
var towerRange = 150;
var rangeSprite, range, bulletSprite;
var reload = 1000;
var bullets = [];
var goalSprite, goal;
//new
var basicTowerCost = 150;
var basicTowerText;
var turbineCost = 200;
var turbineText;

var lives = 20;
var livesText;
var currentLives = 100;
var ended = false;
var endTime = waveDelay[0] + waveDelay[1] + waveDelay[2] + waveDelay[3] + waveDelay[4] + waveDelay[5];
var bg, bgs;
/////////////////////////////////////////////////////////////////
///////////////	Functions //////////////////////////////////////
///////////////////////////////////////////////////////////////

function preload() {
	// load the platforms
	//load the small horizontal platform
	//pathSide = new Sprite("img/platformSide.png");
	//load the small vertical platform
	//pathDown = new Sprite("img/platformDown.png");
	//load the long horizontal platform
//	pathLongSide = new Sprite("img/platformLongSide.png");
	//load enemy
	//load background
	//bg = new Sprite("img/levelbg.png");
	enemy = new Sprite ("img/Lumberjack_Sprite_Sheet.png",41,42);
	house = new Sprite ("img/house.png",66,73)
	//question = new Sprite("img/question.png",59,66);
	helpMe = new Sprite("img/dino.png",400,400);
	
	lightning = new Sprite("img/energy.png", 50, 50)
	
	tower = new Sprite("img/tower1.png",50,50);
	keyboard = new Keyboard();
	space = keyboard.createSpaceKey();
	mouse = new Mouse();
	selectedSquare = new Sprite("img/selectedSquare.png");
	
	rangeSprite = new Sprite("img/target.png");
	bulletSprite = new Sprite("img/pinecone.png");
	
	heart = new Sprite("img/heart.png", 40, 40)
	blank1 = new Sprite("img/blank.png", 1, 50)
	blank2 = new Sprite("img/blank.png", 1, 50)
	goalSprite = new Sprite("img/treedeath.png", 50, 50);
	game.loadBackgroundImage('bg1', 'img/levelbg.png');
	endSprite = new Sprite("img/lose.png");
	winSprite = new Sprite("img/winscreen.png");
	tur = new Sprite("img/wind_turbines.png",50,50);
}

function create() {
	//create an instance of the classes
//	pathSideOne = pathSide.create(200,100);
//	pathDownOne = pathDown.create(200,100);
//	PathSideTwo = pathSide.create(200,280);
//	pathDownTwo = pathDown.create(570,300);
//	pathSideThree = pathLongSide.create(0,470);
	//bgs = bg.create(0,0);
	game.setBackgroundImage('bg1', 800, 600, 0, 0);

	goal = goalSprite.create(550, 450);
	goal.addAnimation("death", [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 4, false);
	goal.setStopFrame(15)
	logo = lightning.create(game.gameWidth() - 130, 25)
	
	//butto.createButton()
	var Timer = setInterval(increase, (250-(10*turbines)));
	//questio = question.create(700,500);
	
	towerSide = tower.create(towerSideX, towerSideY);
	towerSide.setImmovable(true);
	towers.push(towerSide);
	
	
	turSide = tur.create(turSideX, turSideY); //
	turSide.setImmovable(true);
	selected = selectedSquare.create(800,0);
	
	//scoress = scoreText.create(550,30);
	
	livesText = new Text(lives, game.gameWidth() - 90, 75, "50px", "Arial", "#FFF");
	
	//new
	basicTowerText = new Text(basicTowerCost, game.gameWidth() - 100, 162, "25px", "Arial", "#FFF");
	turbineText = new Text(turbineCost, game.gameWidth() - 100, 210, "25px", "Arial", "#FFF");
	
	livesText.setVisible(true);
	
	//livess = livesText.create(550,90);
	logo2 = heart.create(game.gameWidth() - 130, 82)
	end1 = blank1.create(510,460)
	//updated 
	end2 = blank2.create(511,460)
	
	for (i=0;i<3;i++){
	//	if (game.getGameTime() > (lastEnemy + 400)) {
		wave1.push(enemy.create(155,20));
		//enemy.create(155,10)
	
	//	lastEnemy = game.getGameTime();
		//}
		//console.log(i);
		}
	for (i=0;i<10;i++){
		wave2.push(enemy.create(155,20));//NN
	}
	for (i=0;i<20;i++){
		wave3.push(enemy.create(155,20));
	}
	for (i=0;i<35;i++){
		wave4.push(enemy.create(155,20));
	}
	for (i=0;i<50;i++){
		wave5.push(enemy.create(155,20));
	}
	enemy.addAnimation('left',[4,5,6],5);
	//console.log("l");
	enemy.addAnimation('right',[1,2,3],5);
	//console.log("r");
	enemy.setStopFrame(0);
	scoreText = new Text("score", game.gameWidth()-90, 23, "50px", "Arial", "#FFF");
	//scoreText.changeText(0)
	house = house.create(142,0)
}


function update() {
	
	if (oldTurbines < turbines){
		var Timer = setInterval(increase, (250-(10*turbines)));
		oldTurbines = turbines
	}
	
	console.log(turbines)
	console.log(scoreText); //throw '';
	/*if (game.getGameTime() > (lastEnemy + 400)) {
		enemies.push(enemy.create(155,10));	
		//enemy.create(155,10)
	
		lastEnemy = game.getGameTime();
		//console.log(i);
	}
	*/
	livesText.changeText(lives)
	for (i=0; i<(enemies.length);i++){
	if (game.getGameTime() > (lastEnemy + 800)) {
		
	//make enemy move down (1)
	if (enemies[i].getX()==155 && enemies[i].getY()==20){
		enemies[i].setVelocityX(0);
		enemies[i].setVelocityY(150);
		lastEnemy = game.getGameTime();
		//console.log(enemyOne.getY());
		}
	}
	//make enemies move along (2)
	if ((enemies[i].getY()==150 /*&& enemyOne.getX()==575*/) ){
			enemies[i].setVelocityY(0);
			enemies[i].setVelocityX(150);		
			enemies[i].playAnimation('right');			
	}
	//make enemies move down(3)
	if (enemies[i].getX()==410 && enemies[i].getY()==150){
		enemies[i].setVelocityX(0);
		enemies[i].setVelocityY(150);
		enemies[i].stop();
		//console.log(enemyOne.getY());
		}
	//make enemies move along (4)
	if ((enemies[i].getY()==260 /*&& enemyOne.getX()==575*/) ){
			enemies[i].setVelocityY(0);
			enemies[i].setVelocityX(-150);
			enemies[i].playAnimation('left');
	}
	//make enemies move down(5)
	if (enemies[i].getX()==60 && enemies[i].getY()==260){
		enemies[i].setVelocityX(0);
		enemies[i].setVelocityY(150);
		enemies[i].stop();
		//console.log(enemyOne.getY());
		}
	//make enemy move along (6)
	if ((enemies[i].getY()==460 /*&& enemyOne.getX()==575*/) ){
			enemies[i].setVelocityY(0);
			enemies[i].setVelocityX(150);
			enemies[i].playAnimation('right');					
	}
	//stop enemy at square 11 along and 10 down (!!do 550-width of sprite)
	if (enemies[i].getX()==510){
		enemies[i].kill();
	}
	
	game.checkOverlap(enemies[i], end1, decreaseLives)
	game.checkOverlap(enemies[i], end2, increaseLives)
	
	
	for(x=0; x < bullets.length; x++){
		game.checkOverlap(enemies[i], bullets[x], killEnemy, [enemies[i], bullets[x]])
	}
	
		if (lives == 0){
		lives = 0
		console.log("start")
		for(i=0; i<enemies.length; i++){
			enemies[i].setVelocityX(0)
			enemies[i].setVelocityY(0)
			enemies[i].stop();
		}
		scoreText.changeText(0)
		//var timeToEnd = game.getGameTime() + 8000;
		goal.playAnimation("death");
		ended = true
		endTime = game.getGameTime() + 4000;
		//endSprite.create(0,0);
	}
	
	}
	
	scoreText.changeText(score)
	
	
	if(mouse.mouseX() < 600) {
		mouse.onClick(returnBool);
		if(clicked) {
			squares = detectSquare();
			if(selected.getX()==squares[0]*50&&selected.getY()==squares[1]*50) {
				selected.setX(800);
				selected.setY(0);
			} else {
				selected.setX(squares[0]*50);
				selected.setY(squares[1]*50);
			}
		}
		//if(spaces[mouse.onClick(detectSquare)[0]][mouse.onClick(detectSquare)[1]] == "") {
			//console.log("free");
		//}
	} else if(selected.getX() != 800) {
		mouse.onClick(returnBool);
		if(clicked) {
			squares = detectSquare();
			if(squares[0]*50==towerSideX&&squares[1]*50==towerSideY) {
				if(spaces[selected.getX()/50][selected.getY()/50]=="") {
					if (score >= basicTowerCost){
						createTower(tower);
					}
				}
			}
			if(squares[0]*50==turSideX&&squares[1]*50==turSideY) {
				if(spaces[selected.getX()/50][selected.getY()/50]=="") {
					if (score >= turbineCost){
						createTower(tur);
					}
				}
			}
		}
	}
	clicked = false;
	
	for(x=0; x < towers.length; x++) {
		if(towers[x][2] < game.getGameTime()) {
			for(i=0; i < enemies.length; i++) {
				var check = false;
				check = game.checkOverlap(towers[x][1], enemies[i], fireBullet, [towers[x][0], i]);
				if(check){
					towers[x][2] = game.getGameTime() + reload;
					break;
				}
			}
		}
	}
	
	/*checked = false;
	if(mouse.mouseX() >700 && mouse.mouseX()<765 && mouse.mouseY()>500 && mouse.mouseY()<575) {
		mouse.onClick(returnBoolean);
		if(!helpLoaded) {
			//game.pause();
			help = helpMe.create(100,100);
			helpLoaded = true;

		}
		//gamePausee();
	}
	if(mouse.mouseX() >480 && mouse.mouseX()<500 && mouse.mouseY()>100 && mouse.mouseY()<120) {
		if(helpLoaded){
			helpLoaded = false;
			console.log("here");		
			help.kill();
		}
		//gameResumee();
	}
			*/
	//butto.addDownAction(show_image("img/question.png",59,66,"pic"),0)
	
	//butto.addDownAction(show_image("img/dino.png",59,66,"pic"),0);
	scoreText.setVisible(true);
	
	if(game.getGameTime() > waveDelay[nextWave-1]){
		var wave;
		var end = false;
		switch(nextWave){
			case 1:
				wave = wave1;
				break;
			case 2:
				wave = wave2;//NN
				break;
			case 3:
				wave = wave3;
				break;
			case 4:
				wave = wave4;
				break;
			case 5:
				wave = wave5;
				break;
		}
		if(end){
			console.log("end");
		} else {
			for(i=0; i<wave.length; i++){
				enemies.push(wave[i]);
			}
			waveDelay[nextWave] += game.getGameTime();
			nextWave += 1;
		}
	}
	if(game.getGameTime() > endTime){
		if(ended){
			endSprite.create(0,0);
		} else {
			winSprite.create(0,0);
		}
	}
}

/*function gamePausee(){
	if(!helpLoaded) {
			game.pause();
			help = helpMe.create(100,100);
			helpLoaded = true;
			console.log("hey");
		}
	
}

function gameResumee(){
	if(helpLoaded){
			helpLoaded = false;
			console.log("here");		
			help.kill();
			game.resume();
		}
}
*/
/*function show_image(src, width, height, alt) {
	if (c == 0) {
    var img = document.createElement("img");
    img.src = src;
    img.width = width;
    img.height = height;
    img.alt = alt;

    // This next line will just add it to the <body> tag
    document.body.appendChild(img); }
	c = 1;
}
*/

function createTower(towerType) {
	var newTower = towerType.create(selected.getX(), selected.getY(), 50, 50);
	spaces[selected.getX()/50][selected.getY()/50] = "T";
	
	
	
	//new 
	if (towerType == tower){
		if (score - basicTowerCost > 0){
			score = score - basicTowerCost
			var range = rangeSprite.create(selected.getX()-towerRange/2, selected.getY()-towerRange/2);
			//newTower.setDraggable(newTower);
			towers.push([newTower, range, reload]);
		}
	}else if(towerType == tur) {
		if (score - turbineCost > 0){
			turbines += 1;
			score = score - turbineCost
		}
	}
}


function detectSquare(square = null) {
	var x = mouse.mouseX();
	var y = mouse.mouseY();
	if(!(square == null)) {
		x = square;
		y = square;
	}
	if(x < 500) {
		x = (String(x/50))[0];
	} else {
		x = (String(x/50)).substring(0,2);
	}
	if(y < 500) {
		y = (String(y/50))[0];
	} else {
		y = (String(y/50)).substring(0,2);
	}
	return [x, y];
}

function returnBool() {
	clicked = true;
}

function returnBoolean(){
	checked = true;
}

function increase() {
	score = score + 1
	if (score > 999){
		score = 999
	}
}

function fireBullet(tower, i) {
	var xCo = tower.getX()+towerRange/2;
	var yCo = tower.getY()+towerRange/2
	var bullet = bulletSprite.create(xCo+25, yCo+25);
	bullets.push(bullet);
	var angle = -Math.PI + Math.atan2(yCo-i.getY(), xCo-i.getX());
	/*if(xCo<i.getX()&&yCo<i.getY()){
		console.log(1);
		angle = Math.PI - angle;
	} else if(xCo>i.getX()&&yCo<i.getY()){
		console.log(2);
		angle = -angle;
	} else if(xCo>i.getX()&&yCo<i.getY()){
		console.log(3);
		angle = -Math.PI + angle;
	} else {
		console.log(4);
		
	}*/
	bullet.setAngle(angle*(180/Math.PI));
	bullet.setVelocityX(500*Math.cos(angle));
	bullet.setVelocityY(500*Math.sin(angle));
	return true;
}
function decreaseLives(){
	lives = lives - 1
}

function increaseLives(){
	lives = lives + 1
}	
function killEnemy(one, two){
	one.kill();
	two.kill();
}
