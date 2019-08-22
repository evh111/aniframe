let canvas = document.getElementById('pixel-canvas');
let color = document.getElementById('palette');
let frameTable = document.getElementById('frame-table');
let frames = document.getElementById('frames');
let frame = document.getElementById('frame');

// Sets default index to 0
var frameIndex = 0;

// Sets default 'pen' to white
var penColor = '#ffffff';

// Get the current 'frameIndex'
function setIndex(frame) {
  // Adjust UI
  frameTable.rows[0].cells[frameIndex].classList.remove('selection');
  // Converts 'data-value' into a number
  frameIndex = Number(frame.getAttribute('data-value'));
  frame.classList.add('selected');
}

function setFrameRate() {
  // Do stuff
}

// Sets the selected color as a 'pen'
function setPenColor(pen) {
  penColor = pen;
}

// Supported color palette (does not handle PWM)
let colormap = {
  '#000000': 0b000,
  '#0000ff': 0b001,
  '#00ff00': 0b010,
  '#00ffff': 0b011,
  '#ff0000': 0b100,
  '#ff00ff': 0b101,
  '#ffff00': 0b110,
  '#ffffff': 0b111
};

// Creates the grid
makeGrid();

// Global animation array
animation = { frames: [] };

// Set the 'animation' array to a series of 10 black frames
for (let f = 0; f < 10; f++) {
  let frame = [];
  M = canvas.rows.length;
  for (let i = 0; i < M; i++) {
    let row = [];
    N = canvas.rows[0].cells.length;
    for (let j = 0; j < N; j++) {
      row.push(0);
    }
    frame.push(row);
  }
  animation.frames.push(frame);
}

color.addEventListener('click', function() {});

// Function to create grid (16x32)
function makeGrid() {
  for (let r = 0; r < 16; r++) {
    const row = canvas.insertRow(r);
    for (let c = 0; c < 32; c++) {
      const cell = row.insertCell(c);
      cell.addEventListener('click', fillSquare);
      // Make sure all the cells that are initialized have a supported color
      cell.setAttribute('style', 'background-color: #000000');
      cell.setAttribute('controller-color', '0');
    }
  }
}

// Colors in selected cell with the value of penColor
// then, maps the updated cell to the controller
function fillSquare() {
  this.setAttribute('style', `background-color: ${penColor}`);
  // Maps colors as soon as they are set and embed the result in the element
  let controllerColor = colormap[penColor];
  if (controllerColor == undefined) {
    alert(`That color isn't supported by the controller`);
  } else {
    this.setAttribute('controller-color', `${colormap[penColor]}`);
    currentFrame();
  }
}

// Clears grid of all colored cells
function clearGrid() {
  // Loop to set to black frames and reset 'frameIndex' to 0
  frameIndex = 0;
  for (let f = 0; f < 10; f++) {
    let frame = [];
    M = canvas.rows.length;
    for (let i = 0; i < M; i++) {
      let row = [];
      N = canvas.rows[0].cells.length;
      for (let j = 0; j < N; j++) {
        row.push(0);
      }
      frame.push(row);
    }
    animation.frames.push(frame);
  }
}

// Sends a frame as an array of JSON
function currentFrame() {
  M = canvas.rows.length;
  for (let i = 0; i < M; i++) {
    N = canvas.rows[0].cells.length;
    for (let j = 0; j < N; j++) {
      cell = canvas.rows[i].cells[j];
      animation.frames[frameIndex][i][j] = cell.getAttribute(
        'controller-color'
      );
    }
  }
  $.post('/animation', JSON.stringify(animation, null, 4), null, 'json');
  console.log(JSON.stringify(animation, null, 4), null, 'json');
}
