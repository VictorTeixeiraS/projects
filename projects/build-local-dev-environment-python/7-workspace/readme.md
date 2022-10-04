# Your Workspace

*If you already have a system you love for organizing projects on your computer, you can skip this step.*

Many developers spend years haphazardly writing code and maintaining projects all across their filesystem. I'll introduce you to how I manage my code on my machine. You can organize your code however you prefer, but this has been a method that's served me well for many years. If you don't like this method, that's okay, but please have *a* system.

## Create your workspace

### 1. Navigate to your home directory

Inside your terminal run the "change directory" command to switch to your [home directory](https://wiki.debian.org/home_directory):

```bash
cd ~/
```

`~/` is a symbol on UNIX systems that refers to your home directory.

### 2. List the contents of your home directory

Run the "list" command:

```bash
ls
```

You should see all the files and folders in your home directory, if there are any.

### 3. Create your "workspace" folder:

Run a "make directory" command to create a "workspace" folder:

```bash
mkdir workspace
```

You can make sure it was created successfully by running `ls` again.

### 4. Navigate into the workspace folder

Then "change directory":

```
cd workspace
```

## Keep *all* of your code in your workspace

All of your projects will live here, in your workspace. In the VS Code menu, run `file -> open folder` and open your workspace folder. Now your command line and your VS Code file explorer will both be rooted in your "workspace". To test this, create a text file in VS Code by right clicking in the file explorer and selecting "new file". Once the file is made, run `ls` in the terminal again. You should see your file! If you don't, reach out for help in the Discord. You can delete the test file by running the "remove" command:

```bash
rm name_of_file
```
