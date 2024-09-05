## Getting Started

### Prerequisites

Make sure you have the following installed:

- **Python 3.10**: You can download it from [python.org](https://www.python.org/downloads/release/python-3100/).
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


