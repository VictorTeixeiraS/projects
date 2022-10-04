# Command Line Interface

*If you already have a favorite CLI, and already know how to use it, you can skip this step.*

A [command line interface](https://en.wikipedia.org/wiki/Command-line_interface), or CLI, is a developer's best friend. Many of the tasks you do as a developer are most effectively done on the command line.

In Boot.dev courses you're used to running your code by clicking a "run" button. As a developer, you'll most likely run your code using a command line instead. For example, if your Python code is in a file called `main.py`, you would run:

```bash
python main.py
```

## Where is the command line?

There are different ways to open a command line prompt depending on your operating system. The easiest way is to access it directly inside of VS Code.

![cli in vs code](https://i.imgur.com/l9POGK3.png)

First, open VS code. At the bottom of the screen you should see a command line. If you don't see it, you can press:

```
ctrl + `
```

to open it.

## Using the command line

We want you using [Bash](https://www.gnu.org/software/bash/manual/html_node/What-is-Bash_003f.html) (or the nearly-identical [Zsh](https://en.wikipedia.org/wiki/Z_shell)) as the shell language for your terminal. Bash is the language that almost every programmer uses to interact with a command line. Read the section below about how to set up a shell for your specific operating system.

### Here's where you can see which shell language you're using in VS Code

![shell language VS Code](https://i.imgur.com/ZHle30O.png)

### For Mac OS:

You should see in the top-right of your VS Code *terminal* a little "[zsh](https://en.wikipedia.org/wiki/Z_shell)" label. "zsh" or "z shell" is a Unix shell that's *very* similar to "[bash](https://www.gnu.org/software/bash/manual/html_node/What-is-Bash_003f.html)". If it says "zsh", you're good to go! Skip down to the "run a command" section.

If it doesn't say `zsh`, you can use the icons next to it to change it. If you can't find `zsh` reach out in the Discord for help. You should be good to move on to the "run a command" step!

### For Linux / Windows (WSL)

You should see in the top-right of your VS Code *terminal* a little "[bash](https://en.wikipedia.org/wiki/Z_shell)" label.

If it doesn't say `bash`, you can use the icons next to it to change it. If you can't find `bash` reach out in the Discord for help. You should be good to move on to the "run a command" step!

## Run a command

Now that you've got VS Code open with a `bash` or `zsh` terminal, type `pwd` in the command prompt and press `enter`. `pwd` stands for "print working directory", so you should get back the path of your working directory. If you do, you're good to move on!

If you're stuck, reach out in the Discord for help.
