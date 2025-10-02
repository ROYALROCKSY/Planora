document.addEventListener("DOMContentLoaded", async () => {
    const subjectEl = document.getElementById("priority-subject");
    const reasonEl = document.getElementById("priority-reason");

    try {
        const res = await fetch("/cards/priority-focus");
        const data = await res.json();

        if (res.ok) {
            subjectEl.textContent = data.subject || "No recommendation";
            reasonEl.textContent = data.reason || "";
        } else {
            subjectEl.textContent = "Error fetching recommendation";
            reasonEl.textContent = data.error || "";
        }
    } catch (err) {
        console.error(err);
        subjectEl.textContent = "Error fetching recommendation";
        reasonEl.textContent = err.message;
    }
});
