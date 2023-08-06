!/bin/bash

factorial() {
    local num=$1

    if [ $num -eq 0 ]; then
        echo 1
    else
        local prev_factorial=$(factorial $((num - 1)))
        echo $((num * prev_factorial))
    fi
}