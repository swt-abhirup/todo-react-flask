# 📝 Full-Stack To-Do Application  
### React (Vite) + Flask API + MySQL

A simple, clean, production-ready **full-stack To-Do application** built using:

- **React + Vite** for the frontend  
- **Flask (Python)** for the backend
- **MySQL** for database storage
- **REST API Architecture**

This project is created as part of my Full-Stack development training and portfolio preparation.

---

## 🚀 Features

### **Frontend (React + Vite)**
- Add new tasks  
- Mark tasks completed / incomplete  
- Edit existing tasks  
- Delete tasks  
- Fully responsive UI built with **Bootstrap 5**  
- API integration with Flask backend  

### **Backend (Flask API)**
- REST endpoints: `GET`, `POST`, `PUT`, `DELETE`
- MySQL database connectivity  
- Clean folder structure (`routes`, `models`, `database`)  
- Error handling & JSON responses  

### **Database (MySQL)**
- Table: `todos`
- Fields include:
  - `id` (PK)
  - `task`
  - `completed`
  - `created_at`

---

## 📁 Project Structure

todo-react-flask/
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   ├── requirements.txt
│   └── .env (ignored)
│
├── frontend/
│   ├── index.html
│   ├── vite.config.js
│   ├── package.json
│   ├── README.md
│   └── src/
│       ├── App.jsx
│       ├── main.jsx
│       ├── components/
│       │   ├── TodoForm.jsx
│       │   └── TodoList.jsx
│       └── assets/
│
├── README.md (root)
└── .gitignore
