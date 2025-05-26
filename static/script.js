document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const responseArea = document.getElementById('response-area');
    const sendBtn = document.getElementById('send-btn');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        const message = userInput.value.trim();
        if (!message) return;
        sendBtn.disabled = true;
        responseArea.textContent = 'Thinking...';
        try {
            const res = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message })
            });
            const data = await res.json();
            responseArea.textContent = data.response;
        } catch (err) {
            responseArea.textContent = 'Error: Could not reach the server.';
        } finally {
            sendBtn.disabled = false;
        }
    });
});
