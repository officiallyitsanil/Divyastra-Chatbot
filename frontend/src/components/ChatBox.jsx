import { useState } from "react";

function ChatBox() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMessage = { sender: "You", text: input };
    setMessages((prev) => [...prev, userMessage]);

    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input })
    });

    const data = await res.json();
    const botMessage = { sender: "Divyastra", text: data.response };
    setMessages((prev) => [...prev, botMessage]);
    setInput("");
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Chat with Divyastra</h2>
      <div style={{ height: 400, overflowY: "auto", border: "1px solid #ccc", padding: 10 }}>
        {messages.map((msg, i) => (
          <div key={i}><strong>{msg.sender}:</strong> {msg.text}</div>
        ))}
      </div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        placeholder="Ask anything..."
        style={{ width: "80%", padding: 8, marginTop: 10 }}
      />
      <button onClick={sendMessage} style={{ padding: 8, marginLeft: 10 }}>Send</button>
    </div>
  );
}

export default ChatBox;