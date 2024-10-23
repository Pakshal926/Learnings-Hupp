# Git RESET
## How to Revert Changes Inside a Commit Not Pushed to the Local Repository

To revert changes from the last commit in your Git repository when the commit has not been pushed to the remote repository, 
you can use the `git reset` command. Below is a detailed explanation of how this works and how to use the command.

## Understanding `git reset HEAD~`

1. **What is `git reset`?**
   - The `git reset` command is used to undo changes in the Git history. It can modify the index (staging area) and the working directory depending on the options you use.

2. **What does `HEAD~` mean?**
   - In Git, `HEAD` refers to the current commit your repository is pointing to. The `~` operator is used to reference previous commits. For example, `HEAD~` refers to the commit just before the current commit (i.e., the last commit).

## Using the Command

To revert the last commit but keep the changes in your working directory, use the following command:

```bash
git reset HEAD~
```

# Git AMEND

# Using `git commit -a --amend`

In Git, the `commit --amend` command allows you to modify the most recent commit. This can be useful if you want to change the commit message, add new changes, or include additional files in the last commit without creating a new commit.

## The Command

To amend the last commit while skipping the staging area for modified files, you can use the following command:

```bash
git commit -a --amend

