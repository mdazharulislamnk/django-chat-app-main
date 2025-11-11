#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """CLI entrypoint: sets DJANGO_SETTINGS_MODULE and delegates to Django."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')  # use project settings
    try:
        from django.core.management import execute_from_command_line  # Django’s runner
    except ImportError as exc:
        # Helpful error if Django isn’t installed/venv not activated
        raise ImportError(
            "Couldn't import Django. Is it installed and is your virtualenv active?"
        ) from exc
    execute_from_command_line(sys.argv)  # run commands like runserver/migrate

if __name__ == '__main__':
    main()
