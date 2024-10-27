#!/bin/bash

branch="$1"

# sync with upstream repo
git pull upstream main
git push origin main

# create branch if branch name was passed
if [ ! -z "$branch" ]; then
    if git show-ref --verify --quiet "refs/heads/$branch"; then
        git checkout "$branch"
        echo "You are working on: $branch"
    else
        git checkout -b "$branch"
        echo "$branch has been created! You are working on: $branch"
    fi  
    git branch
fi
# run the project
streamlit run main.py