<div align="center">

<img src="./.github/assets/readme/bookverse-logo.svg" alt="BookVerse" width="88" />

# BookVerse

**Library management, reimagined.**

A JavaFX desktop app that runs a small library end to end: catalogue, members,
issuing, returns, fines and a community chat. Everything is saved to plain-text
files, so there is nothing to install but Java.

![Java](https://img.shields.io/badge/Java-21-ed8b00?logo=openjdk&logoColor=white)
![JavaFX](https://img.shields.io/badge/JavaFX-21.0.6-0a74da)
![Gradle](https://img.shields.io/badge/Gradle-8.13-02303a?logo=gradle&logoColor=white)
![Storage](https://img.shields.io/badge/storage-plain%20text-555555)
![License](https://img.shields.io/badge/license-MIT-blue)

[Screens](#screens) ·
[Flows](#flows) ·
[Architecture](#architecture) ·
[Get started](#getting-started)

<img src="./.github/assets/readme/bookverse-welcome.jpg" alt="BookVerse welcome screen with log in and sign up buttons" width="800" />

</div>

BookVerse covers the daily work of a small library. A librarian keeps the
catalogue and the member list, readers borrow up to three books at a time, and
late returns are fined at a fixed daily rate that stops growing once the book is
back. A built-in chat room lets members talk to each other. The whole thing is
about 1,400 lines of Java plus FXML views and one stylesheet.

## At a glance

| | |
| --- | --- |
| **What it is** | A desktop app built with Java 21, JavaFX 21.0.6 and Gradle 8.13 |
| **Storage** | Three plain-text files, `library_data.txt`, `members.txt` and `user_data.txt`; no database |
| **Borrowing rules** | At most 3 books out per member, and no new issue while the total due is above 1000 TK |
| **Fines** | 60 TK per overdue day; the fine freezes on return and can be paid in part or in full, never over |
| **Chat** | A socket chat server on port 12345 with one handler thread per client |
| **Screens** | Welcome, dashboard, inventory, issue, return, members, chat and pop-ups for login, sign-up and cards |
| **Licence** | MIT |
