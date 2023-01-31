package main

import (
	"errors"
	"fmt"
)

func commandListPrev(cfg *config) error {
	if cfg.prevListURL == nil {
		return errors.New("you're on the first page")
	}

	pokemon, nextList, prevList, err := cfg.pokeapiClient.ListPokemon(cfg.prevListURL)
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
