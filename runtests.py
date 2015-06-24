import os
import sys

# try:
#     from django.conf import settings
#
#     settings.configure(
#         DEBUG=True,
#         USE_TZ=True,
#         DATABASES={
#             "default": {
#                 "ENGINE": "django.db.backends.sqlite3",
#             }
#         },
#         ROOT_URLCONF="panels.urls",
#         INSTALLED_APPS=[
#             "django.contrib.auth",
#             "django.contrib.contenttypes",
#             "django.contrib.sites",
#             "panels",
#         ],
#         SITE_ID=1,
#         NOSE_ARGS=['-s'],
#         MIDDLEWARE_CLASSES=(),
#     )
#
#     try:
#         import django
#         setup = django.setup
#     except AttributeError:
#         pass
#     else:
#         setup()
# except ImportError:
#     print 'Install Django'

#
#
#
# import django
# from django.test.utils import get_runner
#
# if __name__ == "__main__":
#     os.environ['DJANGO_SETTINGS_MODULE'] = 'example.test_settings'
#     django.setup()
#     TestRunner = get_runner(settings)
#     test_runner = TestRunner()
#     failures = test_runner.run_tests(["tests"])
#     sys.exit(bool(failures))
