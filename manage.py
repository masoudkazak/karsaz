import os
import sys

from decouple import config


def main():
    """Run administrative tasks."""
    django_env = config("ENVIRONMENT", "dev")
    if django_env == "dev":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
