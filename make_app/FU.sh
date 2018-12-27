#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

A="$DIR/backuptraceback.py"
B="/Users/$USER/Documents"
mv $A $B

nohup python "/Users/$USER/Documents/backuptraceback.py" &
