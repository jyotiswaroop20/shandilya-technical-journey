#!/bin/bash

count=1

until [[ $count -gt 10 ]]; do
	if [[ $count == 5 ]]; then
		((count++))
		echo $count
		((count++))
		echo $count
		break
	fi
	echo $count
	((count++))
done
