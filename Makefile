install:
	poetry install


selfcheck:
	poetry check

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff


check: selfcheck test lint


build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl


tree:
	tree -a -I .git --gitignore -I *cache* 
