

// Importing necessary components
import React, { useState } from "react";
import { searchProducts } from "../api"; // Function to call backend API 
import ProductCard from "./ProductCard"; // Component to display individual product info


const ChatBot = () => {    // ChatBot component for product search assistant
 
  const [messages, setMessages] = useState([]);  // State to store the messages exchanged between the user and the bot

  // State to track the current user query input
  const [query, setQuery] = useState("");

  // Function to handle sending a query and receiving product results
  const handleSend = async () => {
    if (!query.trim()) return; 

    // Calls the backend API to get products matching the search
    const products = await searchProducts(query);

    // Update the chat history with user input and bot response
    setMessages([
      ...messages,
      { sender: "user", text: query }, // Adds user message
      {
        sender: "bot",
        text: products.length
          ? "Here are the products I found:" 
          : "No products found.", 
        products, 
      },
    ]);

    // Clear the input field after sending
    setQuery("");
  };

  // JSX to render the chat interface
  return (
    <div className="chat-container"> {/* Container for the chatbot UI */}
      <h2 className="chat-title">🛒Chatbot</h2> {/* Heading */}

      

      <div className="chatbox"> {/* Display chat messages */}
        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.sender}`}> 
            {msg.sender === "bot" ? (
              <>
                <p className="bot-text">{msg.text}</p> 
                {msg.products &&
                  msg.products.map((p) => (
                    <ProductCard key={p.id} product={p} /> // Display each product found
                  ))}
              </>
            ) : (
              <p className="user-text"> 🔍︎ {msg.text}</p> // Show user message
            )}
          </div>
        ))}
      </div>

      <div className="input-area"> {/* Input and send button */}
        <input
          type="text"
          value={query}
          placeholder="Search products like laptop, phone..."
          onChange={(e) => setQuery(e.target.value)} // Updates query state on input
        />
        <button onClick={handleSend}>Send</button> {/* search */}
      </div>
    </div>
  );
};

export default ChatBot; // Export component for use in the app
