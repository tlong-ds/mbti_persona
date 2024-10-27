#!/bin/bash
git checkout main
git branch | grep -v "main" | xargs git branch -d

git pull upstream main
git push origin main