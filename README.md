# Flask API Boilerplate

A clean and modular Flask REST API boilerplate using SQLAlchemy, UUID-based user model, SQLite database, and OpenAPI-ready structure. Includes:

- ✅ Health check endpoint
- 👤 Basic user CRUD (Create, Read, Update, Delete)
- 🧱 SQLite database with SQLAlchemy ORM
- 🧪 Compatible with Postman for easy API testing
- 🪝 Blueprint architecture for clean route organization
- 🌐 Ready for OpenAPI/Swagger extension

---

## 📁 Project Structure

```
flask-boilerplate/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── models/
│   │   └── user.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── user_routes.py
│   └── services/
│       └── user_services.py
├── migrations/
├── .env
├── requirements.txt
└── run.py
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/flask-boilerplate.git
cd flask-boilerplate
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root:
```
SECRET_KEY=your_secret_key_here
FLASK_ENV=development
```

### 5. Run the App
```bash
flask db upgrade  # Initializes the SQLite database
flask run
```

---

## 🧪 API Endpoints

### 📍 Health Check
```
GET /api/health
Response: { "status": "ok", "message": "API is healthy" }
```

### 👤 User CRUD

#### ➕ Create User
```
POST /api/users
Body:
{
  "username": "example_user"
}
```

#### 🔍 Get User
```
GET /api/users/<user_id>
```

#### 🧾 List All Users
```
GET /api/users
```

#### ✏️ Update User
```
PUT /api/users/<user_id>
Body:
{
  "username": "new_username"
}
```

#### ❌ Delete User
```
DELETE /api/users/<user_id>
```

---