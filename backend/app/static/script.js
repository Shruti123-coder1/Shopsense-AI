const chat = document.getElementById("chat");

// Add default welcome message when chat opens
function addWelcomeMessage() {
    const welcomeMsg = document.createElement("p");
    welcomeMsg.classList.add("bot");
    welcomeMsg.innerHTML = "<b>Bot:</b> Hello! How can I help you today?";
    chat.appendChild(welcomeMsg);
    chat.scrollTop = chat.scrollHeight;
}

// Call welcome message on page load
window.onload = addWelcomeMessage;

function sendMessage() {
    let userText = document.getElementById("msg").value.trim();
    if(userText === "") return;  // ignore empty messages

    // Show user message
    let userMsg = document.createElement("p");
    userMsg.classList.add("user");
    userMsg.innerHTML = "<b>You:</b> " + userText;
    chat.appendChild(userMsg);

    chat.scrollTop = chat.scrollHeight;

    // Send message to server
    fetch("/chat?msg=" + encodeURIComponent(userText))
        .then(response => response.text())
        .then(data => {
            let botMsg = document.createElement("p");
            botMsg.classList.add("bot");
            botMsg.innerHTML = "<b>Bot:</b> " + data;
            chat.appendChild(botMsg);
            chat.scrollTop = chat.scrollHeight;
        });

    document.getElementById("msg").value = "";
}

// Send message on Enter key
document.getElementById("msg").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});
