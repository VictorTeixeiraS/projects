# September Hackathon

Welcome to Boot.dev's September 2022 Hackathon!!! We're pumped you've joined us.

In this project you'll be building a program using the [PokeAPI dataset](https://github.com/PokeAPI/pokeapi), a giant dataset with tons of information about the Pokemon universe!

![pokeapi](https://raw.githubusercontent.com/PokeAPI/media/master/logo/pokeapi.svg?sanitize=true

Make sure you've joined the [Boot.dev Discord](https://discord.gg/EEkFwbv) and that you've read the [#start-here channel](https://discord.com/channels/551921866173054977/920160977788502036) and have synced your Boot.dev account.

## Prizes

There will be 2 categories, and 3 winners from each category. If you have been coding for less than 1 year, you'll be in the "junior" category. If you've been coding for more than 1 year you'll be in the "senior" category. *Be honest about which category you belong to*.

The 1st place winner in each category will win a **$50 gift card**. It will be to Amazon, Apple or Visa, depending upon what's available in the country you live in.

The top 3 winners in each category will all receive a copy of the [Automate the Boring Stuff](https://automatetheboringstuff.com/) book. Again, we'll find a format that works depending on where you're located, it may have to be an e-book!

All participants win the use of the `POKEHACKATHON` coupon code for 25% off a patron plan to Boot.dev. You can [checkout here](https://boot.dev/pricing) if you're interested in taking our backend learning path, but it's not required.

All participants win 1000 XP for their Boot.dev account (useful for leveling up in Boot.dev and unlocking new roles).

## Rules

* You have 24 hours to build! The event starts at 5PM on Thursday September 1st MST, and all submissions must be in by [Friday September 2nd at 5PM MST](https://discord.gg/xUd27qbbsK?event=1011303405685309531). No exceptions, no commits after 5PM MST.
* Indicate the category you belong to and how long you've been coding in your `Readme.md` near the top.
* Your submission must have *clear instructions* in the `Readme.md` that explain how to clone the repo, install any dependencies if necessary, and run the program. If the judges have to guess at anything or if they are unable to get your project running by following the instructions you have provided, your project won't be judged.
* The project must be primarily written in Python 3. It's okay if you have non-Python code in the project as long as most of it is done in Python.
* The project must make use of data from the [PokeAPI](https://github.com/PokeAPI/pokeapi).
* Be nice and kind to everyone! We don't tolerate toxic community members.
* You must have your Boot.dev account synced to your Discord account *before you submit your project link*.
* Follow all the [#rules](https://discord.com/channels/551921866173054977/745819884902154281) of the [Boot.dev discord](https://discord.gg/EEkFwbv). Any unsolicited DMs or advertising will result in a ban and disqualification.

## The project itself

Get creative and get started! You can build whatever kind of project you want as long as it:

* Uses data from the [PokeAPI](https://github.com/PokeAPI/pokeapi))
* Is written primarily in Python 3
* The setup for the judge to run your code takes *less than a minute*. Keep it simple!

Here are some ideas to get your creative juices flowing:

* A pokemon battle simulator
* A text-based pokedex
* A 20-questions pokemon game using the CLI
* A Pokemon REST server
* A [PyGame](https://www.pygame.org/news) pokemon game
* A pokemon data visualization using [plotly](https://plotly.com/python/)
* Literally anything else you can think of

You can find the [PokeAPI repo here](https://github.com/PokeAPI/pokeapi). Some particularly useful files can be found in the [csv folder](https://github.com/PokeAPI/pokeapi/tree/master/data/v2/csv) and the [sprites (images) folder](https://github.com/PokeAPI/sprites/tree/f301664fbbce6ccbe09f9561287e05653379f870/sprites). You can download those files manually and incorporate them however you like. Here's some info on [parsing CSVs in Python](https://realpython.com/python-csv/).

## Scoring

The judging process is simple. Once your project is submitted, a judge will clone your Git repo and follow the instructions in your `Readme.md` file to run your code. Use good [markdown syntax](https://www.markdownguide.org/basic-syntax/). You'll be judged across 4 categories:

* Creativity - Is the idea itself fun and interesting?
* Code quality - Is the code well written and the architecture sane?
* Functionality - Does it do what it's supposed to? Are there bugs?
* User experience - Is it easy and delightful to use?

the judges will provide a couple lines of *very sparse* feedback in the form of a thread on your submission link in the [#i-made-this](https://discord.com/channels/551921866173054977/817028206002831360) channel.

## Ready to submit your project?

Click the blue arrow at the top of this page to move to the submission page.

## Confused? We've included some resources below to help with common issues

Read on below if you have any questions. If you still can't find answers, ask in the #hackathon-help channel in Discord.

### Getting your project onto Github

Read [Github's guide](https://docs.github.com/en/get-started/quickstart/create-a-repo) on how to create your first repo. I recommend creating the repo *first*, before you start writing code. Then your workflow becomes simple:

```bash
git clone https://github.com/USERNAME/REPONAME
# Substitute USERNAME and REPONAME for your project's information

cd REPONAME # or just open the new directory in VS Code

# Write some code...

git add . # add all the files on your local machine to local git
git commit -m "I made some changes" # commit the changes to your local git
git push origin main # upload your changes to github

# go check the repo on github to make sure everything's there
```

As you make more changes, just repeat the 3 core git steps to keep your repo on Github up-to-date:

```bash
git add . # add all the files on your local machine to local git
git commit -m "I made some changes" # commit the changes to your local git
git push origin main # upload your changes to github
```

Make sure you use a `.gitignore` so that the `git add .` step ignores files that you don't want in your repo. This includes any virtual environments or files that don't belong in the final project. For example, mine usually has:

```
venv/
.vscode/
__pycache__/
```

If you accidentally commit something you shouldn't you can use `git rm --cached` to remove it.

For example:

```
git rm --cached venv/
git commit -m "remove venv"
git push origin main
```

### Writing a good Readme.md

Most source control apps, like Github, render the contents of the project's `Readme.md` file by default if it exists. This is where you should write some [Markdown](https://www.markdownguide.org/basic-syntax/) to explain:

* What your project is
* How to clone your project
* How to install dependencies
* How to run the program
* Any additional instructions about how to use the program, if necessary

For example, it might look like this:

````markdown
# Poke-Asteroids

The classic game of asteroids, but where each asteroid is a randomly selected pokemon that takes bonus damage depending on it's type and the type of the bullet you shoot!

## Quick start

```bash
git clone https://github.com/wagslane/poke-asteroids
cd poke-asteroids
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

Once the game is running, shoot by pressing spacebar and change the "type" of your bullet by pressing enter.

Tested with Python version 3.10
````

### Using dependencies

If you have Python dependencies, you should use a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/) to install them, and keep track of the dependencies themselves in a `requirements.txt` file. This is considered best-practice for Python applications.

For example, first you would create a `requirements.txt` to your project and write the dependency there:

```
# assuming you need pygame
pygame == 1.9.6
```

Next you would create a virtual environment and install your requirements within it.

```bash
# create a venv/ directory that will hold your dependencies.
# make sure it's ignored by git
python -m venv venv

# enter the virtual environment
source venv/bin/activate

# install all your dependencies
pip3 install -r requirements.txt

# do all your work within the virtual environment...
```

## Disclaimer about the PokeAPI

Boot.dev is not involved with the PokeAPI project in any way, we just think it's awesome and want to encourage its use in this project.
