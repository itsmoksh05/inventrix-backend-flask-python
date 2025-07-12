# 🧠 Inventrix – Flask + MongoDB Backend API

Inventrix is a backend RESTful API built with **Flask** and **MongoDB**, designed for managing users, inventory items, and admin operations. This app uses a modular architecture and follows clean coding practices with Pydantic validation, password hashing, and automated testing.

---

## 📦 Tech Stack

- **Python** + **Flask**
- **MongoDB** with `pymongo`
- **Pydantic** for data validation
- **Werkzeug Security** for password hashing
- **pytest** for automated testing
- **Modular Project Structure**
- **No templates** (API-only backend)

---

## 🧱 Project Structure

```
inventrix-backend/
├── app/
│   ├── __init__.py
│   ├── routes/                # Route blueprints
│   ├── services/              # Business logic
│   ├── models/                # Pydantic data models
│   ├── utils/                 # Helper utils (hashing, serializers)
│   └── database/              # MongoDB connection
│
├── tests/                     # pytest test cases
├── run.py                     # Entry point
├── requirements.txt
└── README.md
└── .gitignore
```

---

## 🚀 Features

### 👤 User Module (`/api/auth`)
- `POST /register` – Register a new user
- `POST /login` – User login with credential check
- `GET /me/<username>` – Fetch current user profile

### 📦 Item Module (`/api/items`)
- `POST /` – Add new item (auto `added_on`)
- `GET /` – Get all items
- `GET /<id>` - Get item by id
- `Get /<name>` - Get item by name
- `PUT /<id>` – Update item by ID
- `DELETE /<id>` – Delete item by ID

### 🔐 Admin Module (`/api/admin`)
- `GET /users` – View all users
- `GET /user/<id>` – View user by ID
- `DELETE /user/<id>` – Delete user by ID

---

## 🔐 Security

- Passwords are securely stored using `werkzeug.security` hashing (`generate_password_hash`)
- Duplicate checks on `username` and `email`
- Clean exception handling and validation

---

## 🧪 Testing

Run all tests using:

```bash 
pytest
```

Test modules cover:
- User registration/login
- Item CRUD operations
- Admin routes

---

## ⚙️ Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/itsmoksh05/inventrix-backend-flask-python.git
cd inventrix-backend
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate    # For Linux/Mac
.venv\Scripts\activate       # For Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the app**
```bash
python run.py
```

Make sure MongoDB is running locally or update your DB URI in `db_conn.py`.

---

## ✅ Example JSON Payloads

### 🔹 Register User

```json
POST /api/auth/register
{
  "username": "moksh",
  "email": "moksh@example.com",
  "password": "test123",
  "role": "USER"
}
```

### 🔹 Add Item

```json
POST /api/items/
{
  "name": "Laptop",
  "user_name": "moksh",
  "quantity": 5,
  "image_url": null,
  "expiry_date": "2025-12-31",
  "category_name": "Electronics"
}
```

---

## ✨ Author

**Moksh Patel**  
📧 mokshpokar98@gmail.com  
🌐 https://linkedin.com/in/itsmoksh05

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
