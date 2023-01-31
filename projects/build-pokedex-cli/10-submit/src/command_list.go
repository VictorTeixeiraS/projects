package main

import "fmt"

func commandList(cfg *config) error {
	pokemon, nextList, prevList, err := cfg.pokeapiClient.ListPokemon(cfg.nextListURL)
	if err != nil {
		return err
	}

	cfg.nextListURL = nextList
	cfg.prevListURL = prevList

	for _, p := range pokemon {
		fmt.Println(p.Name)
	}
	return nil
}
