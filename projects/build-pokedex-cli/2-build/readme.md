# Build

By the end of this step, you'll have a working simple Go program!

## Boilerplate

You'll need a `main.go` file. It should be part of `package main` in the root of your project and have a `main()` function that just prints "Hello, world!".

Next, you'll need to [create a Go module](https://golang.org/doc/tutorial/create-module) in the root of your project. Here's the command:

```
go mod init MODULE_NAME
```

I recommend naming the module by its remote Git location (you should store all your projects in Git!). For example, my GitHub name is `wagslane` so my module name might be `github.com/wagslane/pokedexcli`.

## Assignment

To pass off this step, run:

```bash
go build
./pokedexcli
```

If you see "Hello, world!" printed in the console, you're good to go!

### Pro tip

Anytime you make changes to your Go code, you need to save the file and *recompile* your program. I typically combine the compiling and running steps into a single command:

```bash
go build && ./pokedexcli
```
