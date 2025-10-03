document.addEventListener("DOMContentLoaded", () => {
  const notesList = document.getElementById("notesList");
  const noteSearch = document.getElementById("noteSearch");
  const filterType = document.getElementById("filterType");
  const filterDate = document.getElementById("filterDate");
  const filterMonth = document.getElementById("filterMonth");
  const filterYear = document.getElementById("filterYear");
  const applyFilter = document.getElementById("applyFilter");

  let allNotes = [];

  // Fetch notes
  function fetchNotes(filterTypeValue = "", filterValue = "") {
    fetch(`/notes/fetch?user_id=${USER_ID}&filter_type=${filterTypeValue}&filter_value=${filterValue}`)
      .then(res => res.json())
      .then(data => {
        allNotes = data.notes;
        renderNotes(allNotes);
      });
  }

//   function renderNotes(notes) {
//     notesList.innerHTML = "";
//     notes.forEach(note => {
//       const li = document.createElement("li");
//       li.className = "note-item";
//       li.dataset.id = note._id;
//       li.innerHTML = `
//         <div class="note-text" title="Double click to expand">
//           ${note.snippet}
//         </div>
//         <div class="note-meta">
//           <span>${note.created_at}</span>
//           <span class="star" style="cursor:pointer">${note.starred ? "★" : "☆"}</span>
//         </div>
//       `;

//       // Double click to expand
//       li.querySelector(".note-text").addEventListener("dblclick", () => {
//         li.querySelector(".note-text").textContent = note.text;
//       });

//       // Star toggle
//       li.querySelector(".star").addEventListener("click", () => {
//         const newStar = !note.starred;
//         fetch("/notes/toggle_star", {
//           method: "POST",
//           headers: {"Content-Type":"application/json"},
//           body: JSON.stringify({note_id: note._id, starred: newStar})
//         }).then(() => {
//           note.starred = newStar;
//           li.querySelector(".star").textContent = newStar ? "★" : "☆";
//         });
//       });

//       notesList.appendChild(li);
//     });
//   }


function renderNotes(notes) {
    notesList.innerHTML = "";
    notes.forEach(note => {
      const li = document.createElement("li");
      li.className = "note-item";
      li.dataset.id = note._id;

      // Create snippet if note has more than 35 words
      const snippet = note.text.split(" ").length > 35
        ? note.text.split(" ").slice(0, 35).join(" ") + "..."
        : note.text;

      li.innerHTML = `
        <div class="note-text" title="Double click to expand">
          ${snippet}
        </div>
        <div class="note-meta">
          <span>${note.created_at}</span>
          <span class="star" style="cursor:pointer">${note.starred ? "★" : "☆"}</span>
        </div>
      `;

      // Double click to toggle full text
      li.querySelector(".note-text").addEventListener("dblclick", () => {
        const textDiv = li.querySelector(".note-text");
        if(textDiv.textContent === snippet){
          textDiv.textContent = note.text; // show full note
        } else {
          textDiv.textContent = snippet;   // collapse back to snippet
        }
      });

      // Star toggle
      li.querySelector(".star").addEventListener("click", () => {
        const newStar = !note.starred;
        fetch("/notes/toggle_star", {
          method: "POST",
          headers: {"Content-Type":"application/json"},
          body: JSON.stringify({note_id: note._id, starred: newStar})
        }).then(() => {
          note.starred = newStar;
          li.querySelector(".star").textContent = newStar ? "★" : "☆";
        });
      });

      notesList.appendChild(li);
    });
  }




  // Search notes
  noteSearch.addEventListener("input", () => {
    const term = noteSearch.value.toLowerCase();
    const filtered = allNotes.filter(n => n.text.toLowerCase().includes(term));
    renderNotes(filtered);
  });

  // Filter type show/hide
  filterType.addEventListener("change", () => {
    filterDate.style.display = filterType.value === "date" ? "inline-block" : "none";
    filterMonth.style.display = filterType.value === "month" ? "inline-block" : "none";
    filterYear.style.display = filterType.value === "year" ? "inline-block" : "none";
  });

  applyFilter.addEventListener("click", () => {
    let val = "";
    if(filterType.value === "date") val = filterDate.value;
    else if(filterType.value === "month") val = filterMonth.value;
    else if(filterType.value === "year") val = filterYear.value;

    fetchNotes(filterType.value, val);
  });

  // Initial fetch
  fetchNotes();
});
