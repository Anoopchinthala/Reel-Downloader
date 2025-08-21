# Instagram Reel Downloader

The **Reel Downloader** project is a simple yet effective Python-based application that allows users to download Instagram Reels directly using the [Instaloader](https://github.com/instaloader/instaloader) library. The system focuses on providing a lightweight, user-friendly way to fetch reels while removing unnecessary metadata and files, ensuring only the video is retained.

---

## Overview
Instagram Reels have become a popular way of sharing short videos. However, downloading them for offline viewing isn’t supported natively. This project solves that problem by allowing users to input a reel URL and download the video directly to their system.  

The project leverages **Instaloader** for downloading and includes built-in cleanup functions to remove unwanted files, leaving only the `.mp4` video.  

Additionally, the repository includes **unit tests (pytest)** to ensure reliability and maintainability.

---

## Features
- **Reel Downloader Module:** Downloads Instagram Reels using a given URL.
- **File Cleaner Module:** Automatically deletes metadata, captions, and other non-video files.
- **Error Handling:** Detects invalid URLs and provides user-friendly error messages.
- **Testing Support:** Comes with basic unit tests for validation.
- **Lightweight & Portable:** Requires only Python and Instaloader.

---

## Technology Stack
- **Programming Language:** Python 3.10+
- **Library/Frameworks:** 
  - [Instaloader](https://github.com/instaloader/instaloader) (for downloading Reels)
  - [Pytest](https://docs.pytest.org/) (for testing)
- **Version Control:** Git & GitHub

---

## Installation and Setup

To run this project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Anoopchinthala/Reel-Downloader.git

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt

3. **Run the project:**
    ```bash
    python Main.py

4. **Run the tests (optional):**
    ```bash
    pytest test_project.py
