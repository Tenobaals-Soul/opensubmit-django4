#!../.venv/bin/python
import os
import sys

if __name__ == "__main__":
    # delegate everything else to the ordinary Django manage.py functionality
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opensubmit.settings")
    print(sys.executable)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
