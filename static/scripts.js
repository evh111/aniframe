let canvas = document.getElementById('pixel_canvas');
let sizePicker = document.getElementById('sizePicker');
let color = document.getElementById('palette');

// Sets default 'pen' to white
var penColor = '#ffffff';

// Sets the selected color as a 'pen'
function setPenColor(pen) {
  penColor = pen;
}

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

color.addEventListener('click', function() {});

// Create the grid (16x32)
makeGrid();

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

function fillSquare() {
  this.setAttribute('style', `background-color: ${penColor}`);
  // Maps colors as soon as they are set and embed the result in the element
  let controllerColor = colormap[penColor];
  if (controllerColor == undefined) {
    alert(`That color isn't supported by the controller`);
  } else {
    this.setAttribute('controller-color', `${colormap[penColor]}`);
    getFrameAsJSON();
  }
}

// Clears grid of all colored cells
function clearGrid() {
  document.location.reload(true);
}

function getFrameAsJSON() {
  // Make an object that contains an array of frames
  let animation = {
    frames: [
      [
        // Rows go in here as arrays
      ]
    ]
  };
  M = canvas.rows.length;
  N = canvas.rows[0].cells.length;
  // Loops over each cell and adds an attribute to the first frame
  // REMINDER: Needs to handle mutiple frames
  // SUGGESTION: Have an index that they (the user?) controls from the UI
  for (let i = 0; i < M; i++) {
    let row = [];
    for (let j = 0; j < N; j++) {
      cell = canvas.rows[i].cells[j];
      // REMINDER: Modify to restrict this to our pallette
      row.push(cell.getAttribute('controller-color'));
      //animation.frames[0].push(cell.getAttribute('controller-color'));
    }
    animation.frames[0].push(row);
  }
  console.log(JSON.stringify(animation));
  $.post('/animation', JSON.stringify(animation, null, 4), null, 'json');
}
