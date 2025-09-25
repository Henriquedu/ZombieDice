// Definição dos dados
const dice = [
  { color: "green", faces: ["brain","brain","brain","footprint","footprint","shotgun"] },
  { color: "yellow", faces: ["brain","brain","footprint","footprint","shotgun","shotgun"] },
  { color: "red", faces: ["brain","footprint","footprint","shotgun","shotgun","shotgun"] },
];

let brains = 0;
let shotguns = 0;

const statusEl = document.getElementById("status");
const resultsEl = document.getElementById("results");
const scoreEl = document.getElementById("score");
const rollBtn = document.getElementById("rollBtn");
const stopBtn = document.getElementById("stopBtn");

function rollDice() {
  resultsEl.innerHTML = "";

  for (let i = 0; i < 3; i++) {
    const die = dice[Math.floor(Math.random() * dice.length)];
    const face = die.faces[Math.floor(Math.random() * die.faces.length)];

    const p = document.createElement("p");
    p.textContent = `${die.color.toUpperCase()} -> ${face}`;
    resultsEl.appendChild(p);

    if (face === "brain") brains++;
    else if (face === "shotgun") shotguns++;
  }

  scoreEl.textContent = `Cérebros: ${brains} | Tiros: ${shotguns}`;

  if (shotguns >= 3) {
    statusEl.textContent = "💥 Você levou 3 tiros! Perdeu a rodada!";
    rollBtn.disabled = true;
    stopBtn.disabled = true;
  } else {
    statusEl.textContent = "Você pode continuar ou parar.";
    stopBtn.disabled = false;
  }
}

function stopRound() {
  statusEl.textContent = `Rodada encerrada! Você guardou ${brains} cérebros.`;
  rollBtn.disabled = true;
  stopBtn.disabled = true;
}

rollBtn.addEventListener("click", rollDice);
stopBtn.addEventListener("click", stopRound);
