package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const exitCommandSlug = "exit"

func startRepl() {
	reader := bufio.NewScanner(os.Stdin)
	printPrompt()
	for reader.Scan() {
		text := cleanInput(reader.Text())
		if command, exists := getCommands()[text]; exists {
			err := command.callback()
			if err != nil {
				fmt.Println(err)
			}
		} else {
			printUnknown(text)
		}

		printPrompt()
	}
}

func printPrompt() {
	fmt.Print(" Pokedex > ")
}

func printUnknown(text string) {
	fmt.Println(text, ": command not found")
}

func cleanInput(text string) string {
	output := strings.TrimSpace(text)
	output = strings.ToLower(output)
	return output
}

type cliCommand struct {
	name        string
	description string
	callback    func() error
}

func getCommands() map[string]cliCommand {
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
}
