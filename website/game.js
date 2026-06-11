const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const box = 20;

let snake = [];
snake[0] = { x: 9 * box, y: 9 * box };

let direction = "RIGHT";

let food = {
  x: Math.floor(Math.random() * 20) * box,
  y: Math.floor(Math.random() * 20) * box
};

let score = 0;

// Controls
document.addEventListener("keydown", changeDirection);

function changeDirection(event) {
  let key = event.keyCode;

  if (key == 37 && direction != "RIGHT") direction = "LEFT";
  else if (key == 38 && direction != "DOWN") direction = "UP";
  else if (key == 39 && direction != "LEFT") direction = "RIGHT";
  else if (key == 40 && direction != "UP") direction = "DOWN";
}

// Collision
function collision(head, array) {
  for (let i = 0; i < array.length; i++) {
    if (head.x === array[i].x && head.y === array[i].y) {
      return true;
    }
  }
  return false;
}

// Game loop
function draw() {
  ctx.fillStyle = "black";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // snake
  for (let i = 0; i < snake.length; i++) {
    ctx.fillStyle = i === 0 ? "lime" : "green";
    ctx.fillRect(snake[i].x, snake[i].y, box, box);
  }

  // food
  ctx.fillStyle = "red";
  ctx.fillRect(food.x, food.y, box, box);

  // old head position
  let snakeX = snake[0].x;
  let snakeY = snake[0].y;

  if (direction == "LEFT") snakeX -= box;
  if (direction == "RIGHT") snakeX += box;
  if (direction == "UP") snakeY -= box;
  if (direction == "DOWN") snakeY += box;

  // eat food
  if (snakeX === food.x && snakeY === food.y) {
    score++;
    food = {
      x: Math.floor(Math.random() * 20) * box,
      y: Math.floor(Math.random() * 20) * box
    };
  } else {
    snake.pop();
  }

  // new head
  let newHead = { x: snakeX, y: snakeY };

  // game over
  if (
    snakeX < 0 ||
    snakeY < 0 ||
    snakeX >= canvas.width ||
    snakeY >= canvas.height ||
    collision(newHead, snake)
  ) {
    clearInterval(game);
    alert("Game Over! Score: " + score);
    return;
  }

  snake.unshift(newHead);

  // score
  ctx.fillStyle = "white";
  ctx.fillText("Score: " + score, 10, 20);
}

let game = setInterval(draw, 100);