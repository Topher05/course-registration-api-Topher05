# Course Registration API COSC381

A Python-based API for managing student course registration, built with FastAPI.

## Features

- Register students for courses.
- View available courses and student details.
- Manage course and student data through an easy-to-use API.
- Interactive API documentation at `/docs`.

## Installation

1. **Clone or download the repository**:
   ```bash
   git clone https://github.com/Topher05/course-registration-api-Topher05.git
   cd course-registration-api-Topher05
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the app**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the app**:
   - Use API endpoints for:
     - Registering students for courses.
     - Viewing course details.
     - Managing student records.
   - Navigate to `/docs` for an interactive API documentation interface.

3. **Stop the app**:
   - Press `Ctrl+C` in the terminal.

## Running Tests

Run the test suite with:
```bash
pytest
```

## Requirements

- Python 3.6 or higher
- See `requirements.txt` for additional dependencies.

## Endpoints

Some common endpoints include:
- `/students/{student_id}`: Retrieve or manage student information.
- `/courses/{course_id}`: View course details.
- `/register`: Register a student for a course.

For a complete list, refer to the interactive documentation available at `/docs`.
