var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
canvas.width = window.innerWidth-50;
canvas.height = window.innerHeight-50;

context.font = '40pt Consolas';
context.fillStyle = 'blue';
context.textAlign = 'center';
context.fillText('Hello World!', canvas.width/2, canvas.height/2);
