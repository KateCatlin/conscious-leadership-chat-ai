document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const responseArea = document.getElementById('response-area');
    const sendBtn = document.getElementById('send-btn');
    const loadingPlaceholder = document.getElementById('loading-placeholder');
    const responseMessage = document.getElementById('response-message');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        const message = userInput.value.trim();
        if (!message) return;

        // Show response area and typing animation
        responseArea.classList.remove("hidden");
        loadingPlaceholder.classList.add("visible"); // Show animated dots
        responseMessage.classList.add("hidden"); // Hide response bubble
        responseMessage.textContent = ""; // Clear previous response
        sendBtn.disabled = true;

        try {
            const res = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message })
            });
            const data = await res.json();

            // Hide typing animation and show response
            loadingPlaceholder.classList.remove("visible"); // Hide animated dots
            responseMessage.classList.remove("hidden"); // Show response bubble
            responseMessage.textContent = data.response.replace(/principles/gi, "commitments");
        } catch (err) {
            loadingPlaceholder.classList.remove("visible"); // Hide animated dots
            responseMessage.classList.remove("hidden"); // Show response bubble
            responseMessage.textContent = 'Error: Could not reach the server.';
        } finally {
            sendBtn.disabled = false;
        }
    });
});
