const KEYS_UP = ["w", "ArrowUp"]
const KEYS_DOWN = ["s", "ArrowDown"]
const KEYS_LEFT = ["a", "ArrowLeft"]
const KEYS_RIGHT = ["d", "ArrowRight"]

let state = {
  left: false,
  right: false,
  up: false,
  down: false
}

/* Clone state */
let lastState = Object.assign({}, state)

function update() {
  const changed = state.left != lastState.left ||
        state.right != lastState.right ||
        state.up != lastState.up ||
        state.down != lastState.down
  lastState = Object.assign({}, state)

  if (changed) {
    if (state.left !== state.right) {
      // Turning either direction -> start turning
      if (state.left) request("/left")
      if (state.right) request("/right")
    } else if (state.up !== state.down) {
      // Not turning but going forward / back
      if (state.up) request("/up")
      if (state.down) request("/down")
    } else {
      request("/stop")
    }
  }
}

let lastUrl = ""
function request(url) {
  if (lastUrl === url) return
  lastUrl = url

  showUrl(url)

  let request = new XMLHttpRequest()
  request.open("GET", url)
  request.send()
}

const infoDisplay = document.getElementById("display")
function showUrl(url) {
  url = url.replace("/", "")
  url = url.substring(0, 1).toUpperCase() + url.substring(1)
  infoDisplay.innerHTML = url
}

window.onkeydown = event => {
  const key = event.key
  if (KEYS_UP.includes(key)) state.up = true
  if (KEYS_DOWN.includes(key)) state.down = true
  if (KEYS_LEFT.includes(key)) state.left = true
  if (KEYS_RIGHT.includes(key)) state.right = true
  update()
}

window.onkeyup = event => {
  const key = event.key
  if (KEYS_UP.includes(key)) state.up = false
  if (KEYS_DOWN.includes(key)) state.down = false
  if (KEYS_LEFT.includes(key)) state.left = false
  if (KEYS_RIGHT.includes(key)) state.right = false
  update()
}
