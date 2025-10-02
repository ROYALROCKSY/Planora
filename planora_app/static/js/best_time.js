async function fetchBestTime() {
    // Get user_id from session (or URL fallback for testing)
    const urlParams = new URLSearchParams(window.location.search);
    const userIdFromUrl = urlParams.get("user_id");  

    // Call backend; backend already handles session/fallback
    try {
        const res = await fetch(`/cards/best-time${userIdFromUrl ? `?user_id=${userIdFromUrl}` : ""}`);
        const data = await res.json();

        if (res.ok && data.best_time) {
            document.getElementById("peak-focus-time").textContent = data.best_time;
        } else {
            console.error("Failed to fetch best time:", data.error);
            document.getElementById("peak-focus-time").textContent = "Error fetching time";
        }
    } catch (err) {
        console.error("Error fetching best time:", err);
        document.getElementById("peak-focus-time").textContent = "Error fetching time";
    }
}

window.addEventListener("DOMContentLoaded", fetchBestTime);
