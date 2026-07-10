# HelpDesk Pro

A full-stack Help Desk Ticket Management System built with **Flask**, **SQLite**, **SQLAlchemy**, and **Bootstrap**. This application allows users to create, manage, and track support tickets while providing administrators with tools to manage ticket status and monitor support operations.

---

## Features

### User Features

* User Registration and Login
* Secure Password Hashing
* User Authentication with Flask-Login
* Dashboard with ticket statistics
* Create support tickets
* View all submitted tickets
* View detailed ticket information
* Track ticket status
* Logout functionality

### Admin Features

* Admin Dashboard
* View all user tickets
* Update ticket status
* Search tickets
* Filter tickets by status
* Role-based access control

---

## Tech Stack

### Backend

* Python 3
* Flask
* Flask-SQLAlchemy
* Flask-Login
* SQLite

### Frontend

* HTML5
* Bootstrap 5
* Jinja2 Templates

### Database

* SQLite

### Version Control

* Git
* GitHub

---

## Project Structure

```text
HelpDesk-Pro/
│
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
│
├── models/
│   ├── user.py
│   └── ticket.py
│
├── routes/
│   ├── auth.py
│   └── tickets.py
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── tickets.html
│   ├── create_ticket.html
│   └── ticket_detail.html
│
├── static/
│
└── instance/
    └── helpdesk.db
```

## Installation

Clone the repository

```bash
git clone https://github.com/laksh-1901/HelpDesk-Pro.git
```

Move into the project directory

```bash
cd HelpDesk-Pro
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser and visit

```text
http://127.0.0.1:5000
```

---

## Application Workflow

1. Register a new account.
2. Login securely.
3. Create support tickets.
4. View your tickets from the dashboard.
5. Track ticket status.
6. Admin users can manage and update ticket status.

---

## Security Features

* Password hashing using Werkzeug
* Session management with Flask-Login
* Authentication-protected routes
* Role-based authorization
* SQLAlchemy ORM to help prevent SQL injection

---

## Future Improvements

* Email notifications
* Ticket comments
* File attachments
* Password reset
* User profile management
* REST API
* Docker support
* PostgreSQL support
* Dashboard analytics and charts
* Responsive mobile interface

---

## Skills Demonstrated

* Python Programming
* Flask Web Development
* Authentication & Authorization
* CRUD Operations
* SQLAlchemy ORM
* Database Design
* MVC Project Structure
* Bootstrap UI Development
* Git & GitHub
* Software Design Principles

---

## Author

**Dhanalakshmi P**

GitHub: https://github.com/laksh-1901

---

## License

This project is created for educational purposes and portfolio demonstration.
