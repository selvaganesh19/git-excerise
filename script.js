// Send the user input to the chatbot backend
async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
  
    if (userInput.trim() === "") return;
  
    // Display user message in the chat
    displayMessage(userInput, "user-message");
  
    // Send the message to the Flask backend
    try {
      const response = await fetch("http://127.0.0.1:5000/chatbot", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userInput })
      });
  
      const data = await response.json();
      displayMessage(data.response, "bot-message");
    } catch (error) {
      displayMessage("Error connecting to the chatbot.", "bot-message");
    }
  
    // Clear the input field
    document.getElementById("user-input").value = "";
  }
  
  // Function to display a message in the chat box
  function displayMessage(message, className) {
    const chatBox = document.getElementById("chat-box");
    const messageElement = document.createElement("div");
    messageElement.className = `message ${className}`;
    messageElement.innerText = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
  }
  