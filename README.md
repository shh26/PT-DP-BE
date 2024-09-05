## Getting Started

### Prerequisites

Make sure you have the following installed:

- **Python 3.10**: Download it from [python.org](https://www.python.org/downloads/release/python-3100/).
- **PostgreSQL**: Download it from [PostgreSQL](https://www.postgresql.org/download/).
- **pgAdmin**: You can download it from [pgAdmin](https://www.pgadmin.org/download/).
- **pip**: Python package manager.
- **virtualenv** (optional but recommended): For creating isolated Python environments.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shh26/PT-DP-BE.git
   
2. Navigate to the project directory:

   ```bash
   cd your-repo

3. (Optional) Create and activate a virtual environment:

   ```bash
   python3.10 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

4. Install the dependencies from requirements.txt:

   ```bash
   pip install -r requirements.txt

### Database Setup   
5. Run the following commands to apply migrations and set up the database:

   ```bash
   python manage.py migrate

### Running the Development Server
6. To start the Django development server, run:

   ```bash
   python manage.py runserver

### Creating a Superuser
6. To access the Django admin panel, you need to create a superuser:

   ```bash
   python manage.py createsuperuser


## Postgres And pgAdmin setup instructions

### PostgreSQL Setup

1. Install PostgreSQL and create a new database and user:

   - Create a new PostgreSQL database:

     ```sql
     CREATE DATABASE your_db_name;
     ```

   - Create a new PostgreSQL user and set a password:

     ```sql
     CREATE USER your_db_user WITH PASSWORD 'your_password';
     ```

   - Grant the user access to the database:

     ```sql
     GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
     ```

2. Update your Django `settings.py` file to configure the database connection:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }

### pgAdmin Setup Instructions
1. Connect to PostgreSQL Server:

   ```bash
   Open pgAdmin and create a new server by right-clicking on "Servers" → "Create" → "Server".
   Set a name (e.g., Local PostgreSQL).
   Under the "Connection" tab, fill in the following details:
   Host: localhost
   Port: 5432
   Username: Your PostgreSQL username (e.g., my_project_user)
   Password: Your PostgreSQL password
   Click "Save".


2. Create a Database in pgAdmin:
   ```bash
   Navigate to your server in pgAdmin, right-click on "Databases" → "Create" → "Database".
   Enter the database name (e.g., my_project_db) and choose the owner (the user you created earlier).
   Click "Save".
   Managing the Database:

You can use pgAdmin to manage tables, run queries, and check the data in your PostgreSQL database.
