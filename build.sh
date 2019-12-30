python manage.py makemigrations users
python manage.py migrate users
python manage.py makemigrations
python manage.py migrate
# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@djangox.com', 'password123')" | python manage.py shell
