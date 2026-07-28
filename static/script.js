let sessionId = null;

const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const chatMessages = document.getElementById('chat-messages');

chatForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const message = userInput.value.trim();
  if (!message) return;

  // Append user message
  appendMessage(message, 'user-message');
  userInput.value = '';

  // Show temporary loading response
  const loadingDiv = appendMessage('Typing...', 'bot-message');

  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message, session_id: sessionId })
    });

    const data = await response.json();
    if (response.ok) {
      sessionId = data.session_id;
      loadingDiv.textContent = data.response;
    } else {
      loadingDiv.textContent = "Error: " + (data.detail || "Unable to get response.");
    }
  } catch (error) {
    loadingDiv.textContent = "Error connecting to backend server.";
  }
});

function appendMessage(text, className) {
  const msgDiv = document.createElement('div');
  msgDiv.className = `message ${className}`;
  msgDiv.textContent = text;
  chatMessages.appendChild(msgDiv);
  chatMessages.scrollTop = chatMessages.scrollHeight;
  return msgDiv;
}