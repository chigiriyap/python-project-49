install:
	uv sync

brain-progression:
	uv run brain-progression

brain-gcd:
	uv run brain-gcd

brain-calc:
	uv run brain-calc

brain-even:
	uv run brain-even

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

.PHONY: install brain-games build package-install lint

