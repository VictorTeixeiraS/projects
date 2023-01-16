# NPM init and Hello World

`npm` stands for "Node Package Manager". By installing Node.js, you've gained two new commands:

* `node` - The JavaScript runtime. This will let you run your JavaScript files.
* `npm` - The package manager. This manages dependencies, metadata, and allows you to specify "scripts" to run.

**Most JS devs don't run the `node` command directly, they use it within an npm script.**

## npm init

Start a new node project by typing `npm init`. This command will prompt you with a series of questions. For this project, you can either press enter for the recommended defaults or follow the prompts. Once you have completed the `npm init` process, add a `main.js` file to the root of your project. For now, add a simple `console.log` command

```js
console.log('hello world')
```

to that file. This will be the entry point.

Next, edit the `package.json` file that was created during `npm init`. The scripts section should have something like:

```json
...
"scripts": {
  "start": "node main.js"
},
...
```

That adds a "start" script to this project that runs `main.js` using `node`. With all that ready to go, simply run:

```bash
npm start
```

And you should see your "hello world" message logged to the console!

## .gitignore

A `.gitignore` file is used to tell Git which files or folders to ignore when committing changes to a repository. This is useful for ignoring files that are specific to your local development environment or files that should not be tracked in the repository, such as compiled files or sensitive information.

Create a `.gitignore` file at the project root (with the leading period). Have git ignore the `node_modules/` directory.
