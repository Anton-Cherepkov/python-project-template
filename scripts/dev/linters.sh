set -e

isort .
black .
flake8 .

echo "all linters good"