package pokeapi

import (
	"encoding/json"
	"io"
	"net/http"
)

// ListPokemon -
func (c *Client) ListPokemon(nextURL *string) ([]Pokemon, *string, error) {
	url := baseURL + "/pokemon"
	if nextURL != nil {
		url = *nextURL
	}

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return nil, nil, err
	}

	resp, err := c.httpClient.Do(req)
	if err != nil {
		return nil, nil, err
	}
	defer resp.Body.Close()

	dat, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, nil, err
	}

	pokemonResp := RespListPokemon{}
	err = json.Unmarshal(dat, &pokemonResp)
	if err != nil {
		return nil, nil, err
	}

	return pokemonResp.Results, pokemonResp.Next, nil
}
