# BookVerse: Library Management System

BookVerse is a JavaFX desktop application for running a small library. It keeps a book catalogue and member profiles, handles issuing and returning with due dates, charges fines for overdue books, and includes a community chat. Everything is saved to plain-text files, so there is no database to set up.

## Contents

- [Features](#features)
- [Using the app](#using-the-app)
- [Repository structure](#repository-structure)
- [Data files](#data-files)
- [Getting started](#getting-started)
- [Built with](#built-with)
- [Known limitations](#known-limitations)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Accounts**: sign up and log in with an email and password from pop-up dialogs.
- **Dashboard**: progress bars for books issued, dues paid and fines.
- **Inventory**: browse the catalogue, sort it by author, title or availability, and add new books.
- **Issuing**: search by book name or author and pick a due date. A member can have at most 3 books out at once, and issuing is refused while their total due is above 1000 TK.
- **Returns and fines**: overdue books are fined 60 TK per day. A fine stops growing once the book is returned, and it can then be paid in full or in part, but never overpaid.
- **Members**: a member list, a "Become a member" form (name, profession, contact) and a "My Profile Card" view.
- **Community chat**: a socket-based chat room backed by a small chat server.
- **Plain-text storage**: books, members and accounts are saved to `.txt` files in the project folder.

## Using the app

1. Start the app (see [Getting started](#getting-started)) and sign up with an email and password, then log in.
2. Use **Become a member** to create your member profile.
3. In **Inventory**, add books or sort the catalogue.
4. In **Issue**, find a book, choose a due date and issue it.
5. In **Return**, return the book. If it was overdue, the fine is now fixed and can be paid from the same screen.
6. Open the **Dashboard** to see your issues, dues and fines at a glance.

## 📁 Repository Structure

- `src/main/` — Contains the application source code logic.
- `library_data.txt` — Plain-text data store for the book catalog.
- `members.txt` — Plain-text data store for library member profiles.
- `user_data.txt` — Plain-text data store for application users and administrators.
- `build.gradle.kts` — Kotlin DSL configuration file for Gradle dependencies and builds.

## 💾 Data Persistence Format

The system uses plain-text files with pipe-delimited (`|`) records to maintain state:

- **`library_data.txt`**: `BookID|Title|Author|Genre|IsAvailable`
- **`members.txt`**: `MemberID|Name|Email|JoinDate`
- **`user_data.txt`**: `UserID|Username|PasswordHash|Role`

## 🚀 Getting Started

### Prerequisites

- **Java Development Kit (JDK):** Version 11 or higher recommended.
- **Terminal / Command Prompt**

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Kairo-2081/LibraryManager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd LibraryManager
   ```

### Running the Application

You can execute the application using the included Gradle wrapper.

**On Windows:**
```cmd
gradlew.bat run
```

**On macOS / Linux:**
```bash
chmod +x gradlew
./gradlew run
```

### Building & Testing

- **Build project:**
  ```bash
  ./gradlew build
  ```
- **Run unit tests:**
  ```bash
  ./gradlew test
  ```

## 🛠️ Built With

- **Kotlin / Java** — Core programming languages.
- **Gradle** — Build automation and dependency management tool using Kotlin DSL (`build.gradle.kts`).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [Issues page](https://github.com/Kairo-2081/LibraryManager/issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
