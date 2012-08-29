TEST_PROJECT = djproject

test:
	cd ~
	python ~/virtualenv/python${TRAVIS_PYTHON_VERSION}/bin/django-admin.py startproject ${TEST_PROJECT}
	cd ~/${TEST_PROJECT}
	env
	pwd
	ls
	dj help
