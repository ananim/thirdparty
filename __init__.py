import os
import sys

MODULES = (
    'boto',
    'django',
    'beautifulsoup',
    'django_compressor',
    'django-appconf',
    'httplib2',
    'python-nose',
    'django-nose',
    'python-coverage',
    'mongo-python-driver',
    'mongoengine',

    'renames', # not really a module, more like a patches/fixes place
)

thirdparty_root = os.path.realpath(os.path.dirname(__file__))

for mod in MODULES:
    mod_path = os.path.join(thirdparty_root, mod)
    if mod_path not in sys.path:
        sys.path.insert(0, mod_path)
