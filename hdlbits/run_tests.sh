#!/bin/bash

set -euo pipefail

MODULE_NAME=top_module.sv

test() {
    file=$1
    path=$(dirname $file)

    echo "Running test for $path ..."
    pushd $path > /dev/null
        result=$(make 2>&1)

        if echo $result | grep -q "test failed"; then
            echo "  FAILED!"
            echo "Test details:"
            echo -e "$result"
            exit 1
        fi
    popd > /dev/null
}

find . -name $MODULE_NAME | while read file; do test "$file"; done