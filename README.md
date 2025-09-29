# BOOK_IT SITE
This is a booking site where registered and logged in users can make,delete,udate and access bookings of available book.
Admins



## 🏗️ Architectural Decisions
This is modular backend service design for managing books, users, and related services.  
This seperates layers for `models/`, `services/`, `routes/`, `crud/` and `schema/`).

---

- **Framework**: FastAPI → lightweight, async, great for APIs.  
- **ORM**: SQLModel (built on SQLAlchemy) → type-safe models and migrations.  
- **Database**: PostgreSQL → chosen for reliability, scalability, and support on Render.  
- **Deployment**: Render Web Service → auto-deploy from GitHub with managed Postgres.  
- **Architecture**: Modular design (separate layers for `models/`, `services/`, `routes/`, `crud/` and `schema/`).

---

## 🗄️ Database Architecture

- **Users Table** → Stores user accounts and authentication details.  
- **Books Table** → Each book belongs to a user (via foreign key).  
- **Services Table** → Defines additional features tied to books or users.  


---

## ⚙️ How to Run Locally

### 1. Clone Repository
```bash
git clone https://github.com/naecherem20/BOOKIT.git
cd BOOKIT
```
---
### 2. Create and Activate Virtual Environment
```
python -m venv env
source env/bin/activate  # On Linux/Mac
env\Scripts\activate     # On Windows
```
### 3. Install Dependencies
```pip install -r requirements.txt```
###4.Setup Env Variables
```
DATABASE_URL=postgresql+psycopg2://postgres:kantel-pp20@localhost:5432/BOOKIT
SECRET_KEY= #secret key
ALGORITHM=HS256
 ```
### 4.Run Database Migrations
```
python -m main  # or ensure metadata.create_all(engine) runs once
```
### 5. Run Server
```
uvicorm main:app --reload
```
### 6.Environment Variable

| Variable       | Description                    | Example                                   |
| -------------- | ------------------------------ | ----------------------------------------- |
| `DATABASE_URL` | Connection string for Postgres | `postgresql://user:pass@host:5432/bookit` |
| `SECRET_KEY`   | Secret key for auth/session(run openssl rand -hex 32| `supersecretkey`                          |
| `DEBUG`        | Debug mode toggle (True/False) | `True`                                    |




