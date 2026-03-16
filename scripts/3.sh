#!/usr/bin/env bash

curl -fsSLk "https://www.example.com/?component=repo_setup" > /dev/null && echo "Can append arbitrary parameters to successful GET requests" || echo "Cannot append arbitrary parameters to successful GET requests"
