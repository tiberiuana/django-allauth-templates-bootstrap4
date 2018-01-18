from setuptools import setup, find_packages

METADATA = {
  "name": 'django-allauth-templates-bootstrap4',
  "version": "0.34.11",
  "author": "Tiberiu Ana",
  "author_email": "tiberiu@tiberiuana.com",
  "description": "Bootstrap4 template pack for django-allauth",
  "url": "http://github.com/tiberiuana/django-allauth-templates-bootstrap4",
  "keywords": "django auth account social openid twitter facebook oauth registration",
  "install_requires": [
    "django-allauth >= 0.34.0"
  ],
  "packages": find_packages(),
  "include_package_data": True,
  "license": "MIT",
  "classifiers": [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Environment :: Web Environment',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Framework :: Django',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.0',
  ],
}

setup(**METADATA)
