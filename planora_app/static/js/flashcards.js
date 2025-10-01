// static/js/flashcards.js

const uploadInput = document.getElementById("doc-upload");
const uploadBtn = document.querySelector(".upload-btn");
const flashcardStage = document.querySelector(".flashcard-stage");
const flashcardContent = document.getElementById("flashcard-content");
const flashLeft = document.getElementById("flash-left");
const flashRight = document.getElementById("flash-right");

let flashcards = [];
let currentIndex = 0;

// Default flashcard color palette
const defaultColors = [
  "linear-gradient(135deg, #ede9fe, #f7f6ff)", // lavender
  "linear-gradient(135deg, #fce7f3, #fff7fb)", // blush
  "linear-gradient(135deg, #eaf8f0, #ffffff)", // mint
  "linear-gradient(135deg, #ffe5e5, #fff0f0)"  // pinkish
];

// Update flashcard display
function updateFlashcard() {
  if (flashcards.length === 0) {
    flashcardContent.textContent = "No flashcards yet. Upload a document to generate.";
    flashcardStage.style.background = "linear-gradient(135deg, #f0f0f0, #ffffff)";
    return;
  }

  const card = flashcards[currentIndex];
  // Show content in bold, no numbering
  flashcardContent.innerHTML = "<strong>" + card.text + "</strong>";
  flashcardStage.style.background = card.color || defaultColors[currentIndex % defaultColors.length];
}

// Navigate flashcards
flashRight.addEventListener("click", () => {
  if (flashcards.length === 0) return;
  currentIndex = (currentIndex + 1) % flashcards.length;
  updateFlashcard();
});

flashLeft.addEventListener("click", () => {
  if (flashcards.length === 0) return;
  currentIndex = (currentIndex - 1 + flashcards.length) % flashcards.length;
  updateFlashcard();
});

// Upload file and generate flashcards
uploadBtn.addEventListener("click", async () => {
  const file = uploadInput.files[0];
  if (!file) return alert("Please select a file first.");

  const formData = new FormData();
  formData.append("file", file);
  // Temporary hardcoded user_id
  formData.append("user_id", "68dc37187ffd67372e424594");

  try {
    const res = await fetch("/flashcards/upload", {
      method: "POST",
      body: formData
    });

    const data = await res.json();

    if (res.ok) {
      if (!data.flashcards || data.flashcards.length === 0) {
        alert("No flashcards were generated from this document.");
        return;
      }

      // Clean flashcard content: remove any "Flashcard X:" prefix
      flashcards = data.flashcards.map((fc, index) => {
        let text = fc.text || "";

        // Remove "Flashcard 1:" or "1." prefixes
        if (text.includes(":")) {
          const parts = text.split(":");
          if (parts[0].trim().toLowerCase().startsWith("flashcard") || /^\d+$/.test(parts[0].trim())) {
            text = parts.slice(1).join(":").trim();
          }
        }

        return {
          text,
          color: defaultColors[index % defaultColors.length]
        };
      });

      currentIndex = 0;
      updateFlashcard();
      alert("Flashcards generated!");
    } else {
      alert("Upload failed: " + data.error);
    }
  } catch (err) {
    console.error(err);
    alert("Upload failed: " + err.message);
  }
});

// Initialize empty flashcard stage
updateFlashcard();
