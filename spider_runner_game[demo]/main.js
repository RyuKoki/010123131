let canvas = document.getElementById('canvas');
let context = canvas.getContext('2d');

canvas.width = 650;
canvas.height = 200;

let enemy;
let enemies = [];
let player;
let element = document.documentElement;
let game_speed;
let count_score;
let score;
let keyboard_input = {
    up:false,
    space:false,
    open_full:false,
    close_full:false,
    keyListener:function (event) {
        var key_state = (event.type == "keydown")?true:false;
        switch (event.keyCode) {

            case 38: // arrow up button
                keyboard_input.up = key_state;
            break;
            case 33: // page up button
                keyboard_input.open_full = key_state;
            break;
            case 27: // Esc button
                keyboard_input.close_full = key_state;
            break;
            case 32:
                keyboard_input.space = key_state;
            break;
        }
    }
}

sprite_sheet = {
    frame_sets:[[0, 1]],
    image:new Image()
};

enemy_sheet = {
    image:new Image()
};

background_sheet = {
    image: new Image()
};

class Player {

    constructor (frame_set, speed) {
        this.x = 25;
        this.y = 0;
        this.w = 50;
        this.h = 50;
        this.dist_y = 0;
        this.count = 0;
        this.speed = speed;
        this.frame = 0;
        this.frame_index = 0;
        this.frame_set = frame_set;
    }


    jump () {
        if (this.y == canvas.height - this.h) {
            this.dist_y = -10;
        }
    }

    show () {
        context.drawImage(sprite_sheet.image, player.frame * this.h , 0, 
            this.h, this.h, Math.floor(player.x), Math.floor(player.y), this.h, this.h);
    }

    control () {
        if (keyboard_input.up) {
            this.jump();
        }

        this.y += this.dist_y;

        if (this.y + this.h < canvas.height) {
            this.dist_y += 0.25;
        } else {
            this.dist_y = 0;
            this.y = canvas.height - this.h;
        }

        this.show();
    }

 
    change(frame_set,speed){
        if (this.frame_set != frame_set) {
            this.count = 0;
            this.speed = speed;
            this.frame_index = 0;
            this.frame_set = frame_set;
            this.frame = this.frame_set[this.frame_index];
    
          }
    }

    update(){
        this.count ++;
      if (this.count >= this.speed) {
        this.count = 0;
        this.frame_index = (this.frame_index == this.frame_set.length - 1) ? 0 : this.frame_index + 1;
        this.frame = this.frame_set[this.frame_index];
      }
    }

}

class Enemy {

    constructor (x, y) {
        this.x = x;
        this.y = y;
        this.w = 40;
        this.h = 40;

        this.dist_x = -game_speed;
    }

    show () {
        context.drawImage(enemy_sheet.image, this.x, this.y, this.w, this.h)
    }

    run () {
        this.x += this.dist_x;
        this.show();
        this.dist_x = -game_speed;
    }

}

class Score {

    constructor (score) {;
        this.text = "Score : " + score;
        this.x = 325;
        this.y = 40;
        this.align = "center";
    }

    show () {
        context.fillStyle = 'black';
        context.font = "20px Consolas";
        context.textAlign = this.align;
        context.fillText(this.text, this.x, this.y);
    }
}

function random_dist (min, max) {
    return Math.round(Math.random() * (max - min) + min);
}

function spawn_enemy () {
    let x_pos = random_dist(650, 750);
    enemy = new Enemy(x_pos, 160);
    enemies.push(enemy);
}

function start () {
    game_speed = 3;
    context.font = "20px Consolas";
    score = 0;
    count_score = new Score(score);
    player = new Player();
    requestAnimationFrame(update);
}




let initialSpawnTimer = 200;
let spawnTimer = initialSpawnTimer;
function update () {
    requestAnimationFrame(update);
    context.drawImage(background_sheet.image, 0, 0, canvas.width, canvas.height)
    // context.clearRect(0, 0, canvas.width, canvas.height);
    spawnTimer--;
    if (spawnTimer <= 0) {
        spawn_enemy();
        console.log(enemies);
        spawnTimer = initialSpawnTimer - game_speed * 8;
    
        if (spawnTimer < 60) {
            spawnTimer = 60;
        }
    }

    for (let i = 0; i < enemies.length; i++) {
        let e = enemies[i];

        if (e.x + e.w < 0) {
            enemies.splice(i, 1);
        }

        if (player.x < e.x + e.w && player.x + player.w > e.x && player.y < e.y + e.h && player.y + player.h > e.y) {
                if (confirm("Game Over! \nDo you want to restart?")) {
                    enemies = [];
                    spawnTimer = initialSpawnTimer;
                    game_speed = 3;
                    score = 0;
                } else {
                    window.close();
                }
            }
        e.run();
    }

    // game_speed += 0.003

    if(!player.control()){
        player.change(sprite_sheet.frame_sets[0], 10);
    }

    player.control();
    
    if (keyboard_input.open_full) {
        element.requestFullscreen();
    } else if (keyboard_input.close_full) {
        document.exitFullscreen();
    }

    score++;
    player.update();
    count_score.text = "Score : " + (Math.floor(score/60));
    count_score.show();

}

document.addEventListener("keydown", keyboard_input.keyListener);
document.addEventListener("keyup", keyboard_input.keyListener);

requestAnimationFrame(update);


sprite_sheet.image.src = "sp_100x50_ver01.png";
enemy_sheet.image.src = "01.png";
background_sheet.image.src = "bg01.jpg"



start();
