# Installing Python

We're going to use [webi](https://webinstall.dev/pyenv/) to install [pyenv](https://github.com/pyenv/pyenv). `pyenv` makes it easy to mange your Python versions - we want to be on the latest version!

## Install pyenv with webi

Run this command to install pyenv with [webi](https://webinstall.dev/pyenv/).

```bash
curl -sS https://webi.sh/pyenv | sh
```

Then close your terminal (trash icon in the top-right of the terminal) and re-open it (ctrl + `).

### Have trouble installing pyenv on Linux or Windows (WSL)?

If you're having trouble, try installing the required build tools, then re-running the webi installer:

```bash
sudo apt update
```

```bash
sudo apt install -y build-essential zlib1g-dev libssl-dev
```

```bash
sudo apt install -y libreadline-dev libbz2-dev libsqlite3-dev libffi-dev
```

```bash
curl -sS https://webi.sh/pyenv | sh
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

**If it worked move to the next step.**
