
🛒   E-commerce Chatbot

   A full-stack application designed to provide a conversational interface for searching and viewing e-commerce products. This project seamlessly integrates a React.js frontend with a Flask REST API backend, backed by a SQLite database.


---
 
 📐 Project Architecture

  Frontend (React.js) ↔ Axios ↔ Backend (Flask) ↔ SQLite (via SQLAlchemy)

-> **Frontend**: React app with components for the chatbot and product cards.
-> **Backend**: Flask API that serves product data from a SQLite database.
-> **Database**: SQLite database seeded with mock e-commerce products.

---


✨ Features
1. Interactive Chatbot: Engage with a conversational agent to query products.
2. Product Search: Efficiently find products by name (e.g., "Laptop", "Smartphone").
3. Dynamic Display: View search results presented as intuitive product cards.
4. Scalable Architecture: Built on a modern, decoupled tech stack.
5. Mock Data Integration: Pre-populated database for immediate testing and demonstration.

---


🛠️ Technologies Used

| Layer      | Technology     | Purpose                              |
|------------|----------------|--------------------------------------|
| Frontend   | React.js       | Building the user interface          |
| Backend    | Flask          | REST API to serve product data       |
| Database   | SQLite         | Simple and lightweight data storage  |
| ORM        | SQLAlchemy     | Object-relational mapping            |
| CORS       | flask-cors     | Enabling frontend-backend requests   |
| Styling    | CSS            | Basic visual design                  |
| HTTP Client| Axios          | API requests from frontend           |
| Bundler    | Parcel         | Build and serve the frontend         |

---
## 📂 Project Structure


ecommerce-chatbot/
├── backend/
│   ├── app.py
│   ├── models.py
│   └── ecommerce.db
├── frontend/
│   ├── src/
│   │   ├── index.js
│   │   ├── api.js
│   │   └── components/
│   │       ├── ChatBot.js
│   │       └── ProductCard.js
│   └── index.html
├── README.md


---

🧪 Mock Data Used

The project includes a seed_db() function in backend/app.py that populates the SQLite database with a predefined set of mock product data.
This allows for immediate testing without manual data entry.

```python
 sample_products = [
    {"name": "Laptop", "description": "Gaming laptop with 16GB RAM", "price": 99999},
    {"name": "Laptop", "description": "Asus TUF gaming with 16GB RAM", "price": 105000},
    {"name": "Laptop", "description": "Asus Rog Strix g16-RTX 4060", "price": 200000},
    {"name": "Smartphone", "description": "S23 Ultra ", "price": 125000},
    #....more Products
  ]

```
We can update these inside `backend/app.py` under the `seed_db()` function.


---

⚖ Challenges and Resolutions

Throughout the development of this project, several common full-stack integration challenges were addressed:

1. CORS Errors: Initial attempts to connect the frontend to the backend were hindered by Cross-Origin Resource Sharing (CORS) security policies.
   Solution: Integrated flask-cors into the Flask application to properly configure and manage CORS headers, allowing legitimate cross-origin requests.

2. Database Seeding Issues: The database was not consistently seeding with mock data upon application startup.
   Solution: Implemented db.create_all() and database seeding logic within Flask's application context (app.app_context()) to ensure the database schema and initial data are correctly established.

3. Undefined API Responses: The frontend was occasionally receiving undefined or malformed data from the API.
   Solution: Implemented robust input validation on the backend and added fallback handling on the frontend to gracefully manage unexpected or missing data, improving overall application stability.


---

@ How to Run the Project

 🔙 Backend

```bash
cd backend
pip install flask flask-cors flask-sqlalchemy
python app.py
```

 🔜 Frontend

```bash
cd frontend
npm install
npm run start
```

Then, open browser at: `http://localhost:1234`

---

🤖 Chatbot Usage

Once both the backend and frontend are running:
1. Open your web browser and navigate to http://localhost:1234.
2. In the chatbot interface, type product names or keywords like:

  - Laptop
  - Smartphone
  - Headphones
  - Camera
  - Smartwatch
  - Tablet
  - Bluetooth Speaker
  - Wireless Mouse
  - Keyboard
The chatbot will process your query and display matching products from the database.

---

📈 Improvements Possible

- Addinng user login and cart
- Adding more items in databases 
- More Improved UI
  
 ---

🎡 Key Learnings

  Developing this E-commerce Product Assistant provided valuable insights into:

- Building a complete full-stack application from scratch, understanding the flow between client, server, and database.
- Establishing seamless communication protocols between distinct frontend (React) and backend (Flask) technologies.
- The critical importance of robust error handling and clear error messaging for both developers and end-users.
- Setting up and managing a lightweight yet effective RESTful API using Flask.
- Designing and implementing intuitive, reactive user interfaces with React.js that respond dynamically to user input and data changes.

