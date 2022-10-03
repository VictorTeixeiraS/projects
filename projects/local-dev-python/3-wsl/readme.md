# Installing Windows Subsystem for Linux

*If you're on Mac or Linux, or already have WSL2 configuring, you can skip this step.*

## Make sure you're on Windows 10 or 11

If you are on an older version, **please upgrade**. Your life as a developer will not be fun if you're on such an old version of Windows.

The built-in Windows command line (which we'll explain more in the next step) is, simply put *terrible*. It's *so bad* that if you're on Windows we're just going to have you install WSL 2 (Windows Subsystem for Linux). This will allow you to use your normal Windows desktop, but *also* have a Linux command line you can use for development. WSL2 was a *huge* step forward for developers on Windows. Don't worry, WSL is a microsoft product that's built to work with Windows. It won't mess up your current Windows installation.

### 1. Run Windows Update

Click on the start menu and begin typing "windows update". You should see a program called "Windows Update Settings", open that. Click "check for updates", and if there are any updates, install them and restart your computer as instructed by the updater.

### 2. Open the Windows Command Prompt and install WSL

2a. Click on the start menu and begin typing "cmd.exe". You should see a program called "Command Prompt", *right-click* on it and select "Run as administrator".

2b. Type `wsl --install` in the prompt and press enter.

2c. Restart your computer

### 3. Setting up the Ubuntu distro

Ubuntu is a very popular distribution (or distro) of Linux, and it was installed automatically alongside WSL.

3a. After restarting your computer in step 2, you should see an "Ubuntu" Window open automatically once you log back in. If you don't, search for the "Ubuntu" program in the start menu and launch it.

3b. The Ubuntu window will prompt you to enter a username and password. Make sure you remember these! These are the credentials for your Linux user.

### 4. Using WSL in VS Code

4a. Open VS Code and navigate to the "Extensions" menu on the left hand toolbar. 

4b. Search for and install the ["WSL extension by Microsoft"](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl).

4c. In the very bottom-left of VS Code there should be a green button. Click on that and select "New WSL Window using Distro..." and select "Ubuntu".

You should now have a new WSL-ready VS Code editor! You can close the other VS Code window. **I recommend pinning this new window to your task bar so that you can always open the WSL-enabled version of VS Code in one click.** If you're ever in the "regular" VS Code window you won't have access to your Linux filesystem, so I'd just avoid it completely.

If you have issues, reach out to us for help in the Discord. You can also poke around the [official WSL tutorial](https://learn.microsoft.com/en-us/windows/wsl/install) and the official [WSL-Remote VS Code plugin](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) tutorial.

**You're good to move on to the next step.**
