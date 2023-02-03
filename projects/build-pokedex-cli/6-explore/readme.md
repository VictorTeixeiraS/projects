# Explore

After using the `map` commands, we want our users to be able to see a list of all the Pokémon in a given area.

Add the `explore` command. It takes the name of a location area as an argument.

## Tips

* Use the same [PokeAPI location-area endpoint](https://pokeapi.co/docs/v2#location-areas), but this time you'll need to pass the `name` of the location area being explored. By adding an `id`, the API will return *a lot* more information about the location area.
* Feel free to use tools like JSON lint and JSON to Go to help you parse the response.
* Parse the Pokemon's names from the response and display them to the user.
* Make sure to use the caching layer again! Re-exploring an area should be blazingly fast.
* You'll need to alter the function signature of *all* your commands to allow them to allow parameters. E.g. `explore <area_name>`

## Example usage

```bash
Pokedex > explore pastoria-city-area
Exploring pastoria-city-area...
Found Pokemon: 
 - tentacool
 - tentacruel
 - magikarp
 - gyarados
 - remoraid
 - octillery
 - wingull
 - pelipper
 - shellos
 - gastrodon
Pokedex > 
```
