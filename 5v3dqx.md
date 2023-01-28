Git & GitHub Sheet
======================================

Initializing and Cloning
------------------------

*   `git init`: Initialize a new git repository
*   `git clone [url]`: Clone a repository from a remote source

Staging and Committing
----------------------

*   `git add [file]`: Add a file to the staging area
*   `git commit -m "[message]"`: Commit the changes with a message
*   `git commit -a -m "[message]"`: Commit all changes in the working directory, including modifications and deletions, with a message
*   `git commit --amend`: Modify the most recent commit
*   `git commit --amend -m "[new message]"`: Modify the most recent commit and change its commit message
*   `git commit --amend --no-edit`: Modify the most recent commit without changing the commit message

Viewing Repository Status
-------------------------

*   `git status`: Show the status of the current repository
*   `git log`: Show the commit history
*   `git log -n [number]`: Show the last `n` commits in the commit history
*   `git log --oneline`: Show a condensed view of the commit history
*   `git log --stat`: Show the commit history with the number of lines added, modified and deleted in each commit
*   `git diff`: Show the differences between the working directory and the last commit
*   `git diff [branch1] [branch2]`: Show the differences between the two specified branches

Branching
---------

*   `git branch`: Show the current branch
*   `git branch [name]`: Create a new branch with the given name
*   `git checkout [branch]`: Switch to the specified branch
*   `git checkout -b [name]`: Create a new branch and switch to it
*   `git merge [branch]`: Merge the specified branch into the current branch
*   `git branch -d [name]`: Delete the specified branch
*   `git branch -D [name]`: Force delete a branch

Merging
-------

*   `git merge [branch]`: Merge the specified branch into the current branch
*   `git merge --abort`: Abort the current merge process

Reverting
---------

*   `git revert [commit]`: Revert the specified commit
*   `git reset [commit]`: Reset the repository to the specified commit
*   `git reset --hard [commit]`: Reset the repository to the specified commit and discard any changes in the working directory
*   `git clean -f`: Remove untracked files from the working directory


Tagging
-------

*   `git tag`: Show the list of tags
*   `git tag [name]`: Create a new tag with the given name




Remote Repositories
-------------------

*   `git remote -v`: Show the list of remote repositories and their URLs
*   `git remote add [name] [url]`: Add a new remote repository with the given name and URL
*   `git remote remove [name]`: Remove the specified remote repository
*   `git fetch [remote]`: Fetch changes from a remote repository
*   `git pull [remote] [branch]`: Pull changes from a remote repository and automatically merge them
*   `git push [remote] [branch]`: Push changes to a remote repository
*   `git push --set-upstream [remote] [branch]`: Set the specified remote repository and branch as the upstream for the current branch

Conflicts
---------

*   `git status`: Show the status of the current repository and any conflicts
*   `git diff`: Show the differences between the working directory and the last commit, including conflicts
*   `git diff --base [file]`: Show the differences between the common ancestor and the current version of a file, including conflicts
*   `git diff [branch1] [branch2] [file]`: Show the differences between the specified branches for a file, including conflicts
*   `git add [file]`: Add a file to the staging area after resolving conflicts
*   `git mergetool`: Open a merge tool to resolve conflicts

GitHub Specific
---------------

*   `git push -u origin [branch]`: Push the current branch to the remote repository and set it as the upstream
*   `git pull origin [branch]`: Pull changes from the specified branch on the remote repository
*   `git pull --rebase origin [branch]`: Pull changes and rebase the current branch onto the remote repository
*   `git branch -r`: Show the list of remote branches
*   `git push origin --delete [branch]`: Delete a remote branch
*   `git fetch origin [branch]:[new_branch]`: Fetch a remote branch and create a new local branch with the given name
*   `git remote prune origin`: Remove remote branches that have been deleted from the remote repository

Advanced Git
------------

*   `git bisect start`: Start the bisect process to find the commit that introduced a bug
*   `git bisect bad`: Mark the current commit as bad
*   `git bisect good [commit]`: Mark the specified commit as good
*   `git bisect reset`: Exit the bisect process and return to the original commit
*   `git blame [file]`: Show the last modification on each line of a file, including the commit and the author
*   `git cherry-pick [commit]`: Apply the changes of a specific commit to the current branch
*   `git reflog`: Show the reference log of the repository, including branch and tag references and their movements
*   `git gc`: Cleanup unnecessary files and optimize the repository


Advanced GitHub
---------------

*   `git pull --rebase upstream [branch]`: Pull changes from an upstream repository and rebase the current branch
*   `git push --force`: Force push changes to a remote repository
*   `git push --force-with-lease`: Force push changes with a "lease" that ensures that the remote branch is updated with the most recent commit
*   `git stash branch [name]`: Create a new branch and apply the changes from the latest stash on top of it
*   `git stash drop [stash]`: Remove a specific stash from the list
*   `git stash list`: Show the list of stashes in the repository
*   `git stash apply [stash]`: Apply the changes of a specific stash to the working directory
*   `git stash pop [stash]`: Apply and remove a specific stash from the list
*   `git stash clear`: Remove all stashes from the repository

Collaboration
-------------

*   `git fork`: Create a copy of a repository on GitHub under your own account
*   `git pull request`: Submit changes to the original repository for review and potential merge
*   `git merge request`: Request the original repository maintainers to merge changes in your fork
*   `git review`: Review changes on pull request and leave comments
*   `git approve`: Approve changes on pull request
*   `git request-changes`: Request changes on pull request before approving
*   `git close`: Close an open pull request
*   `git merge`: Merge approved pull request into the main branch
*   `git tag [version]`: Tag a specific commit with a version number
