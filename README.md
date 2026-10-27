# 📚 Library Manager

A lightweight, console-based **Library Management System** built with **Kotlin/Java** and managed via the **Gradle** build system. This project demonstrates basic CRUD operations, object-oriented programming principles, and flat-file data persistence without the overhead of a heavy relational database.

## 📋 Table of Contents

- [Features](#-features)
- [Usage Preview](#-usage-preview)
- [Repository Structure](#-repository-structure)
- [Data Persistence Format](#-data-persistence-format)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
  - [Building & Testing](#building--testing)
- [Built With](#%EF%B8%8F-built-with)
- [Contributing](#-contributing)
- [License](#-license)

## 📋 Features

- 📖 **Book Management:** Keep track of available books, genres, and availability statuses.
- 👥 **Member Directory:** Register, view, and manage library patrons.
- 🔐 **User Authentication:** System administrator access logs to secure the management interface.
- 💾 **Flat-File Persistence:** Data is automatically saved to and loaded from local `.txt` files.

## 💻 Usage Preview

When you launch the application, you will be presented with an interactive console management menu:

```text
========================================
       LIBRARY MANAGEMENT SYSTEM       
========================================
1. View Book Catalog
2. Add New Book
3. Register Patron
4. View Active Members
5. System Admin Settings
6. Exit
----------------------------------------
Select an option (1-6):
```

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
