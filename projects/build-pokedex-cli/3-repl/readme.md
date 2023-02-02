# REPL

[REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) stands for "read-eval-print loop". It's a common type of program that allows for interactivity. You type in a command, the program evaluates it and prints the result. You can then type in another command, and so on.

Your command line is a REPL! Our Pokedex will also be a REPL.

## Assignment

Remove your "hello world message".

In this step, your program should start up an interactive REPL when you run it. It should print a prompt, wait for you to type in a command, and then print the result of that command. The prompt should look like this:

```bash
pokedex > 
```

You should have two available commands:

* help: prints a help message describing how to use the REPL
* exit: exits the program

### How to build a REPL

I expect you to figure a lot of this out on your own. Don't be afraid to Google! That said, here are some pointers:

Use an infinite `for` loop to keep the REPL running. At the start of the loop, you should block and wait for some input. Once input is received, you should parse it and then execute a command. Once the command is finished, and any output is printed, you should go to the next iteration of the loop and wait for more input.

* Get input using [bufio.NewScanner](https://pkg.go.dev/bufio#NewScanner), [.Scan](https://pkg.go.dev/bufio#Scanner.Scan), and [.Text](https://pkg.go.dev/bufio#Scanner.Text)
* I recommend storing your commands in a map. Remember, functions are first-class citizens in Go, you can pass them around as values!

Here's a hint:

```go
type cliCommand struct {
	name        string
	description string
	callback    func() error
}

return map[string]cliCommand{
    "help": {
        name:        "help",
        description: "Displays a help message",
        callback:    commandHelp,
    },
    "exit": {
        name:        "exit",
        description: "Exit the Pokedex",
        callback:    commandExit,
    },
}
```

### Example usage

This is what my shell session looked like when I completed this step:

```bash
wagslane@MacBook-Pro-4 src % ./pokedexcli
Pokedex > help

Welcome to the Pokedex!
Usage:

help: Displays a help message
exit: Exit the Pokedex

Pokedex > exit
wagslane@MacBook-Pro-4 src %
```

Keep in mind that `Pokedex >` is a command line prompt. The program waited for me at that point to type in `help` and press enter, then `exit` and press enter.
