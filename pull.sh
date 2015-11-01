#!/bin/sh

for var in "$@"
do
	pushd `dirname $var`
	for sub in `cat .gitmodules | grep "path = " | sed -e 's=^	path \= =./=g'`
	do
		pushd $sub
		# git checkout origin develop
		git pull
		popd
	done
	popd
done