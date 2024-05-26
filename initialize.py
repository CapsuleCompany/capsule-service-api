import os
import subprocess
import django
from django.core.management import call_command

# ANSI color codes for blue, green, bold, and reset
BLUE = "\033[94m"
GREEN = "\033[92m"
BOLD = "\033[1m"
RESET = "\033[0m"


def run_command(command):
    result = subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        input=b"y\ny\n",
    )
    if result.stdout:
        print(result.stdout.decode("utf-8"))
    if result.stderr:
        print(result.stderr.decode("utf-8"))


def create_superuser(email, password):
    from django.contrib.auth import get_user_model

    User = get_user_model()
    if not User.objects.filter(email=email).exists():
        User.objects.create_superuser(email=email, password=password)
        print(
            f"{GREEN}{BOLD}Superuser created with email: {email} and password: {password}{RESET}"
        )
    else:
        print(f"{GREEN}{BOLD}Superuser with email: {email} already exists{RESET}")


def main():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "core.settings"
    )  # Ensure this is correct
    django.setup()

    commands = [
        "python manage.py makemigrations user --empty",
        "python manage.py makemigrations service --empty",
        "python manage.py migrate user",
        "python manage.py migrate service",
        "python manage.py makemigrations user --empty",
        "python manage.py makemigrations service --empty",
        "yes yes | python manage.py makemigrations user",
        "python manage.py migrate user",
        "yes yes | python manage.py makemigrations service",
        "python manage.py migrate service",
        "python manage.py migrate",
        "python manage.py makemigrations payment",
        "python manage.py migrate payment",
        "python manage.py makemigrations schedule",
        "python manage.py migrate schedule",
    ]

    for command in commands:
        print(f"{BLUE}{BOLD}Running command:{RESET} {command}")
        run_command(command)
        print(f"{GREEN}{BOLD}Command completed{RESET}")

    # Create superuser after migrations
    create_superuser("camryn@test.com", "0010110")


if __name__ == "__main__":
    main()
