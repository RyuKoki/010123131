let canvas = document.getElementById('canvas');
let context = canvas.getContext('2d');

canvas.width = window.innerWidth-100;
canvas.height = 300;

class Player {

    constructor (x, y, width, height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }

    Draw () {
        context.fillStyle = 'green';
        context.fillRect(this.x, this.y, this.width, this.height);
    }
}
let spider_size = 75;
const player = new Player(50, canvas.height-spider_size, spider_size, spider_size);
player.Draw();

class Enemy {

    constructor (x) {
        this.x = x;
        this.width = Math.floor(Math.random() * (75-50)) + 50;
        this.height = this.width;
        this.y = canvas.height - this.height;
    }

    Draw () {
        context.fillStyle = 'red';
        context.fillRect(this.x, this.y, this.width, this.height);
    }
}

const enemy = new Enemy(300);
enemy.Draw();

