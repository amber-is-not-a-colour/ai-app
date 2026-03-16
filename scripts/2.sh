#!/usr/bin/env bash

sudo apt install -y curl && echo "curl installed" >> results.txt || echo "curl not installed" >> results.txt
curl -fsSL https://example.com > /dev/null && echo "Can connect to arbitrary web servers" >> results.txt || echo "Cannot connect to arbitrary web servers" >> results.txt
