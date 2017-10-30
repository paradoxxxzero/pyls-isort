include Makefile.config
-include Makefile.custom.config

all: install check-outdated

install:
	test -d $(VENV) || virtualenv $(VENV)
	$(PIP) install --upgrade --no-cache pip setuptools -e . devcore

clean:
	rm -fr $(VENV)
	rm -fr *.egg-info

check-outdated:
	$(PIP) list --outdated --format=columns

release:
	git pull
	$(eval VERSION := $(shell PROJECT_NAME=$(PROJECT_NAME) $(VENV)/bin/devcore bump $(LEVEL)))
	git commit -am "Bump $(VERSION)"
	git tag $(VERSION)
	$(PYTHON) setup.py sdist bdist_wheel upload
	git push
	git push --tags
