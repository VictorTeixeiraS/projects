package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"github.com/bootdotdev/courses/projects/pokedexcli/internal/pokeapi"
)

const exitCommandSlug = "exit"

type config struct {
	pokeapiClient pokeapi.Client
	nextListURL   *string
	prevListURL   *string
}

func startRepl(cfg *config) {
	reader := bufio.NewScanner(os.Stdin)
	printPrompt()
	for reader.Scan() {
		text := cleanInput(reader.Text())
		if command, exists := getCommands()[text]; exists {
			err := command.callback(cfg)
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
	fmt.Print("Pokedex > ")
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
	callback    func(*config) error
}

func getCommands() map[string]cliCommand {
	return map[string]cliCommand{
		"help": {
			name:        "help",
			description: "Displays a help message",
			callback:    commandHelp,
		},
		"list": {
			name:        "list",
			description: "List the next batch of Pokemon",
			callback:    commandList,
		},
		"listprev": {
			name:        "listprev",
			description: "List the last batch of pokemon",
			callback:    commandListPrev,
		},
		"exit": {
			name:        "exit",
			description: "Exit the Pokedex",
			callback:    commandExit,
		},
	}
}
