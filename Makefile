.PHONY: type.check
type.check:
	@pipenv run mypy @.mypy_check_files --config-file=$(CURDIR)/mypy.ini

.PHONY: lint.check
lint.check:
	@pipenv run pylint --rcfile $(CURDIR)/.pylintrc app.py src
