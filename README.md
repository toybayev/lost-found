# Lost & Found

A simple Django web application for lost and found items.

## How to Run the Application

### 1. Install and Activate Virtual Environment
First, create and activate a virtual environment:

```bash
python -m venv env
On Windows:

bash
Copy
Edit
./env/Scripts/activate
On Mac/Linux:

bash
Copy
Edit
source env/bin/activate
2. Install Dependencies
Ensure you have Django 4.0 installed:

bash
Copy
Edit
pip install django==4.0
3. Navigate to the Project Directory
bash
Copy
Edit
cd ask_platform
4. Apply Migrations and Run the Server
bash
Copy
Edit
python manage.py migrate
python manage.py runserver
Now, open your browser and visit http://127.0.0.1:8000/ to access the application.

Features
Users can create, view, and track lost & found items.
Admin panel for managing categories and items.
Contact the item owner via Telegram.
Project Structure
bash
Copy
Edit
lostfound/
│── lostfound/         # Main Django project settings
│── lost/              # Lost & Found application
│   │── static/lost/   # Static files (logo, styles)
│   │── templates/lost/ # HTML templates
│   │── views.py       # Application views (CRUD operations)
│   │── models.py      # Database models
│   │── forms.py       # Django forms
│   │── urls.py        # URL routing
│── manage.py          # Django command-line utility
Admin Access
To access the Django admin panel, create a superuser:

bash
Copy
Edit
python manage.py createsuperuser
Then login at http://127.0.0.1:8000/admin/.    
