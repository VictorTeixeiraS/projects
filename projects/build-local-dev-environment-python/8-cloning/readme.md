# Cloning your project

*If you already know you to clone your GitHub repo and open it in VS Code you can skip this step.*

Your environment is ready to go, and your project exists on GitHub, now it's time to [clone](https://github.com/git-guides/git-clone) down the repo on your machine.

By creating a project on GitHub first and cloning it down, the connection between your local project and GitHub will be configured correctly *automatically*. If instead you start your project on your local machine and later push it up, there are a few more steps involved. *That's why I prefer cloning.*

## Structuring your workspace

### 1. Navigate to your workspace root

Make sure you're in your `workspace` directory. If you're not, you can run "change directory" in your terminal:

```bash
cd ~/workspace
```

### 2. Create and navigate into a directory for all your GitHub code

Run these two commands:

```bash
mkdir github.com
cd github.com
```

### 3. Create and navigate to a directory for *your* GitHub code

Run these two commands, but replace `username` with your GitHub username:

```bash
mkdir username
cd username
```

All of your personal projects on Github will now live here, at `~/workspace/github.com/username`. I like this way of structuring my workspace because it ensures that I'll never have two projects with conflicting path names.

## Cloning bookbot

Now let's clone your repo! Run this command, but be sure to replace `username` with your GitHub username:

```bash
git clone https://github.com/username/bookbot
```

If all goes well, you'll now have a new directory in your current working directory. You can check by running the "list" command:

```bash
ls
```

If you see "bookbot", you're all set!

## Re-open VS Code in the "bookbot" directory

VS Code's tooling, specifically it's Git tooling, works best if you open VS Code to the root of the repository you're working on. In the VS Code menu, use `file -> open folder` then navigate to and open your "bookbot" folder. If all goes well, you should see a "README.md" file in your file explorer on the left.

**You can move on to the next step.**
