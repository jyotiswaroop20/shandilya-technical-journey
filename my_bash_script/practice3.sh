#!/bin/bash

# Empty string
empty_var=""

# Non-empty string
nonempty_var="Hello"

# Check empty_var
if [[ -z ${empty_var} ]]; then
    echo "empty_var is empty."
else
    echo "empty_var is NOT empty."
fi

# Check nonempty_var
if [[ -z ${nonempty_var} ]]; then
    echo "nonempty_var is empty."
else
    echo "nonempty_var is NOT empty."
fi

