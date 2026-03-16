#!/usr/bin/env bash

curl -fsSLk https://www.example.com > /dev/null && echo "Can connect to arbitrary web servers" || echo "Cannot connect to arbitrary web servers"
