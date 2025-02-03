#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twitter.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Ensure Django binds to the correct port on Render
    if len(sys.argv) > 1 and sys.argv[1] == "runserver":
        port = os.getenv("PORT", "8000")  # Use Render's PORT or default to 8000
        sys.argv[2:] = ["0.0.0.0:" + port]  # Override the default host:port

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()