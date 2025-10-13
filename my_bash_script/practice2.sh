#!/bin/bash

var=100

if [[ -v var ]]; then
        echo "Variable assign true"
else
        echo "Variable not assogned and not found"
fi

