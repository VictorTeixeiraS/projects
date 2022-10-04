# Git

*If you already have Git installed and know how to clone your project, you can skip this step.*

## What is Git and why should I care?

[Git](https://git-scm.com/) is *by far* the most popular way for developers to keep track of their code. We use Git because it:

* Keeps a full history of our project's code
* Allows us to "go back in time" in order to revert mistakes
* Makes it easy to merge code changes between multiple developers working on the same project
* Keeps track of all the "versions" of our code in a single place
* Makes it easy to "push" and "pull" code from computer to computer without manually copying files

Git was originally created by [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) the creator of [Linux](https://www.linux.org/), and was made in order to keep track of the Linux codebase. It's an amazing open-source project that's free to use.

## Installing git

Type `git version` into your terminal and press `enter`. If you get back a version number, you're done! Move onto the "Install the Github CLI" step.

If the `git` command isn't found, read on for how to install it on your OS.

### Install Git on Linux (and WSL)

In your VS Code terminal, run this command:

```bash
sudo apt install git
```

If it worked, the `git version` command should now also work.

### Install Git on Mac OS

In your VS Code terminal, run this command:

```bash
xcode-select --install
```

It will install `git` as well as some other common dev tools

If it worked, the `git version` command should now also work.

## Install the Github CLI

Run this command in your terminal to use [webi](https://webinstall.dev/gh/) to install the Github CLI:

```bash
https://webinstall.dev/gh/
```

## Use the Github CLI to Configure Git to use your GitHub Credentials

Run this command in your terminal:

```bash
gh auth login
```

Follow the instructions.

* Use `HTTPS` as your preferred protocol.
* Enter `Y` when asked if you want to authenticate git with your Github credentials.

## Sign in to VS Code with Github

In the bottom-left of your VS Code window you'll see an "accounts" icon.

![vs code accounts button](https://i.imgur.com/ybz4vzV.png)

Sign in to VS Code with your GitHub account. This will keep all your VS Code settings backed-up on your GitHub account in case you switch computers.

**You're good to move to the next step!**
