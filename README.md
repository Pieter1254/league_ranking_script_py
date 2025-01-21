# League Ranking Script

This script calculates and displays the ranking of teams based on match results.

## Python Version
This script is compatible with **Python 3.6+**.

## Operating System
This was built in **WSL 2** on a windows machine.

## Requirements
- Python 3.6 or higher.
- No additional libraries are required besides Python's built-in `re` and `collections`.

## How to Use

### Run the Script

1. **Via File Input:**
   - When running the script, you'll be prompted to provide a file path containing the match results.
   - The file should contain one match result per line in the format:
     ```
     Team A score, Team B score
     ```
     Example:
     ```
     Team A 1, Team B 1
     Team C 2, Team D 2
     Team A 3, Team B 3
     ```

2. **Via String Input:**
   - Alternatively, you can provide the match results directly through the terminal. Enter each match result line-by-line, and type `done` when you're finished.
   
### Usage:
```bash
python3 league_ranking_script.py
