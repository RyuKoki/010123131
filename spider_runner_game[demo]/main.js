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

class Player {

    constructor (x, y, width, height) {
        this.x = x;
        this.y = y;
        this.w = width;
        this.h = height;

        this.dist_y = 0;
    }

    jump () {
        if (this.y == canvas.height - this.h) {
            this.dist_y = -10;
        }
    }

    draw () {
        context.fillStyle = 'green';
        context.fillRect(this.x, this.y, this.w, this.h);
    }

    control () {
        if (keyboard_input.up) {
            this.jump();
        }

        this.y += this.dist_y;

        if (this.y + this.h < canvas.height) {
            this.dist_y += 0.4;
        } else {
            this.dist_y = 0;
            this.y = canvas.height - this.h;
        }

        this.draw();
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

    draw () {
        context.fillStyle = 'red';
        context.fillRect(this.x, this.y, this.w, this.h);
    }

    run () {
        this.x += this.dist_x;
        this.draw();
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
    // let y_pos = random_dist(90, 160);
    enemy = new Enemy(x_pos, 160);
    enemies.push(enemy);
}

function start () {
    game_speed = 3;

    context.font = "20px Consolas";
    score = 0;
    count_score = new Score(score);

    player = new Player(25, 0, 40, 40);
    requestAnimationFrame(update);
}

let initialSpawnTimer = 200;
let spawnTimer = initialSpawnTimer;
function update () {
    requestAnimationFrame(update);
    context.clearRect(0, 0, canvas.width, canvas.height);
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

        if (player.x < e.x + e.w && player.x + player.w > e.x &&
            player.y < e.y + e.h && player.y + player.h > e.y) {
                if (confirm("Game Over! \nDo you want to restart?")) {
                    enemies = [];
                    spawnTimer = initialSpawnTimer;
                    score = 0;
                } else {
                    window.close();
                }
            }
        e.run();
    }

    player.control();
    
    if (keyboard_input.open_full) {
        element.requestFullscreen();
    } else if (keyboard_input.close_full) {
        document.exitFullscreen();
    }

    score++;
    
    count_score.text = "Score : " + (Math.floor(score/60));
    count_score.show();

}

document.addEventListener("keydown", keyboard_input.keyListener);
document.addEventListener("keyup", keyboard_input.keyListener);
requestAnimationFrame(update);

start();
