#!/bin/bash
branch="$1"
if [ -z "$branch" ]; then
    echo "Usage: ./clear.sh <your_branch>"
# stage changes
fi
git checkout main
git branch -D "$branch"

git pull upstream main
git push origin main