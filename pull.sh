#!/bin/sh

for var in "$@"
do
	pushd `dirname $var`
	pushd `cat .gitmodules | grep "path = " | sed -e 's=^	path \= =./=g'`
	# git checkout origin develop
	git pull
	popd
	popd
done