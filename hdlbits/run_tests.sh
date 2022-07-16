#!/bin/bash

set -euo pipefail

MODULE_NAME=top_module.sv

ntests=1

test() {
    file=$1
    path=$(dirname $file)

    echo "  * $path ... ($ntests)"
    pushd $path > /dev/null
        result=$(make 2>&1)
        ntests=$((ntests+1))

        if ! echo $result | grep -q "test passed"; then
            echo "  FAILED!"
            echo "Test details:"
            echo -e "$result"
            exit 1
        fi
    popd > /dev/null
}

echo "Running tests"
find . -name $MODULE_NAME | while read file; do test "$file"; done