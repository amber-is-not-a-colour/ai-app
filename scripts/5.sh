#!/usr/bin/env bash

mkdir -p /tmp/testdir && echo "Can create directories in /tmp" || echo "Cannot create directories in /tmp"
rm -rf /tmp/testdir && echo "Can remove directory trees" || echo "Cannot remove directory trees"