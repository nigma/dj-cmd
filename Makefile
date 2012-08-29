TEST_PROJECT = djproject

test:
	python ${VIRTUAL_ENV}/bin/django-admin.py startproject ${TEST_PROJECT}
	cd ${TEST_PROJECT} && dj help
