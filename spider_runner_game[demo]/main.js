let canvas = document.getElementById('canvas');
let context = canvas.getContext('2d');

canvas.width = 650;
canvas.height = 200;

let game_speed;
let player;
let element = document.documentElement;
let keyboard_input = {
    up:false,
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
            this.dist_y = -12;
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
            this.dist_y += 0.75;
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

}

function rand_int (min, max) {
    return Math.round(Math.random() * (max-min) + min);
}

function start () {
    player = new Player(25, 0, 40, 40);
    game_speed = 2;
    requestAnimationFrame(update);
}

function update () {
    requestAnimationFrame(update);
    context.clearRect(0, 0, canvas.width, canvas.height);

    player.control();
    
    if (keyboard_input.open_full) {
        element.requestFullscreen();
    } else if (keyboard_input.close_full) {
        document.exitFullscreen();
    }

}

document.addEventListener("keydown", keyboard_input.keyListener);
document.addEventListener("keyup", keyboard_input.keyListener);
requestAnimationFrame(update);

start();
