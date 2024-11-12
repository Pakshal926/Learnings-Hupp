Here’s the file structured in Markdown format:

```markdown
# Git Commands Guide

This guide covers some essential Git commands, including resetting commits, amending commits, deleting branches, merging branches, and adding submodules.

---

## 1. Git RESET
### How to Revert Changes Inside a Commit Not Pushed to the Remote Repository

To revert changes from the last commit in your Git repository when the commit has not been pushed to the remote repository, use the `git reset` command.

### Understanding `git reset HEAD~`

- **What is `git reset`?**
  - The `git reset` command is used to undo changes in Git history. It can modify the index (staging area) and the working directory depending on the options you use.

- **What does `HEAD~` mean?**
  - `HEAD` refers to the current commit your repository is pointing to. The `~` operator is used to reference previous commits. For example, `HEAD~` refers to the commit just before the current one (i.e., the last commit).

### Using the Command

To revert the last commit but keep the changes in your working directory:

```bash
git reset HEAD~
```

---

## 2. Git AMEND
### Using `git commit --amend`

The `git commit --amend` command allows you to modify the most recent commit. This can be useful if you want to change the commit message, add new changes, or include additional files in the last commit without creating a new one.

### Command to Amend the Last Commit

To amend the last commit while skipping the staging area for modified files:

```bash
git commit -a --amend
```

---

## 3. Deleting a Branch Locally and Remotely

To delete a branch both locally and remotely:

### Commands

```bash
# Delete the branch locally
git branch -d <branch-name>

# Delete the branch remotely
git push origin --delete <branch-name>
```

---

## 4. Merging Branches

To merge two branches:

### Commands

```bash
# Pull the latest changes from each branch
git pull <branch1>
git pull <branch2>

# Check out the branch where the final code should go
git checkout <branch1>

# Push the merged changes to the remote repository
git push origin branch1
```

---

## 5. Adding a Submodule to an Existing Repository

To add a submodule to your existing Git repository:

### Command

```bash
git submodule add <repository-url> <path-in-repo>
```

Replace `<repository-url>` with the URL of the repository you want to add and `<path-in-repo>` with the path in your current repository where the submodule should be added.

---

This document provides a quick reference for essential Git tasks, helping streamline version control workflows.
```
