#!/bin/sh

if [ "$1" == "clean" ]; then
	find . -name "*.pyc" -exec rm {} \;
fi

if [ "$1" == "build" ]; then
	python setup.py --user
fi

if [ "$1" == "update" ]; then
	git submodule update --init --recursive
fi