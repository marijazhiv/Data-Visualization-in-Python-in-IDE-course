# Task: Introduction to Virtual Environments and Libraries for Data Visualization

In this task, you’ll learn about virtual environments in Python, three key libraries for data visualization, and why Python is one of the most popular languages for data visualization tasks.

---

### What is a `.venv`?

A `.venv` (short for “virtual environment”) is a dedicated workspace for Python projects that isolates dependencies and libraries. Using `.venv` is beneficial because:
- It prevents conflicts between libraries used in different projects.
- It allows projects to use specific library versions without affecting the global Python environment.
- It is essential for reproducibility, especially when sharing projects with others or deploying to production.

To create a virtual environment, we use:
```bash
python3.9 -m venv venv

Once created, we activate it to install libraries just for this project:

source venv/bin/activate  # On Windows, use `venv\Scripts\activate`