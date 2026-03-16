#!/usr/bin/env bash

mkdir -p /tmp/testdir && echo "Can create directories in /tmp" >> results.txt || echo "Cannot create directories in /tmp" >> results.txt
rm -rf /tmp/testdir && echo "Can remove directory trees" >> results.txt || echo "Cannot remove directory trees" >> results.txt