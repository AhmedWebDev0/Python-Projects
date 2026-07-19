# 🌐 Website Manager

A simple Python project that allows users to create and manage a list of website bookmarks. The program demonstrates the use of **loops**, **lists**, **user input**, and **string manipulation**.

---

## 📌 Features

* 🌍 Add up to 5 websites.
* 🔗 Automatically adds the `https://` prefix.
* 🧹 Cleans user input using `strip()` and `lower()`.
* 📋 Stores websites in a Python list.
* 🚫 Prevents adding more websites after reaching the limit.
* 📖 Demonstrates list management using loops.

---

## 🛠️ Technologies Used

* Python 3

---

## 📂 Project Structure

```text
Website_Manager/
│── website_manager.py
│── README.md
```

---

## ▶️ How It Works

1. The user enters a website name.
2. The program formats the input by:

   * Removing extra spaces.
   * Converting text to lowercase.
   * Adding the `https://` prefix.
3. The website is stored in a list.
4. The process repeats until the maximum number of websites is reached.
5. A message is displayed when no more websites can be added.

---

## 💻 Concepts Practiced

This project demonstrates:

* `while` Loops
* Lists
* User Input (`input()`)
* String Methods (`strip()`, `lower()`)
* List Methods (`append()`, `sort()`)
* Variables
* Conditional Statements (`if` / `else`)
* Formatted Strings (f-strings)

---

## 📷 Example

```text
Maximum Allowed website https:// github.com
Website Added

Maximum Allowed website https:// google.com
Website Added

Maximum Allowed website https:// openai.com
Website Added

Maximum Allowed website https:// cs50.harvard.edu
Website Added

Maximum Allowed website https:// python.org
Website Added

Bookmark Is Full, You Can't Add More
```

---

## 🚀 Future Improvements

* Fix the website counter message.
* Display the list of saved websites correctly.
* Allow users to remove bookmarks.
* Prevent duplicate website entries.
* Validate website names before saving.
* Save bookmarks to a file for permanent storage.
* Add a menu (Add, View, Delete, Exit).

---

## 📜 License

This project was created for learning Python programming and practicing loops, lists, string manipulation, and basic data management.
