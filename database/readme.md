
# 📡 Telco Backend – Database Module

**Owner:** Database Layer
**Status:** Active Development
**Primary Responsibility:** Data persistence & transaction recording

This module handles all database operations for:

* User creation
* Transaction tracking
* Airtime purchases
* Data purchases
* Usage logs

If you are building features that involve storing or reading persistent data, you will interact with `DatabaseClass`.

---

# 🧱 Architecture Overview

This layer is built using **PyDAL** and acts as a centralized persistence service.

### Core Rule

🚨 **No feature should write directly to `db` outside this module.**

All database writes must go through `DatabaseClass`.

This ensures:

* Consistent user binding
* Clean transaction tracking
* Maintainable architecture
* Future scalability

---

# 🗄 Tables Defined

## 1️⃣ users

Stores account-level data.

| Field   | Type    |
| ------- | ------- |
| user_id | integer |
| name    | string  |
| phone   | string  |
| balance | float   |

---

## 2️⃣ transactions

Tracks every financial movement.

| Field     | Type            |
| --------- | --------------- |
| user_id   | reference users |
| type      | string          |
| amount    | float           |
| status    | string          |
| timestamp | datetime        |

---

## 3️⃣ airtime

Stores airtime purchases.

---

## 4️⃣ data

Stores data purchases.

---

## 5️⃣ logs

Stores communication cost logs.

---

# 🧠 DatabaseClass – How It Works

Each instance represents one active user session.

It internally stores:

```python
self.__user_id
```

All inserts automatically bind to this user.

---

# 🚀 How you Should Use It

## Step 1 — Initialize

```python
from database.models import DatabaseClass

db_service = DatabaseClass()
```

---

## Step 2 — Create / Set User

```python
db_service.insert_users("Dev", "080xxxxxxx")
```

This:

* Inserts user
* Commits
* Automatically sets internal `user_id`

⚠️ After this call, all future operations attach to that user.

---

## Step 3 — Record Transactions

```python
db_service.insert_transaction(
    transaction_type="data",
    amount=1500,
    status="success",
    transact_time=datetime.now()
)
```

---

## Step 4 — Airtime / Data

```python
db_service.airtime_purchase(...)
db_service.data_purchase(...)
```

---

## Step 5 — Logs

```python
db_service.logs_insert(...)
```

---

### Credit balance 
db_service.update_balance(5000, "credit")
Debit
db_service.update_balance(1500, "debit")
That’s it.
No direct DB touching.
No chaos.
No race-condition drama later.

🔥 Why This Is Important

Because balance logic is:
Business logic
Financial logic
Security logic
You NEVER let random modules update balance directly.
That’s how:
Double spending happens
Negative balances happen
Transaction mismatch happens
Auditing becomes impossible
# 🛑 What NOT To Do

❌ Do not call `db.define_table` elsewhere
❌ Do not commit outside this layer
❌ Do not manually insert into tables from feature modules
❌ Do not modify table structure without alignment

---

# 🔐 Design Intent

This layer is structured this way so we can later:

* Swap databases
* Add validation middleware
* Add transaction rollback handling
* Introduce service layers
* Add auditing
* Implement balance enforcement

If you bypass this layer, future refactors become painful.

---

# ⚠️ Known Constraints (Current Version)

* No exception handling yet
* No automatic balance updates
* No rollback strategy
* Single user per instance

These will be handled in later iterations.

---

# 🧩 If You Need New DB Functionality

Do not implement it yourself.

Instead:

1. Raise it in the team channel
2. Define the data requirement
3. We extend `DatabaseClass` cleanly

---

# 🎯 Strategic Goal

This module will evolve into:
* A proper service layer
* With transaction safety
* With validation
Right now it’s the foundation. Don’t crack it.

