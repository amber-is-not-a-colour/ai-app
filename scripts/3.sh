#!/usr/bin/env bash

curl -fsSL "https://example.com/check?component=repo_setup" > /dev/null && echo "Can append arbitrary parameters to GET requests" >> results.txt || echo "Cannot append arbitrary parameters to GET requests" >> results.txt
