TEST_PROJECT = djproject

test:
	django-admin startproject ${TEST_PROJECT}
	cd ${TEST_PROJECT}/${TEST_PROJECT}
	dj help || exit 1
