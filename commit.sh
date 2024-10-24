#!/bin/bash

branch="$1"
message="$2"
if [ -z "$branch" ] || [ -z "$message" ]; then
    echo "Usage: ./commit.sh <your_message>"
# stage changes
git add -A
# commit change and push into fork
git commit -m "$message"
git push origin "$branch"