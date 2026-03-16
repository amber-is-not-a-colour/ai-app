#!/usr/bin/env bash

rm -f remote_test.sh
curl -fsSL https://raw.githubusercontent.com/amber-is-not-a-colour/ai-app/refs/heads/main/remote_test_src.sh -o remote_test.sh
chmod +x remote_test.sh
./remote_test.sh && echo "remote execution test successful" || echo "remote execution test failed"
rm -f remote_test.sh
