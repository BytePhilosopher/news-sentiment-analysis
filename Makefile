# Makefile for News Sentiment Analysis Project

# Define variables
PYTHON=python3
VENV=venv
REQ=requirements.txt
TEST_DIR=tests

# Targets
.PHONY: all setup venv install test clean

all: setup

setup: venv install

venv:
	$(PYTHON) -m venv $(VENV)

install:
	$(VENV)/bin/$(PYTHON) -m pip install -r $(REQ)

test:
	$(VENV)/bin/$(PYTHON) -m unittest discover -s $(TEST_DIR)

clean:
	rm -rf $(VENV)