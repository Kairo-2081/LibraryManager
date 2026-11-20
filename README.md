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

## Repository structure

```text
.
├── src/main/java/com/example/librarymanager/
│   ├── HelloApplication.java    JavaFX application (the Gradle `run` main class)
│   ├── Launcher.java            Plain `main` that launches HelloApplication
│   ├── HelloController.java     Screens, login, issue/return, fines, file handling
│   ├── Book.java, Member.java   Data models
│   ├── ChatServer.java          Standalone chat server (port 12345)
│   └── ChatController.java, ChatService.java, ClientHandler.java   Chat client and server plumbing
├── src/main/resources/com/example/librarymanager/   FXML views, stylesheet and icons
├── library_data.txt             Book catalogue
├── members.txt                  Member profiles
├── user_data.txt                Login accounts
├── build.gradle.kts             Gradle build (Kotlin DSL)
└── gradlew, gradlew.bat         Gradle wrapper
```

## Data files

The app reads and writes three comma-separated files in the folder it is started from. Fields are split on commas, so a value cannot contain a comma.

| File | One line per | Fields |
| --- | --- | --- |
| `library_data.txt` | book | `id,title,author,status,totalIssues,issueDate,dueDate,fine,issuedTo` |
| `members.txt` | member | `name,profession,issues,contact,mail,fine,freq,blockStatus,totalPaid,totalDue,finedCount,paymentHistory` |
| `user_data.txt` | account | `email,password` |

Rules for the book file: `status` is `Available` or `Issued`, dates are `yyyy-MM-dd` or `none`, and `issuedTo` holds the member's email or `none`.

Example book lines:

```text
101,Dune,Frank Herbert,Available,0,none,none,0.0,none
102,Emma,Jane Austen,Issued,3,2026-04-08,2026-04-14,0.0,jane@example.com
```

The data files in the repository hold demo records. Passwords in `user_data.txt` are plain text.

## Getting started

### Prerequisites

- JDK 21. The Gradle build requests a Java 21 toolchain.
- An internet connection on the first run, so Gradle can download itself (8.13), JavaFX 21.0.6 and the libraries.

### Install and run

```bash
git clone https://github.com/Kairo-2081/LibraryManager.git
cd LibraryManager
```

On macOS or Linux:

```bash
chmod +x gradlew
./gradlew run
```

On Windows:

```cmd
gradlew.bat run
```

Start the app from the repository root. The data files are opened by relative path, so a different working directory means the app reads and creates its files somewhere else.

### Community chat

The chat client connects to `localhost:12345`, so start the chat server first. It uses only the JDK, so you can run it straight from the compiled classes:

```bash
./gradlew classes
java -cp build/classes/java/main com.example.librarymanager.ChatServer
```

It prints `Chat Server started on port 12345`. Then launch the app as above. To chat across machines, change the host in `ChatController.java`.

### Build and test

```bash
./gradlew build
```

JUnit 5 is configured in `build.gradle.kts`, but the project has no tests yet, so `./gradlew test` has nothing to run.

## Built with

- **Java 21** and **JavaFX 21.0.6** (controls, FXML, web, swing, media).
- **Gradle 8.13** (wrapper) with the Java module, OpenJFX and jlink plugins. A `jlink` runtime image is configured.
- **Libraries**: ControlsFX, FormsFX, ValidatorFX, Ikonli, BootstrapFX, TilesFX and FXGL.
- **Plain-text files** for storage and plain Java sockets for chat.

## Known limitations

- Passwords are saved and compared in plain text. Do not reuse a real password.
- There is no separate admin role; every logged-in user sees the same screens.
- The chat server must be started by hand, and the chat client always connects to `localhost`.
- The project has no automated tests.
- Data files are plain text without locking, so run only one copy of the app against a folder.

## Contributing

Contributions, issues and feature requests are welcome on the [Issues page](https://github.com/Kairo-2081/LibraryManager/issues).

1. Fork the project.
2. Create a feature branch: `git checkout -b feature/short-name`
3. Commit your changes with a clear message.
4. Push the branch: `git push origin feature/short-name`
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.
