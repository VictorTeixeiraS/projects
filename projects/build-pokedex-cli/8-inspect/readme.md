# Inspect

Just like in the Pokemon game, our Pokedex will only allow players to see details about a Pokemon if they have seen it before (or in our case, caught it)

Add the `inspect` command. It takes the name of a Pokemon as an argument. It should print the name, height, weight, stats and type(s) of the Pokemon. You shouldn't need to make an API call to get this information, since you should have already stored it when the user caught the Pokemon.

If the user has not caught the Pokemon, just print a message saying so.

## Example usage

```bash
Pokedex > inspect pidgey
you have not caught that pokemon
Pokedex > catch pidgey
Throwing a Pokeball at pidgey...
pidgey was caught!
Pokedex > inspect pidgey
Name: pidgey
Height: 3
Weight: 18
Stats:
  -hp: 40
  -attack: 45
  -defense: 40
  -special-attack: 35
  -special-defense: 35
  -speed: 56
Types:
  - normal
  - flying
```
