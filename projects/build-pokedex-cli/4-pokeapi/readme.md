# PokeAPI

Now we're going to start using the [PokeAPI](https://pokeapi.co/) to get some data from the Pokemon world!

Add 2 new commands: `map` and `mapb`.

### map

The `map` command displays the names of 20 location areas in the Pokemon world. Each subsequent call to `map` should display the next 20 locations, and so on. The idea is that the `map` command will let us explore the world of Pokemon.

### mapb (map back)

Similar to the `map` command, but instead of displaying the next 20 locations, it displays the previous 20 locations. It's a way to go back.

If you're on the first "page" of results, this command should just print an error message.

## Tips for this step

* You'll need to use the [PokeAPI location-area endpoint](https://pokeapi.co/docs/v2#location-areas) to get the location areas.
* Your commands should now accept a pointer to a "config" struct as a parameter. This struct will contain the `Next` and `Previous` URLs that you'll need to paginate through location areas.
* [JSON lint](https://jsonlint.com/) is a useful tool for debugging JSON, it makes it easier to read.
* [JSON to Go](https://mholt.github.io/json-to-go/) a useful tool for converting JSON to Go structs. You can use it to generate the structs you'll need to parse the PokeAPI response.
* [Here's an example](https://pkg.go.dev/net/http#example-Get) of how to make a GET request in Go.
* [Here's how to unmarshal](https://blog.boot.dev/golang/json-golang/#example-unmarshal-json-to-struct-decode) a slice of bytes into a Go struct.
* I recommend creating an [internal package](https://dave.cheney.net/2019/10/06/use-internal-packages-to-reduce-your-public-api-surface) that manages your PokeAPI interactions. It's not required, but it's a good organizational and architectural pattern.
* You can make GET requests in your browser! It's convenient for testing and debugging.

## Example usage

```bash
Pokedex > map
canalave-city-area
eterna-city-area
pastoria-city-area
sunyshore-city-area
sinnoh-pokemon-league-area
oreburgh-mine-1f
oreburgh-mine-b1f
valley-windworks-area
eterna-forest-area
fuego-ironworks-area
mt-coronet-1f-route-207
mt-coronet-2f
mt-coronet-3f
mt-coronet-exterior-snowfall
mt-coronet-exterior-blizzard
mt-coronet-4f
mt-coronet-4f-small-room
mt-coronet-5f
mt-coronet-6f
mt-coronet-1f-from-exterior
Pokedex > map
mt-coronet-1f-route-216
mt-coronet-1f-route-211
mt-coronet-b1f
great-marsh-area-1
great-marsh-area-2
great-marsh-area-3
great-marsh-area-4
great-marsh-area-5
great-marsh-area-6
solaceon-ruins-2f
solaceon-ruins-1f
solaceon-ruins-b1f-a
solaceon-ruins-b1f-b
solaceon-ruins-b1f-c
solaceon-ruins-b2f-a
solaceon-ruins-b2f-b
solaceon-ruins-b2f-c
solaceon-ruins-b3f-a
solaceon-ruins-b3f-b
solaceon-ruins-b3f-c
Pokedex > mapb
canalave-city-area
eterna-city-area
pastoria-city-area
sunyshore-city-area
sinnoh-pokemon-league-area
oreburgh-mine-1f
oreburgh-mine-b1f
valley-windworks-area
eterna-forest-area
fuego-ironworks-area
mt-coronet-1f-route-207
mt-coronet-2f
mt-coronet-3f
mt-coronet-exterior-snowfall
mt-coronet-exterior-blizzard
mt-coronet-4f
mt-coronet-4f-small-room
mt-coronet-5f
mt-coronet-6f
mt-coronet-1f-from-exterior
```
