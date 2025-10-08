document.addEventListener("DOMContentLoaded", function () {
    const addSubjectBtn = document.getElementById("add-subject-btn");
    const subjectsContainer = document.getElementById("subjects-container");

    if (addSubjectBtn) {
        addSubjectBtn.addEventListener("click", () => {
            const input = document.createElement("input");
            input.type = "text";
            input.name = "subjects";
            input.placeholder = "Enter subject name";
            input.classList.add("pref-input");
            subjectsContainer.appendChild(input);
        });
    }

    const addCustomMotivationBtn = document.getElementById("add-custom-motivation-btn");
    if (addCustomMotivationBtn) {
        addCustomMotivationBtn.addEventListener("click", () => {
            const input = document.createElement("input");
            input.type = "text";
            input.name = "custom_motivation";
            input.placeholder = "Enter custom motivation";
            input.classList.add("pref-input");
            addCustomMotivationBtn.insertAdjacentElement("afterend", input);
            addCustomMotivationBtn.style.display = "none";
        });
    }

    const addCustomDifficultyBtn = document.getElementById("add-custom-difficulty-btn");
    if (addCustomDifficultyBtn) {
        addCustomDifficultyBtn.addEventListener("click", () => {
            const input = document.createElement("input");
            input.type = "text";
            input.name = "custom_difficulty";
            input.placeholder = "Enter custom difficulty";
            input.classList.add("pref-input");
            addCustomDifficultyBtn.insertAdjacentElement("afterend", input);
            addCustomDifficultyBtn.style.display = "none";
        });
    }
});
