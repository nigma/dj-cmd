TEST_PROJECT = djproject

test:
	python /home/travis/virtualenv/python${TRAVIS_PYTHON_VERSION}/bin/django-admin.py startproject ${TEST_PROJECT}
	cd ${TEST_PROJECT}/${TEST_PROJECT}
	dj help || exit 1
