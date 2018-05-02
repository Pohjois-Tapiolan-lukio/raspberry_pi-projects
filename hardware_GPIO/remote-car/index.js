const KEYS_UP = ["w", "ArrowUp"]
const KEYS_DOWN = ["s", "ArrowDown"]
const KEYS_LEFT = ["a", "ArrowLeft"]
const KEYS_RIGHT = ["d", "ArrowRight"]

function up(pressed) {
  if (pressed) request("/forward")
  else request("/stop")
}

function down(pressed) {
  if (pressed) request("/backward")
  else request("/stop")
}

function left(pressed) {
  if (pressed) request("/left")
  else request("/stop")
}

function right(pressed) {
  if (pressed) request("/right")
  else request("/stop")
}

function request(url) {
  let request = new XMLHttpRequest();
  request.open("GET", url)
  request.send()
}

window.onkeydown = event => {
  const key = event.key
  if (KEYS_UP.includes(key)) {
    up(true)
  }
  if (KEYS_DOWN.includes(key)) {
    down(true)
  }
  if (KEYS_LEFT.includes(key)) {
    left(true)
  }
  if (KEYS_RIGHT.includes(key)) {
    right(true)
  }
}

window.onkeyup = event => {
  const key = event.key
  if (KEYS_UP.includes(key)) {
    up(false)
  }
  if (KEYS_DOWN.includes(key)) {
    down(false)
  }
  if (KEYS_LEFT.includes(key)) {
    left(false)
  }
  if (KEYS_RIGHT.includes(key)) {
    right(false)
  }
}
