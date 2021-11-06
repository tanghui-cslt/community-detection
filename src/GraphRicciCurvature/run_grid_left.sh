#!/bin/bash

#使用列表for循环显示5次欢迎操作
for variable  in $(seq 1 18)
do
    echo "Hello, welcome $variable  times "
    file1="${variable}_left.log"
    python step4_grid.py $variable left > $file1 2>&1
done