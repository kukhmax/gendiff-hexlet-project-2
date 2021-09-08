install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

patch:
	poetry install
	poetry version patch
	poetry build
	poetry publish --dry-run --username ' ' --password ' '
	python3 -m pip install --user dist/*.whl