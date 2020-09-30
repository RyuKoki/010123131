/*////////////////////////////////////////////////////////////////
Coding By : Onpinya Phakhahutthakosol
     with : Donyapa Praman
@ King Mongkut's University of Technology North Bangkok
@ CprE, KMUTNB (Bangkok)
///////////////////////////////////////////////////////////////*/

let canvas = document.getElementById('canvas');
let context = canvas.getContext('2d');

canvas.width = window.innerWidth-100;
canvas.height = 500;

////////// PART OF PLAYER [SPIDER MAN] //////////
function Player (x, y, width, height) {
    context.fillStyle = 'green';
    context.fillRect(x, y, width, height);
}

/*
'spider', 'control' and 'Movement'
Thank you reference
https://github.com/pothonprogramming/pothonprogramming.github.io/tree/master/content/control
*/
let spider = {

    x:50,
    y:0,
    width:80,
    height:80,
    jumping:true,
    y_dist:0

}

let control = {

    up:false,
    down:false,
    keyListener:function (event) {
        var key_state = (event.type == "keydown")?true:false;
        switch (event.keyCode) {

            case 38: // arrow up
                control.up = key_state;
            break;

            case 40: // arrow down
                control.down = key_state;
            break;

        }
    }
}

var Movement;
Movement = function () {

    if (control.up && spider.jumping == false) {
        spider.y_dist -= 60;
        spider.jumping = true;
    }

    spider.y_dist += 3.0;
    spider.y += spider.y_dist;
    spider.y_dist *= 0.9;

    if (spider.y > 500 - 40 - 80) {
        spider.jumping = false;
        spider.y = 500 - 40 - 80;
        spider.y_dist = 0;
    }

    context.fillStyle = '#202020';
    context.fillRect(0, 0, canvas.width, canvas.height);

    Player(spider.x, spider.y, spider.width, spider.height);

    window.requestAnimationFrame(Movement);

}

window.addEventListener("keydown", control.keyListener);
window.addEventListener("keyup", control.keyListener);
window.requestAnimationFrame(Movement);

/*////////////////////////////////////////////////////////////////
This is the BACKEND part.
Here is FRONTEND part :: https://github.com/DonXI/010123131/tree/master/spider
///////////////////////////////////////////////////////////////*/
