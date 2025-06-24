# Predict Grade ML Website

A web application for predicting the probability of passing core engineering courses, developed for the Computer Engineering Department, Faculty of Engineering, Rajamangala University of Technology Lanna. The system uses machine learning models to predict student performance based on their grades in prerequisite subjects.

## Features

-   **User Authentication:** Login with student ID (validated by department rules).
-   **Subject Selection:** Choose a core subject to predict.
-   **Grade Input:** Enter grades for prerequisite subjects.
-   **Prediction:** Get a probability score for passing the selected subject using trained ML models.
-   **Result Report:** View prediction results and entered grades.
-   **Admin Panel:** Manage subjects, prerequisites, instructors, departments, and prediction criteria.

## Project Structure

```
.
├── manage.py
├── db.sqlite3
├── predictGrade/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── predictApp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── loginforms.py
│   ├── models.py
│   ├── predictors.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   └── static/
├── templates/
│   ├── base.html
│   ├── forms.html
│   ├── login.html
│   ├── reports.html
│   └── select.html
```

## Requirements

-   Python 3.8+
-   Django 3.2+
-   scikit-learn
-   numpy

## Installation

1. **Clone the repository:**

    ```sh
    git clone <your-repo-url>
    cd Django_PredictGrade_ML_Website
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

    _(If `requirements.txt` does not exist, install manually: `pip install django scikit-learn numpy`)_

4. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser (for admin access):**

    ```sh
    python manage.py createsuperuser
    ```

6. **Collect static files (optional for production):**
    ```sh
    python manage.py collectstatic
    ```

## Running the Project

Start the development server:

```sh
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage

1. **Login:** Enter your student ID to log in.
2. **Select Subject:** Choose a subject to predict from the menu.
3. **Input Grades:** Fill in your grades for the prerequisite subjects.
4. **View Prediction:** Submit the form to see your probability of passing and a summary report.

## Machine Learning Models

-   Models are stored as `.p` files in `predictApp/static/predictor/`.
-   Each subject has its own trained logistic regression model.
-   Models are loaded and used for prediction in [`predictApp/predictors.py`](predictApp/predictors.py).

## Customization

-   **Add/Edit Subjects, Prerequisites, Instructors, Departments, Criteria:** Use the Django admin panel at `/admin/`.
-   **Change Templates:** Edit HTML files in the [`templates/`](templates/) directory.
-   **Update Styles:** Modify CSS in [`predictApp/static/css/mainstyles.css`](predictApp/static/css/mainstyles.css).

## License

This project is for educational purposes. Please contact the author for other uses.

## Acknowledgements

-   Computer Engineering Department, Faculty of Engineering, RMUTL
-   Django Project
-   scikit-learn

---

\*Developed as part of the Bachelor of Engineering curriculum, Computer Engineering,
