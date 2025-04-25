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
flask-api-boilerplate/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── models/
│   │   └── user.py
│   ├── routes/
│   │   ├── __init__.py
|   |   ├── health_check.py
│   │   └── user_routes.py
│   └── services/
│       └── user_services.py
├── instance/app.db
├── .env
├── requirements.txt
└── run.py
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/pull3t/flask-api-boilerplate.git
cd flask-api-boilerplate
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root:
```
FLASK_APP=app:create_app
FLASK_ENV=development
SECRET_KEY=yB9k0u8cdRkHe_HVAsdYdFeJKYVE6M2zM4Q4NGJZ3zvA
DATABASE_URI=sqlite:///app.db
```

### 5. Run the App
```bash
deactivate # venv needs to be re-activated to load .env config
source venv/bin/activate  # On Windows: venv\Scripts\Activate.ps1
flask run
```

---

## 🧪 API Endpoints

### 📍 Health Check
```
GET /api/health_check
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