# Catch

It's time to catch some pokemon! Catching Pokemon adds them to the user's Pokedex.

Add the `catch` command. It takes the name of a Pokemon as an argument.

## Tips

* Use the [Pokemon endpoint](https://pokeapi.co/docs/v2#pokemon) to get information about a Pokemon by name.
* Give the user a *chance* to catch the Pokemon using the [math/rand package](https://pkg.go.dev/math/rand#Rand.Intn).
* You can use the pokemon's "base experience" to determine the chance of catching it. The higher the base experience, the harder it should be to catch.
* Once the Pokemon is caught, add it to the user's Pokedex. I used a `map[string]Pokemon` to keep track of caught Pokemon.
* You'll want to store the Pokemon's *data* so that in the next step we can use it.

## Example usage

```bash
Pokedex > catch pikachu
Throwing a Pokeball at pikachu...
pikachu escaped!
Pokedex > catch pikachu
Throwing a Pokeball at pikachu...
pikachu was caught!
```
