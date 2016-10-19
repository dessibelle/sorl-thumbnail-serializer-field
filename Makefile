.PHONY: docs flake8 test coverage

docs:
	cd docs; make html
	open docs/_build/html/index.html

flake8:
	flake8 --ignore=W999 sorl_thumbnail_serializer

test:
	DJANGO_SETTINGS_MODULE=tests.test_project.settings_test PYTHONPATH=. \
		`which django-admin.py` test

coverage:
	coverage erase
	DJANGO_SETTINGS_MODULE=tests.test_project.settings PYTHONPATH=. \
		coverage run --branch --source=sorl_thumbnail_serializer \
		`which django-admin.py` test
	coverage combine
	coverage html
	coverage report
