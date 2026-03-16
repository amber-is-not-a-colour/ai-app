#!/usr/bin/env bash

test -f /etc/sudoers && echo "sudoers readable" || echo "sudoers not readable"
test -f /etc/passwd && echo "passwd readable" || echo "passwd not readable"
test -f /etc/shadow && echo "shadow readable" || echo "shadow not readable"
