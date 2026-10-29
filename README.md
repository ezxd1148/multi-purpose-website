# Multi-Purpose Website

A collection of simple, browser-based utilities built with Python and Flask. This project brings together small programming exercises and practical tools into a single web application.

> By ezxd1146 & Eizdihar for Hack Club Dyad

## Overview

This is a Flask web application designed to make small Python programs accessible through a browser.

Instead of running each program separately in the terminal, users can interact with them through HTML forms and view the calculated results directly on the website.

### Available Tools

| Tool | Description | Status |
|---|---|---|
| Digit Counter | Counts the digits in a given integer | Available |
| Flour Calculator | Calculates the total, average, and heaviest weight from 10 flour measurements | Available |
| Student Steps Calculator | Calculates walking statistics and achievement of a daily step target | In progress |
| Student Grade Calculator | Calculates total marks and grades from quiz, assignment, and exam scores | Needs form fix |
| Text Input Tool | Accepts and displays a user's name and reason | Basic implementation |
| Tool 6 | Reserved for future functionality | Planned |

Some features are still under development.

## How It Works

The application uses **Flask** to connect HTML forms with Python functions.

When a user submits a form:

1. The browser sends the input to a Flask route using an HTTP POST request.
2. The route retrieves and validates the submitted data.
3. A Python function or class processes the input.
4. Flask passes the result to a Jinja2 template.
5. The browser displays the result on the page.

### Tech Stack

- **Python 3.13** for application logic.
- **Flask** for request handling and routing.
- **HTML, CSS and Jinja2** for the user interface.
- **uv** for dependency management.
- **Ruff and Pylint** for code quality checks.
- **GitHub Actions** for automated linting and formatting checks.

### Project Structure

```text
multi-purpose-website/
├── .github/workflows/      # CI workflows
├── src/
│   ├── main.py             # Flask application and routes
│   ├── multi_purpose_website/
│   │   ├── add_tool1.py
│   │   ├── assign_1.py
│   │   ├── assign_2.py
│   │   ├── assign_3.py
│   │   ├── prac_1.py
│   │   └── prac_2.py
│   ├── templates/          # Jinja2 HTML templates
│   ├── static/             # CSS files
│   └── assets/             # Images and other assets
├── pyproject.toml
├── uv.lock
└── README.md
```

The application keeps its Python calculations separate from its Flask routes, making individual tools easier to maintain, reuse, and extend.

## Why This Project?

This project started as a way to turn Python programming exercises into interactive web applications.

Many beginner programming exercises are designed to run in a terminal. Although useful for learning programming fundamentals, they do not demonstrate how those same functions can be integrated into a website.

By building this project, we wanted to explore:

- Connecting standalone Python functions to a Flask backend.
- Handling and validating user input through HTML forms.
- Separating application logic from presentation.
- Practising modular Python development and code organization.
- Using automated code quality tools in a GitHub workflow.

The project also serves as a foundation for experimenting with additional utilities as we continue learning software development.

## Quickstart

### Prerequisites

Make sure you have:

- Git
- Python 3.13
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### 1. Clone the Repository

```bash
git clone https://github.com/ezxd1148/multi-purpose-website.git
cd multi-purpose-website
```

### 2. Install Dependencies

```bash
uv sync
```

This installs the project dependencies defined in `pyproject.toml` using the existing `uv.lock` file.

### 3. Start the Development Server

```bash
uv run flask --app src/main.py run --debug
```

### 4. Open the Website

Visit:

**http://127.0.0.1:5000**

You can now access the available tools from the homepage.

### Code Quality

Run the project's Ruff checks:

```bash
uv run ruff check .
uv run ruff format --check .
```

The repository also includes a GitHub Actions workflow that runs Ruff and Pylint on pushes.

## Current Limitations

This is an ongoing learning project, and some features are not yet complete. But it is shippable.

- The student steps calculator is not connected to its web interface.
- The grading form currently submits to the wrong route.
- Tool 6 does not have an implemented Flask route.
- Some input validation and error handling still require improvements.

The quickstart uses Flask's development server and is not intended for production hosting.

## License

This project is licensed under the [MIT License](LICENSE).

---

Built by [ezxd1148](https://github.com/ezxd1148).
