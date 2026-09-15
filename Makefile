.PHONY: check test

check: test
	python3 grok.py check

test:
	python3 -m unittest -v test_grok.py test_v030.py test_v031.py
