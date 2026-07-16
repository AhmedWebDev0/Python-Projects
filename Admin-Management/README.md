# 👥 Membership Management System

A simple Python project that simulates a basic membership management system. It allows administrators to manage their names and gives non-admin users the option to request access.

---

## 📌 Features

* ✅ Check if a user is an administrator.
* ✏️ Update an administrator's name.
* ➕ Add a new member to the admin list.
* ❌ Display a message when the user chooses not to join.
* 📋 Display the updated list of administrators.

---

## 🛠️ Technologies Used

* Python 3

---

## 📂 Project Structure

```text
Membership_Management/
│── Membership_Management.py
│── README.md
```

---

## ▶️ How It Works

1. The user enters their name.
2. The program checks if the name exists in the administrator list.
3. If the user is an administrator:

   * They can update their name.
4. If the user is not an administrator:

   * They can choose whether to be added to the administrator list.

---

## 💻 Concepts Practiced

This project demonstrates:

* Lists
* User Input (`input()`)
* Conditional Statements (`if`, `elif`, `else`)
* String Methods (`strip()`, `capitalize()`)
* List Methods (`append()`, `index()`)
* Formatted Strings (f-strings)

---

## 📷 Example

```text
Please type your name Ahmed

Hello Ahmed Welcome Back

Delete or Update Your name?

Update

Your New Name, please AhmedDev

Name Updated
['AhmedDev', 'Mustafa', 'Joury', 'Osama', 'Ali']
```

---

## 🚀 Future Improvements

* Fix the delete functionality.
* Validate user input.
* Ignore uppercase/lowercase differences automatically.
* Store members in a file or database.
* Add login with usernames and passwords.
* Create a graphical user interface (GUI).

---

## 📜 License

This project was created for learning Python programming and practicing list manipulation and conditional logic.
