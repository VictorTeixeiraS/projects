package pokeapi

// RespListPokemon -
type RespListPokemon struct {
	Count    int       `json:"count"`
	Next     *string   `json:"next"`
	Previous *string   `json:"previous"`
	Results  []Pokemon `json:"results"`
}

// Pokemon -
type Pokemon struct {
	Name string `json:"name"`
	URL  string `json:"url"`
}
