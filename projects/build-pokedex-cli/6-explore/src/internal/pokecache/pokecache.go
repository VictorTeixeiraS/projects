package pokecache

import (
	"time"
)

// Cache -
type Cache struct {
	cache map[string]cacheEntry
}

type cacheEntry struct {
	createdAt time.Time
	val       []byte
}

// NewCache -
func NewCache(interval time.Duration) Cache {
	c := Cache{
		cache: make(map[string]cacheEntry),
	}

	go c.reapLoop(interval)

	return c
}

// Add -
func (c *Cache) Add(key string, value []byte) {
	c.cache[key] = cacheEntry{
		createdAt: time.Now(),
		val:       value,
	}
}

// Get -
func (c *Cache) Get(key string) ([]byte, bool) {
	val, ok := c.cache[key]
	return val.val, ok
}

func (c *Cache) reapLoop(interval time.Duration) {
	ticker := time.NewTicker(interval)
	for range ticker.C {
		c.reap(time.Now().UTC(), interval)
	}
}

func (c *Cache) reap(now time.Time, last time.Duration) {
	for k, v := range c.cache {
		if v.createdAt.Before(now.Add(-last)) {
			delete(c.cache, k)
		}
	}
}
