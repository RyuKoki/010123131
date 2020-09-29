let canvas = document.getElementById('canvas');
let context = canvas.getContext('2d');

canvas.width = window.innerWidth-100;
canvas.height = 300;

////////// PART OF PLAYER [SPIDER MAN] //////////
let init_player_w = 75;
let init_player_h = 75;
let init_player_x = 50;
let init_player_y = canvas.height-init_player_h;
function player(x, y, width, height) {
    context.fillStyle = 'green';
    context.fillRect(x, y, width, height)
}

function jump() {
    let dist_jump = 80;
    player(init_player_x, init_player_y-dist_jump, init_player_w, init_player_h);
}

function slide() {
    let dist_slide = init_player_h / 2
    player(init_player_x, init_player_y+dist_slide, init_player_w, dist_slide);
}

function running(event) {
    event = event || window.event;
    if (event.keyCode == '39') { // button RIGHT
        player(init_player_x, init_player_y, init_player_w, init_player_h);
    } else if (event.keyCode == '38') { // button UP
        jump();
    } else if (event.keyCode == '40') { // button DOWN
        slide();
    }
}
document.onkeydown = running;
