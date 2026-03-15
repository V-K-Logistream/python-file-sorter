# python-file-sorter
A Python automation script that sorts and routes files based on naming conventions. Includes exception handling for rogue files and detailed, timestamped activity logging.

# Automated File Triage & Sorting Script
## Overview

This Python script automates the triage of chaotic file directories by routing documents into designated folders based on specific naming conventions. It was designed to streamline file management, reduce manual sorting time, and enforce data organization standards.

### Features

Automated Routing: Scans an input directory and moves files into specific destinations (e.g., HR, Ops) based on keyword tags (like Q1 or Q2).

Exception Handling: Automatically isolates files that do not match established naming rules into a Needs_Review folder for human processing.

Detailed Logging: Generates a timestamped .txt report detailing the total files scanned, successful moves, and identified exceptions.

### Setup Instructions

Ensure Python 3 is installed on your local machine.

Clone or download this repository.

Open file_sorter.py in a text editor.

Update the base_dir variable to point to your target directory:
base_dir = "/your/file/must/be/here/TEST"

Ensure your target directory contains an Input folder containing your unsorted files, alongside your destination folders (e.g., HR, Ops, and Needs_Review).

### Usage

Navigate to the directory containing the script and run it via your terminal:
python3 file_sorter.py

## Quality Assurance & Roadmap

Current Status: Fully functional for exact string matches.

Known Behavior: The script is intentionally case-sensitive (it looks strictly for Q1 and ignores q1). This was identified during the Quality Assurance testing phase.

Future Iterations: Implementing case-insensitive logic to account for human error and inconsistencies in manual file naming.
