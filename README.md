# -Phone-Book-Python-Tkinter-SQLite

A simple Phone Book desktop application built with Python, Tkinter, and SQLite.

This project combines a graphical user interface with a local SQLite database to provide basic contact-management functionality. Users can add contacts, display all saved contacts, search for a contact by name, delete contacts, and close the application while safely closing the database connection.

📌 Project Overview

The application provides a small desktop-based phone book with two main components:

Tkinter — creates the graphical user interface.
SQLite — stores contact information locally in a database.

Each contact contains:

Name
Phone number

The application automatically creates the phoneBook.db database and the phoneBook table if they do not already exist.

✨ Features
➕ Add Contact
Enter a name and phone number.
Save the contact to the SQLite database.
Display the new contact in the table.
📋 Show All Contacts
Retrieves all contacts from the database.
Refreshes the GUI table with the current database contents.
🔍 Search Contact
Searches for a contact by name.
Displays the matching result in the table.
Shows a warning message when no matching contact exists.
🗑️ Delete Contact
Deletes a contact using its name.
Refreshes the displayed contact list after deletion.
❌ Close Application
Closes the SQLite database connection.
Properly destroys the Tkinter window.

🖥️📽️YouTube video link:https://youtu.be/WWA4JmccWZ0
