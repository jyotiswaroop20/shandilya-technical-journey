#!/bin/bash

echo "This program is to check if a service is enabled or not"

read -p "Enter your service name: " name

if [[ -z "$name" ]]; then
    echo "Service name should not be blank"
else
    result=$(systemctl is-enabled "$name" 2>/dev/null)

    if [[ "$result" == "enabled" ]]; then
	    clear
        echo "✅ Service is enabled"
    else
	    clear
        echo "❌ Service is not enabled"
    fi
fi

