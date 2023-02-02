# Caching

It's time to implement caching! This will make moving around the map feel a lot snappier. We'll be building a flexible caching system so that it will also help with performance in future steps.

## What is a cache?

A [cache](https://en.wikipedia.org/wiki/Cache_(computing)) temporarily stores data so that future requests for that data can be served faster.

In our case, we'll be caching responses from the PokeAPI so that when we need that same data again, we can grab it from memory instead of making another network request.

## The pokecache package

Create a new internal package called `pokecache` in your `internal` directory. This package will be responsible for all of our caching logic.

Your cache should be a `map[string][cacheEntry]`. A `cacheEntry` should be a struct with two fields:

* `createdAt` - A [time.Time](https://pkg.go.dev/time#Time) that represents when the entry was created.
* `val` - A `[]byte` that represents the raw data we're caching.

You'll probably want to expose a `NewCache()` function that creates a new cache with a configurable `interval` ([time.Duration](https://pkg.go.dev/time#Duration)).

You'll want the following *methods* on the `cache`:

### .Add()

Adds a new entry to the cache. It should take a `key` (a `string`) and a `val` (a `[]byte`).

### .Get()

Gets an entry from the cache. It should take a `key` (a `string`) and return a `[]byte` and a `bool`. The `bool` should be `true` if the entry was found and `false` if it wasn't.

### .reapLoop()

This method should be called when the cache is created (by the `NewCache` function). Each time an `interval` (the `time.Duration` passed to `NewCache`) passes it should remove any entries that are older than the `interval`. This makes sure that the cache doesn't grow too large over time. For example, if the interval is 5 seconds, and an entry was added 7 seconds ago, that entry should be removed.

## Using the cache

Update your code that makes requests to the PokeAPI to use the cache. If you already have the data for a given URL (which is our cache key) in the cache, you should use that instead of making a new request.
Whenever you do make a request, you should add the response to the cache.

## How do I know it's working?

When you use the `map` command to get data for the first time there should be a noticeable waiting time. However, when you use `mapb` it should be instantaneous because the data for that page is already in the cache. Feel free to add some logging that informs you in the command line when the cache is being used.

## Writing tests

Write some [tests](https://go.dev/doc/tutorial/add-a-test) for your cache package! This example code should give you an idea of how to get started, but feel free to add a few more cases.

You can run tests for all packages in a Go module by running `go test ./...` from the root of the module.

```go
func TestAddGet(t *testing.T) {
	const interval = 5 * time.Second
	cases := []struct {
		key string
		val []byte
	}{
		{
			key: "https://example.com",
			val: []byte("testdata"),
		},
		{
			key: "https://example.com/path",
			val: []byte("moretestdata"),
		},
	}

	for i, c := range cases {
		t.Run(fmt.Sprintf("Test case %v", i), func(t *testing.T) {
			cache := NewCache(interval)
			cache.Add(c.key, c.val)
			val, ok := cache.Get(c.key)
			if !ok {
				t.Errorf("expected to find key")
				return
			}
			if string(val) != string(c.val) {
				t.Errorf("expected to find value")
				return
			}
		})
	}
}

func TestReapLoop(t *testing.T) {
	const baseTime = 5 * time.Millisecond
	const waitTime = baseTime + 5*time.Millisecond
	cache := NewCache(baseTime)
	cache.Add("https://example.com", []byte("testdata"))

	_, ok := cache.Get("https://example.com")
	if !ok {
		t.Errorf("expected to find key")
		return
	}

	time.Sleep(waitTime)

	_, ok = cache.Get("https://example.com")
	if ok {
		t.Errorf("expected to not find key")
		return
	}
}
```
