// Definição dos dados com emojis
const dice = [
  { color: "green", faces: ["🧠","🧠","🧠","👣","👣","💥"] },
  { color: "yellow", faces: ["🧠","🧠","👣","👣","💥","💥"] },
  { color: "red", faces: ["🧠","👣","👣","💥","💥","💥"] },
];

let players = [];
let scores = {};
let currentPlayer = 0;
let brains = 0;
let shotguns = 0;
const TARGET = 13;

// Seletores
const setup = document.getElementById("setup");
const game = document.getElementById("game");
const startBtn = document.getElementById("startBtn");
const rollBtn = document.getElementById("rollBtn");
const stopBtn = document.getElementById("stopBtn");
const restartBtn = document.getElementById("restartBtn");
const resultsEl = document.getElementById("results");
const scoreEl = document.getElementById("score");
const statusEl = document.getElementById("status");
const turnEl = document.getElementById("turn");
const scoreboardEl = document.getElementById("scoreboard");

// Iniciar jogo
startBtn.addEventListener("click", () => {
  const numPlayers = parseInt(document.getElementById("numPlayers").value);
  if (numPlayers < 2) {
    alert("Mínimo 2 jogadores!");
    return;
  }
  players = Array.from({length: numPlayers}, (_, i) => `Jogador ${i+1}`);
  scores = {};
  players.forEach(p => scores[p] = 0);
  currentPlayer = 0;
  setup.style.display = "none";
  game.style.display = "block";
  rollBtn.disabled = false;
  stopBtn.disabled = true;
  restartBtn.style.display = "none";
  updateTurn();
  updateScoreboard();
});

// Rolar dados
rollBtn.addEventListener("click", () => {
  resultsEl.innerHTML = "";
  for (let i = 0; i < 3; i++) {
    const die = dice[Math.floor(Math.random() * dice.length)];
    const face = die.faces[Math.floor(Math.random() * die.faces.length)];

    const p = document.createElement("p");
    p.textContent = `${die.color.toUpperCase()} → ${face}`;
    resultsEl.appendChild(p);

    if (face === "🧠") brains++;
    else if (face === "💥") shotguns++;
  }

  scoreEl.textContent = `Rodada: 🧠 ${brains} | 💥 ${shotguns}`;

  if (shotguns >= 3) {
    statusEl.textContent = "💥 Levou 3 tiros! Perdeu os cérebros da rodada.";
    endTurn(false);
  } else {
    statusEl.textContent = "Você pode continuar ou parar.";
    stopBtn.disabled = false;
  }
});

// Parar rodada
stopBtn.addEventListener("click", () => {
  endTurn(true);
});

// Reiniciar jogo
restartBtn.addEventListener("click", () => {
  setup.style.display = "block";
  game.style.display = "none";
});

// Encerrar turno
function endTurn(success) {
  if (success) {
    scores[players[currentPlayer]] += brains;
    statusEl.textContent = `✔️ ${players[currentPlayer]} guardou ${brains} cérebros!`;
  }
  updateScoreboard();

  if (scores[players[currentPlayer]] >= TARGET) {
    alert(`🏆 ${players[currentPlayer]} venceu com ${scores[players[currentPlayer]]} cérebros!`);
    rollBtn.disabled = true;
    stopBtn.disabled = true;
    restartBtn.style.display = "inline-block";
    return;
  }

  brains = 0;
  shotguns = 0;
  currentPlayer = (currentPlayer + 1) % players.length;
  updateTurn();
}

function updateTurn() {
  turnEl.textContent = `👉 Vez de: ${players[currentPlayer]}`;
  scoreEl.textContent = "Rodada: 🧠 0 | 💥 0";
  resultsEl.innerHTML = "";
  stopBtn.disabled = true;
}

function updateScoreboard() {
  scoreboardEl.innerHTML = "";
  players.forEach(p => {
    const li = document.createElement("li");
    li.textContent = `${p}: 🧠 ${scores[p]}`;
    scoreboardEl.appendChild(li);
  });
}
