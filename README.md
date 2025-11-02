# Python Basic Programs — 60-Day Streak

A compact 60-day plan to build core Python skills by solving small, focused programs each day.

Files
- [pythonprograms.py](pythonprograms.py) — active file for daily code snippets.
- [README.md](README.md) — this file.

Purpose
- Practice one small Python program per day for 60 days.
- Build fluency with syntax, data structures, algorithms, and common libraries.

How to use
- Add each day's solution to [pythonprograms.py](pythonprograms.py) or create a `dayNN.py` file.
- Keep each day's code small (10–50 lines) and add a brief comment header with the day number and topic.
- Run with: `python pythonprograms.py` (or `python day01.py`, etc.)

Daily entry template (example)
```python
# Day 01 — Topic: Hello world / Input
def day01():
    """Print greeting and echo user input."""
    name = input("Name: ")
    print(f"Hello, {name}!")

if __name__ == "__main__":
    day01()