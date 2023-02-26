# Installing Python

We're going to use [webi](https://webinstall.dev/pyenv/) to install [pyenv](https://github.com/pyenv/pyenv). `pyenv` makes it easy to manage your Python versions - we want to be on the latest version!

## Install pyenv with webi

Run this command to install pyenv with [webi](https://webinstall.dev/pyenv/).

```bash
curl -sS https://webi.sh/pyenv | sh
```

Make sure to follow the instructions and read any warnings.

When you're done, you'll probably need to close your terminal (trash icon in the top-right of the terminal) and, if you are using VS code, re-open it with:

```
ctrl + `
```

## Install Python 3

Now that you have `pyenv`, run this command to install Python 3.10.7:

```bash
pyenv install -v 3.10.7
```

Then set that version as your default:

```bash
pyenv global 3.10.7
```

Finally, make sure that it worked:

```bash
python --version
```

You should get back a Python version.

**If it worked, move to the next step.**

### Having trouble installing pyenv or Python on Linux or Windows (WSL)?

If you're having trouble, try installing the required build tools, then re-running the webi/python installer:

```bash
sudo apt update
```

```bash
sudo apt install -y build-essential zlib1g-dev libssl-dev libreadline-dev libbz2-dev libsqlite3-dev libffi-dev tk-dev
```

```bash
curl -sS https://webi.sh/pyenv | sh
```

```bash
pyenv install -v 3.10.7
```
