let canvas = document.getElementById('canvas');
let context = canvas.getContext('2d');

canvas.width = 650;
canvas.height = 200;

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
        this.jumping = true;

    }

    show () {

        context.beginPath();
        context.fillStyle = 'green';
        context.fillRect(this.x, this.y, this.w, this.h);
        context.closePath();

    }

    jump () {

        if (keyboard_input.up && this.jumping == false) {
            this.dist_y -= 20;
            this.jumping = true;
        }

        this.dist_y += 1.0;
        this.y += this.dist_y;
        this.dist_y *= 0.9;

        if (this.y > 200 - 20 - 40) {
            this.jumping = false;
            this.y = 200 - 20 - 40;
            this.dist_y = 0;
        }

    }

    control () {

        if (keyboard_input.up) {
            this.jump();
        }

        this.show();

    }

}

var player;
function start () {

    player = new Player(25, 140, 40, 40);
    window.requestAnimationFrame(update);

}

function update () {

    window.requestAnimationFrame(update);
    context.clearRect(0, 0, canvas.width, canvas.height);
    player.control();
}

document.addEventListener("keydown", keyboard_input.keyListener);
document.addEventListener("keyup", keyboard_input.keyListener);

start();
