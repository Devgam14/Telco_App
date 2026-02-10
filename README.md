# 📡 Telco Terminal Application

A terminal-based telecommunications management system built with **Python** using a **procedural and modular programming approach**.  
The application simulates core telecom operations such as airtime recharge, data bundle purchase, calls, SMS, and user account management, all within a terminal environment.

The system uses **PyDAL** as a database abstraction layer over an SQL database.

---

## 🚀 Project Overview

This project demonstrates how real-world telecom operations can be implemented in a **command-line application without object-oriented programming (OOP)**, focusing instead on:
- Functions
- Modules
- Clear separation of responsibilities

It emphasizes simplicity, clarity, and correctness while still modeling realistic system behavior.

---

## 🧱 Architecture

**Application Type:** Terminal-based (CLI)  
**Programming Style:** Procedural / Modular  
**Language:** Python  
**Database:** SQLite (via PyDAL ORM)  

### Architectural Layers
- **Presentation Layer** – Terminal menus and formatted output
- **Service Layer** – Functional business logic
- **Data Layer** – Database operations via PyDAL
- **Core Utilities** – Session handling and configuration

---

## 📁 Project Structure

```
telco_app/
├── main.py
├── core/
│   ├── session.py
│   └── constants.py
├── auth/
│   └── auth_service.py
├── services/
│   ├── user_services.py
│   ├── telco_services.py
│   └── admin_services.py
├── database/
│   ├── db.py
│   └── models.py
├── utils/
│   ├── display.py
│   ├── validators.py
│   └── helpers.py
├── api/
│   └── pricing_api.py
└── requirements.txt
```

---

## 🔐 Authentication & Session Management

- User authentication is handled using functions
- Session state is tracked using variables such as:
  - `current_user`
  - `last_activity_time`
- A **session timeout mechanism** automatically logs out inactive users
- No classes or objects are used for session handling

This mirrors how lightweight terminal systems manage sessions.

---

## 📞 Core Features

### User Features
- User registration and login
- Check account balance
- Recharge airtime
- Purchase data bundles
- Simulate phone calls using time-based logic
- Send SMS
- View usage and transaction history

### Admin Features
- View all registered users
- View system-wide statistics
- Reset user balances
- Block or unblock user accounts

---

## 🌐 External API Integration

Because live telecom operator pricing APIs are not publicly available, the system uses a **hybrid pricing approach**:

- External APIs are used to fetch:
  - Exchange rates
  - Average data cost references
- Final data bundle prices are computed internally using predefined rules

All API interactions are performed using the `requests` library.

---

## 🗄 Database Design

- Database access is handled using **PyDAL**
- SQL queries are abstracted away from the application logic
- Data is stored in relational tables such as:
  - Users
  - Transactions
  - Call logs
  - SMS logs
  - Data purchases

---

## 🧪 Technologies & Libraries Used

- Python 3
- PyDAL
- SQLite
- PrettyTable
- Requests
- Time module
- Random module

---

## ▶️ How to Run the Project

1. Clone or download the project
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python main.py
   ```

---

## 🎓 Academic Relevance

This project demonstrates:

* Procedural programming in Python
* Modular code organization
* ORM-based database interaction without OOP
* Session timeout implementation in terminal applications
* Secure input validation

It is suitable for coursework, system design demonstrations, and academic evaluations.

---

## 📌 Future Enhancements

* Enhanced input validation
* Expanded reporting features
* Improved pricing models
* Automated testing
* Performance optimization

---

## 👨💻 Author

Developed as an educational telecom system simulation using Python and SQL principles.

---

## 📄 License

This project is intended for educational use.
