BINARY_NAME=image_compressor.exe
.DEFAULT_GOAL := all

dependencies:
	python -m venv env
	env\Scripts\activate
	python -m pip install --upgrade pip
	pip install -r requirements.txt

compile:
	pyinstaller -F src\main.py -n ${BINARY_NAME} --clean --noconsole
