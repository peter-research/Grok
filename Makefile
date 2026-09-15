.PHONY: check test

check: test
	python3 grok.py check

test:
	python3 -m unittest -v test_grok.py test_v030.py test_v031.py test_v032.py test_v033.py test_v034.py test_v035.py
