---
description: git related documents
---
# Git

```
# ~/.bashrc 

alias gaa="git add *"
alias gc="git commit -m 'add new content'"
alias gacp="gaa & gc & git push"
alias gitit="git commit -pm '`git status -s` Edit# `git log | grep commit | wc -l`'; git push"


```