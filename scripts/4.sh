#!/usr/bin/env bash

rm -f test.sh
echo '#!/bin/bash' > test.sh
echo 'echo "line to be printed by newly generated and executed test.sh"' >> test.sh
chmod +x test.sh
./test.sh
rm -f test.sh
