const chatBody = document.querySelector("#chatbot-body");
const chatInput = document.querySelector(".chat-input");
const chatSend = document.querySelector(".chat-send");

// Hardcode user_id for now (from MongoDB)
const USER_ID = "68dc37187ffd67372e424594"; // replace with your actual ObjectId

// Scroll to bottom
function scrollToBottom() {
  chatBody.scrollTop = chatBody.scrollHeight;
}

// Create message bubble
function createMessage(content, type = "user") {
  const msg = document.createElement("div");
  msg.classList.add("chat-message", type);

  const textSpan = document.createElement("span");
  textSpan.classList.add("chat-text");
  textSpan.textContent = content;
  msg.appendChild(textSpan);

  // Save button (hidden by default)
  const saveBtn = document.createElement("span");
  saveBtn.classList.add("save-btn");
  saveBtn.textContent = " Save";
  saveBtn.style.display = "none";
  msg.appendChild(saveBtn);

  // Text selection
  textSpan.addEventListener("mouseup", () => {
    const selection = window.getSelection().toString().trim();
    if (selection.length > 0) {
      msg.classList.add("selected");
      saveBtn.style.display = "inline-block";
      saveBtn.dataset.selectedText = selection;
    } else {
      msg.classList.remove("selected");
      saveBtn.style.display = "none";
    }
  });

  // Save button click
  saveBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    const selectedText = saveBtn.dataset.selectedText;
    if (selectedText && selectedText.length > 0) {
      console.log("Saved text:", selectedText);
      alert("Message saved!");
      saveBtn.style.display = "none";
      msg.classList.remove("selected");
      window.getSelection().removeAllRanges();
    }
  });

  chatBody.appendChild(msg);
  scrollToBottom();
  return msg;
}

// Initial placeholder
const initialPlaceholder = document.createElement("div");
initialPlaceholder.classList.add("chat-empty");
initialPlaceholder.textContent = "Hello, want me to help you with something?";
initialPlaceholder.style.textAlign = "center";
initialPlaceholder.style.marginTop = "50%";
chatBody.appendChild(initialPlaceholder);

// Send message to backend
async function sendMessage() {
  const text = chatInput.value.trim();
  if (!text) return;

  if (chatBody.contains(initialPlaceholder)) initialPlaceholder.remove();

  createMessage(text, "user");
  chatInput.value = "";

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: USER_ID, message: text })
    });

    const data = await res.json();

    if (res.ok) {
      createMessage(data.reply, "bot");
    } else {
      createMessage("Error: " + data.error, "bot");
    }
  } catch (err) {
    console.error(err);
    createMessage("Error connecting to server", "bot");
  }
}

// Event listeners
chatSend.addEventListener("click", sendMessage);
chatInput.addEventListener("keydown", (e) => { if (e.key === "Enter") sendMessage(); });


// -----------------
