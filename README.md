# Class-Mate

**Class-Mate** is an intuitive educational platform built with Django and MySQL. It allows users to create or join classes, manage assignments, conduct exams, and evaluate performance. This app is designed to enhance the classroom experience for both students and teachers.

## Features

- **Class Management**: Teachers can create classes and invite students to join.
- **Exam Management**: Create various types of exams, schedule them, and automate grading for objective questions.
- **Evaluation and Feedback**: Manually grade subjective responses, provide detailed feedback, and generate performance reports.
- **Student Dashboard**: Submit assignments, view exam results, and track academic progress.
- **Collaborative Tools**: Announcements, discussion forums, and resource sharing.

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 3.0 or higher
- MySQL

### Steps

1. **Clone the repository**:
    ```sh
    git clone https://github.com/hasan-nazmul/Class-Mate.git
    cd class-mate
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the database**:
    - Create a MySQL database.
    - Update the `DATABASES` settings in `class_mate/settings.py`.

5. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

## Usage

1. **Access the app**: Open your browser and go to `http://localhost:8000`.
2. **Admin Panel**: Log in to the admin panel at `http://localhost:8000/admin` to manage classes, exams, and users.
3. **Create and Join Classes**: Teachers can create classes and share the unique class code with students to join.
4. **Manage Exams**: Teachers can create, schedule, and grade exams. Students can view their results and feedback.

## Contributing

We welcome contributions! Please fork the repository and submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact us at support@classmate.com.

---

**Class-Mate** aims to create a collaborative and organized environment that supports both teaching and learning. By integrating essential educational tools into a single platform, it simplifies classroom management, improves communication, and enhances the overall educational experience.

