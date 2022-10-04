# Making your First Commit

When using git to manage your code, you make changes to your code via [commits](https://github.com/git-guides/git-commit). Good commits tend to be small. For example, you might create a commit and push it up to GitHub each time you:

* Add a new feature
* Fix a new bug
* Rework a bit of your code to be more readable

I usually make 2 or 3 commits for each hour I spend coding - that's not a hard rule, but a good estimate of where you should be.

## First, make a code change

Let's change your [README.md](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) file. A README is a [markdown](https://www.markdownguide.org/getting-started/) file that explains what your project is and how to run it. It's a form of documentation.

Open your `README.md` in the VS Code file explorer and add a small description to the bottom that says something like:

```
BookBot is my first git project!
```

Save the file with `ctrl + s`.

## Next, view your diff

A "diff" is a visual aid that shows you the differences between two files. Now that you've saved a change, you should see a blue notification pill on the "source control" icon on the left of your VS Code window.

![source control tab vs code](https://i.imgur.com/MR4N8yx.png)

Click on it, and under "changes" take a look at your `README.md` file - you should see the diff view.

I recommend using UI tooling (like this diff view) for *visualizing* your changes, but I recommend using the command line for *applying* changes to git. If your change looks good to you, let's push it up to GitHub.

## Stage the change

First, let's [stage](https://www.git-tower.com/help/guides/working-copy/stage-changes/windows#:~:text=The%20%22Staging%20Area%22,%2C%20by%20%22staging%22%20it.) the change. Run this command from the root of your repo in the terminal:

```bash
git add .
```

The "." tells git to stage *all* the changes in the directory and all subdirectories. If you only wanted to stage *specific* files, you could list the files one by one. I use the "." to stage *everything in the repo* 99% of the time. If you need git to ignore files in your project, you can use a [.gitignore file](https://www.freecodecamp.org/news/gitignore-what-is-it-and-how-to-add-to-repo), which we'll cover later.

## Commit the change

Next, we'll commit the change with a message. The commit message will be stored in git alongside the change. In the future, if you wanted to revert this change, or jump back in time to the code at this state, you would use the commit message to find the right change. As such, try to use a descriptive commit message!

Run this command:

```bash
git commit -m "update readme with a description"
```

## Push the change to GitHub

Now that your change been committed *locally*, you should notice that your source control tab on the left no longer has a blue notification - all your changes are committed! However, the commit hasn't been pushed up to GitHub yet for safekeeping. Run this command:

```bash
git push origin main
```

`git push` pushes local changes to a remote location - like GitHub. `origin` is a name that refers to your GitHub repo for this project; it was configured automatically when you cloned your repo. `main` is the name of the default [branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches) for your repo. We'll talk more about branches later.

Once you've pushed, navigate to your repo on GitHub and take a look at the README - you should see your changes!
