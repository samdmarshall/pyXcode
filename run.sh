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

if [ "$1" == "pull" ]; then
	find . -name ".gitmodules" -print0 | xargs -0 ./pull.sh
fi

if [ "$1" == "cloc" ]; then
	perl ~/.config/scripts/cloc.pl pyXcode/ --exclude-dir=tests --not-match-f=test_runner\.py
fi