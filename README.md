### Activate the virtual environment (required before running Django commands)
source venv/bin/activate

### Start the Django development server (runs on http://127.0.0.1:8000/)
python manage.py runserver 

### Create migration files (detects changes in models and prepares database migrations)
python manage.py makemigrations

### Apply migrations to the database (executes pending migrations)
python manage.py migrate

### Show all migrations and their status (applied or pending)
python manage.py showmigrations

### Preview the raw SQL of a specific migration (before applying it)

### Replace <app_name> with the Django app name (e.g., 'core')

### Replace <migration_number> with the migration ID (e.g., 0002)
python manage.py sqlmigrate <app_name> <migration_number>



### update requirements.txt
pip install drf-yasg