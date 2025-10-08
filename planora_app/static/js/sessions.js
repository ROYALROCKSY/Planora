document.addEventListener("DOMContentLoaded", () => {
  const sessionsList = document.getElementById("sessionsList");
  const filterType = document.getElementById("filterType");
  const filterDate = document.getElementById("filterDate");
  const filterMonth = document.getElementById("filterMonth");
  const filterYear = document.getElementById("filterYear");
  const filterSubject = document.getElementById("filterSubject");
  const applyFilter = document.getElementById("applyFilter");

  let allSessions = [];

  function fetchSessions(filterTypeValue = "", filterValue = "") {
    fetch(`/sessions/fetch?user_id=${USER_ID}&filter_type=${filterTypeValue}&filter_value=${filterValue}`)
      .then(res => res.json())
      .then(data => {
        allSessions = data.sessions;
        renderSessions(allSessions);
      });
  }

  function renderSessions(sessions) {
    sessionsList.innerHTML = "";
    sessions.forEach(sess => {
      const li = document.createElement("li");
      li.className = "session-item";
      li.dataset.id = sess._id;

      li.innerHTML = `
        <div class="session-text">
          <strong>${sess.subject}</strong> — ${sess.studied_hrs} hrs (${sess.cycles} cycles)
        </div>
        <div class="session-meta">
          <span>${sess.date} | Start: ${sess.start_time}</span>
        </div>
      `;

      sessionsList.appendChild(li);
    });
  }

  // Filter type show/hide
  filterType.addEventListener("change", () => {
    filterDate.style.display = filterType.value === "date" ? "inline-block" : "none";
    filterMonth.style.display = filterType.value === "month" ? "inline-block" : "none";
    filterYear.style.display = filterType.value === "year" ? "inline-block" : "none";
    filterSubject.style.display = filterType.value === "subject" ? "inline-block" : "none";
  });

  applyFilter.addEventListener("click", () => {
    let val = "";
    if(filterType.value === "date") val = filterDate.value;
    else if(filterType.value === "month") val = filterMonth.value;
    else if(filterType.value === "year") val = filterYear.value;
    else if(filterType.value === "subject") val = filterSubject.value;

    fetchSessions(filterType.value, val);
  });

  // Initial fetch
  fetchSessions();
});
