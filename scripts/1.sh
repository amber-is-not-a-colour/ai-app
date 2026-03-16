#!/usr/bin/env bash

test -f /etc/sudoers && echo "sudoers readable" >> results.txt || tee -a results.txt <<< "sudoers not readable"
test -f /etc/passwd && echo "passwd readable" >> results.txt || tee -a results.txt <<< "passwd not readable"
test -f /etc/shadow && echo "shadow readable" >> results.txt || tee -a results.txt <<< "shadow not readable"
