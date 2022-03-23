.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

# sphinx

SPHINXOPTS    =
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = poc-multi-api
SOURCEDIR     = docs/
BUILDDIR      = docs/_build

# docker
DOCKER=docker-compose --env-file .env --file docker/docker-compose.yaml
SERVICES=

.PHONY:help
help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.PHONY:clean
clean: ## remove build artifacts, compiled files, and cache
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

.PHONY:lint
lint:
	pre-commit run --all-files

.PHONY:test
test: ## run tests quickly with the default Python
	pytest

.PHONY:docs
docs: ## generate Sphinx HTML documentation, including API docs
	rm -rf docs/_build
	# sphinx-apidoc -o docs/_build poc_multi_api
	#$(SPHINXBUILD) "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	mkdocs build

.PHONY:build
build:
	poetry build

# docker


.PHONY:docker-build
docker-build:
	$(DOCKER) build
	$(DOCKER) pull


.PHONY:docker-start
docker-start:
	$(DOCKER) up -d ${SERVICES}


.PHONY:docker-stop
docker-stop:
	$(DOCKER) stop ${SERVICES}


.PHONY:docker-restart
docker-restart: docker-stop docker-start
	echo "[II] Docker services restarted!"


.PHONY:docker-logs
docker-logs:
	$(DOCKER) logs --follow --tail 100 ${SERVICES}

.PHONY: docker-wait
docker-wait:
	echo ${SERVICES} | xargs -t -n1 ./docker/healthcheck.sh
