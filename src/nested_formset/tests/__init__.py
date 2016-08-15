import os
import sys


def setup():
    """Perform test runner setup.

    This is its own function so we can easily call it from doctest
    ``testsetup`` blocks.

    """

    os.environ['DJANGO_SETTINGS_MODULE'] = 'nested_formset.test_settings'

    import django
    django.setup()


def run_tests():

    setup()

    from django.conf import settings
    from django.test.utils import get_runner

    TestRunner = get_runner(settings)
    test_runner = TestRunner()

    failures = test_runner.run_tests(
        ['nested_formset'],
    )

    sys.exit(failures)


if __name__ == '__main__':

    run_tests()
