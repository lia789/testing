
# **Django Project Development Guide**

## **Part 1: Setting Up Your Development Environment and Learning the Basics of Django**

1. **Install Python**
    - Check if Python is already installed by opening your terminal and typing `python --version` or `python3 --version`.
    - If Python is not installed, go to the [Python official website](https://www.python.org/downloads/) and download the latest stable version of Python 3.x.
    - Follow the installation instructions for your operating system. Ensure you check the box to add Python to your PATH during installation.
    - Verify that Python is correctly installed by running the version command again.

2. **Set Up a Virtual Environment**
    - Navigate to your project directory in the terminal. You can create a new directory if needed (`mkdir gowabi_clone`).
    - Inside your project directory, create a virtual environment by running `python -m venv myenv` (replace "myenv" with your preferred environment name).
    - Activate the virtual environment:
        - On Windows: Run `myenv\Scripts\activate`.
        - On macOS/Linux: Run `source myenv/bin/activate`.
    - Your terminal should now show the environment name in parentheses, indicating that the virtual environment is active.
    - To deactivate the virtual environment, use the command `deactivate`.

3. **Install Django**
    - With your virtual environment activated, install Django by running `pip install django` in your terminal.
    - After the installation, verify Django is installed by running `django-admin --version`, which should display the installed version of Django.

4. **Create a New Django Project**
    - Still within your project directory and with the virtual environment activated, start a new Django project by running `django-admin startproject gowabi_clone`.
    - This will create a new directory named `gowabi_clone` with the necessary Django files and structure.
    - Navigate into the project directory using `cd gowabi_clone`.
    - Run the development server with `python manage.py runserver` to check that everything is set up correctly.
    - Open a browser and go to `http://127.0.0.1:8000/` to see the default Django welcome page.

5. **Understand the Django Project Structure**
    - Familiarize yourself with the key files and directories that Django creates for a new project:
        - `manage.py`: A command-line utility that lets you interact with this Django project in various ways.
        - The `gowabi_clone/` directory: Contains the main settings and configuration files for your project, such as `settings.py`, `urls.py`, `wsgi.py`, and `asgi.py`.
    - Explore `settings.py` to understand how Django configurations are managed, including database settings, installed apps, and middleware.
    - Open `urls.py` to see how URL routing is handled in Django.
    - Look into `wsgi.py` and `asgi.py` to understand their roles in serving your Django application.

6. **Create Your First Django App**
    - Inside your project directory, create your first Django app by running `python manage.py startapp booking`.
    - This will create a new directory named `booking` with the following structure: `migrations/`, `admin.py`, `apps.py`, `models.py`, `tests.py`, and `views.py`.
    - Add your new app to the `INSTALLED_APPS` list in `gowabi_clone/settings.py` by adding `'booking.apps.BookingConfig',`.
    - Run the server again to ensure that the new app is correctly integrated into your project.

7. **Set Up the Database**
    - By default, Django uses SQLite as its database. You can keep this for simplicity at the start.
    - Run `python manage.py migrate` to apply initial migrations and set up the database schema.
    - Verify that a new `db.sqlite3` file has been created in your project directory, representing your database.

8. **Introduction to Django Admin**
    - Create a superuser to access the Django admin interface by running `python manage.py createsuperuser`.
    - Follow the prompts to set a username, email, and password.
    - Run the development server and go to `http://127.0.0.1:8000/admin/` to log in and explore the Django admin panel.
    - Familiarize yourself with the Django admin interface, where you can manage users, content, and other data.

9. **Basic Models and Database Interaction**
    - In your `booking/models.py`, define a basic model that represents an entity in your application (e.g., Service, Booking).
    - Run `python manage.py makemigrations` to create migrations for your model.
    - Apply the migrations with `python manage.py migrate`.
    - Register your model with the Django admin by editing `booking/admin.py` to include the model.
    - Access the Django admin to interact with your model, adding, editing, or deleting records.

10. **Conclusion of Part 1**
    - Review what you’ve accomplished: setting up Python, creating a virtual environment, installing Django, starting a project, creating an app, setting up the database, and exploring Django admin.
    - Make sure you understand the project structure and the basics of how Django manages apps and databases.
    - Experiment with creating more models and using the Django admin to solidify your understanding before moving on to the next part.
