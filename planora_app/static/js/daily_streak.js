document.addEventListener("DOMContentLoaded", async () => {
    const streakEl = document.getElementById("daily-streak-count");
    const missedEl = document.getElementById("daily-streak-missed");
    const msgEl = document.getElementById("daily-streak-msg");

    // For now, fallback user_id from URL or hardcoded
    const urlParams = new URLSearchParams(window.location.search);
    const userId = urlParams.get("user_id") || "68dc37187ffd67372e424594";

    try {
        const res = await fetch(`/cards/daily-streak?user_id=${userId}`);
        const data = await res.json();

        if (res.ok) {
            const streak = data.streak || 0;
            const missed = data.missed || 0;
            const msg = data.message || "";

            // ✅ Handle pluralization
            streakEl.textContent = `${streak} ${streak === 1 ? "day" : "days"}`;
            missedEl.textContent = missed;
            msgEl.textContent = msg;
        } else {
            streakEl.textContent = "0 days";
            missedEl.textContent = 0;
            msgEl.textContent = "Error fetching streak";
        }
    } catch (err) {
        console.error(err);
        streakEl.textContent = "0 days";
        missedEl.textContent = 0;
        msgEl.textContent = "Error fetching streak";
    }
});
