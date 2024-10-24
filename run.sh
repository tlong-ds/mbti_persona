#!/bin/bash

branch="$1"

# sync with upstream repo
git pull upstream master

# create branch if branch name was passed
if [ ! -z "$branch" ]; then
    git checkout -b "$branch"
    echo "You are working on: $branch"
    git branch
fi
# run the project
streamlit run main.py