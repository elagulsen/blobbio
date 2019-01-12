var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');
var initSize = 10;
var playSize = initSize + 5;
var blobSize = initSize;
var blobGrow = true;
var playPos = {
    x: canvas.width / 2,
    y: canvas.height / 2,
}
var speed = 2;
var colours = ['#a9b6ff', '#ffa9f9', ' #aeffa9', '#9e76d1', '#ffd983', '#a4f1de'];
//var fs = require('fs');
var dx = 0;
var dy = 0;

window.addEventListener("keydown", keydown, false);
window.addEventListener("keyup", keyup, false);
var right = false;
var left = false;
var up = false;
var down = false;

function keydown(e) {
    switch (e.keyCode) {
        case 37:
            left = true;
            break;
        case 38:
            up = true;
            break;
        case 39:
            right = true;
            break;
        case 40:
            down = true;
            break;
    }
}

function keyup(e) {
    switch (e.keyCode) {
        case 37:
            left = false;
            break;
        case 38:
            up = false;
            break;
        case 39:
            right = false;
            break;
        case 40:
            down = false;
            break;
    }
}

function drawCircle(x, y, size, colour) {
    ctx.beginPath();
    ctx.arc(x, y, size, 0, 2 * Math.PI, false);
    ctx.shadowBlur = size * 1.1;
    ctx.shadowColor = colour;
    ctx.fillStyle = colour;
    ctx.fill();
}

function generateBlobs(n) {
    var blobs = [];
    for (let i = 0; i < n; i++) {
        let blob = {};
        blob.x = Math.random() * (canvas.width * 10) - canvas.width * 5;
        blob.y = Math.random() * (canvas.width * 10) - canvas.width * 5;
        blob.colour = colours[Math.floor(Math.random() * colours.length)];
        blob.radius = initSize;
        blobs.push(blob);
    }
    return blobs;
}

function generateBlots(n) {
    var blots = [];
    for (let i = 0; i < n; i++) {
        let blot = {};
        blot.x = Math.random() * canvas.width * 10 - canvas.width * 5;
        blot.y = Math.random() * canvas.width * 10 - canvas.width * 5;
        blot.colour = colours[Math.floor(Math.random() * colours.length)];
        blot.radius = 20 + Math.ceil(Math.random() * 10);
        blot.xd = [-1, 1][Math.floor(Math.random() * 2)];
        blot.yd = [-1, 1][Math.floor(Math.random() * 2)];
        blot.dx = 0;
        blot.dy = 0;
        blots.push(blot);
    }
    return blots;
}

function mainDraw(blobs, player, blots) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (right) dx -= speed;
    if (left) dx += speed;
    if (down) dy -= speed;
    if (up) dy += speed;

    if (blobGrow) {
        blobSize += .03;
        if (blobSize > 12) blobGrow = false;
    } else {
        blobSize -= .03;
        if (blobSize < 11) blobGrow = true;
    }

    blobs.forEach(function (blob) {
        if (blob.isDead) return;
        if (Math.abs(blob.x + dx - player.x) < (blob.radius + player.radius) && Math.abs(blob.y + dy - player.y) < (blob.radius + player.radius)) {
            blob.isDead = true;
            player.radius = (player.radius ** 2 + blob.radius ** 2) ** 0.5;
        }

        drawCircle(blob.x + dx, blob.y + dy, blob.radius, blob.colour);
    })

    blots.forEach(function (blot) {
        if (blot.isDead) return;
        if (Math.abs(blot.x + blot.dx + dx - player.x) < (blot.radius + player.radius) && Math.abs(blot.y + blot.dy + dy - player.y) < (blot.radius + player.radius)) {
            if (player.radius > blot.radius) {
                blot.isDead = true;
                player.radius = (player.radius ** 2 + blot.radius ** 2) ** 0.5;
            } else {
                clearInterval(interval);
                alert('You were eaten!');
            }
        }
        
        if (Math.random() > .99) blot.xd = !blot.xd;
        if (Math.random() > .99) blot.yd = !blot.yd;
        
        blot.dx += blot.xd;
        blot.dy += blot.yd;
        
        drawCircle(blot.x + dx + blot.dx, blot.y + dy + blot.dy, blot.radius, blot.colour);
    })

    drawCircle(player.x, player.y, player.radius, player.colour);
    $('#points').text(Math.floor(player.radius**2 * Math.PI) - 1256)
}

var invterval;

function init() {
    var blobs = generateBlobs(6000);
    var blots = generateBlots(200);
    var player = {
        x: 400,
        y: 400,
        colour: 'red',
        radius: 20
    }
    interval = setInterval(function () {
        mainDraw(blobs, player, blots)
    }, 10)
}

$(function () {
    init();
})
