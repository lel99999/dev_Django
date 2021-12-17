#!/usr/bin/env python
import sys
import django
from django.conf import settings
from django.test.utils import get_runner
if __name__ == "__main__":
    settings.configure(
        DATABASES={"default": {
            "ENGINE": "django.db.backends.sqlite3"
        }},
        ROOT_URLCONF="tests.urls",
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "myapp",
        ],
    )  # Minimal Django settings required for our tests
        django.setup()  # configures Django
        TestRunner = get_runner(settings)  # Gets the test runner class
        test_runner = TestRunner()  # Creates an instance of the test runner
        
failures = test_runner.run_tests(["tests"])  # Run tests and gather
failures
        sys.exit(bool(failures))  # Exits script with error code 1 if any failures
