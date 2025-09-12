#!/bin/bash
echo "Installing the Software of httpd"
dnf install httpd -y
systemctl start httpd
systemctl enable --now httpd
systemctl status httpd
