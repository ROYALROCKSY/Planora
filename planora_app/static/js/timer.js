document.addEventListener("DOMContentLoaded", () => {
  const countdownEl = document.getElementById("countdown");
  const startBtn = document.getElementById("startBtn");
  const pauseBtn = document.getElementById("pauseBtn");
  const endBtn = document.getElementById("endBtn");
  const resetBtn = document.getElementById("resetBtn");

  const subjectSelect = document.getElementById("subject");
  const totalCyclesSelect = document.getElementById("totalCycles");
  const timerPerCycleSelect = document.getElementById("timerPerCycle");
  const breakTimeSelect = document.getElementById("breakTime");

  const cyclesCompletedEl = document.getElementById("cyclesCompleted");
  const totalCyclesDisplayEl = document.getElementById("totalCyclesDisplay");
  const pauseCountEl = document.getElementById("pauseCount");
  const sessionStatusEl = document.getElementById("sessionStatus");

  let totalCycles = parseInt(totalCyclesSelect.value);
  let cyclesCompleted = 0;
  let pauseCount = 0;
  let timerPerCycle = parseInt(timerPerCycleSelect.value);
  let breakTime = parseInt(breakTimeSelect.value);

  let timer = null;
  let timeRemaining = timerPerCycle * 60;
  let startTime = null;

  // Fetch subjects from backend
  fetch(`/timer/subjects?user_id=68dc37187ffd67372e424594`)
    .then(res => res.json())
    .then(data => {
      data.subjects.forEach(s => {
        const option = document.createElement("option");
        option.value = s;
        option.textContent = s;
        subjectSelect.appendChild(option);
      });
    });

  function formatTime(seconds) {
    const m = Math.floor(seconds / 60).toString().padStart(2, "0");
    const s = (seconds % 60).toString().padStart(2, "0");
    return `${m}:${s}`;
  }

  function updateDisplay() {
    countdownEl.textContent = formatTime(timeRemaining);
    cyclesCompletedEl.textContent = cyclesCompleted;
    totalCyclesDisplayEl.textContent = totalCycles;
    pauseCountEl.textContent = pauseCount;
  }

  function startTimer() {
    if (!subjectSelect.value) {
      alert("Select a subject first!");
      return;
    }

    // Prevent multiple intervals
    if (timer) return;

    if (!startTime) startTime = new Date();
    sessionStatusEl.textContent = "In Progress";

    timer = setInterval(() => {
      timeRemaining--;
      updateDisplay();

      // Cycle completed
      if (timeRemaining <= 0) {
        cyclesCompleted++;
        if (cyclesCompleted >= totalCycles) {
          endSession("Completed");
        } else {
          timeRemaining = timerPerCycle * 60;
        }
      }
    }, 1000);
  }

  function pauseTimer() {
    if (!timer) return;
    clearInterval(timer);
    timer = null;
    pauseCount++;
    pauseCountEl.textContent = pauseCount;
    sessionStatusEl.textContent = "Paused";
  }

  function endSession(reason = "Incomplete") {
    // Stop timer
    if (timer) {
      clearInterval(timer);
      timer = null;
    }

    if (!startTime || !subjectSelect.value) return;

    const endTime = new Date();

    const sessionData = {
      user_id: "68dc37187ffd67372e424594",
      subject: subjectSelect.value,
      start_time: startTime.toISOString(),
      end_time: endTime.toISOString(),
      no_of_cycles_decided: totalCycles,
      no_of_cycles_completed: cyclesCompleted,
      break_time: breakTime,
      pause_count: pauseCount,
      timer_per_cycle: timerPerCycle,
      completion_status: reason,
    };

    fetch("/timer/save_session", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(sessionData),
    })
    .then(res => res.json())
    .then(data => console.log("Session saved:", data))
    .catch(err => console.error(err));

    sessionStatusEl.textContent = reason;

    // Reset timer variables after ending
    startTime = null;
    timeRemaining = timerPerCycle * 60;
    updateDisplay();
  }

  function resetTimer() {
    // Stop timer
    if (timer) {
      clearInterval(timer);
      timer = null;
    }

    // Reset counts
    cyclesCompleted = 0;
    pauseCount = 0;
    startTime = null;

    // Reset dropdowns to defaults
    subjectSelect.value = "";
    totalCyclesSelect.value = "4";
    timerPerCycleSelect.value = "20";
    breakTimeSelect.value = "5";

    // Update local variables
    totalCycles = parseInt(totalCyclesSelect.value);
    timerPerCycle = parseInt(timerPerCycleSelect.value);
    breakTime = parseInt(breakTimeSelect.value);
    timeRemaining = timerPerCycle * 60;

    sessionStatusEl.textContent = "Not Started";
    updateDisplay();
  }

  startBtn.addEventListener("click", startTimer);
  pauseBtn.addEventListener("click", pauseTimer);
  endBtn.addEventListener("click", () => endSession("Incomplete"));
  resetBtn.addEventListener("click", resetTimer);

  updateDisplay();
});
