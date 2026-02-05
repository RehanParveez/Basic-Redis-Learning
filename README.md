# Django Redis Cache Demo

## What is this about
It's about to understand the Redis properly instead of just copy pasting code.
So before moving to Celery or DRF caching, I decided to build a very small
project only focused on Redis as a cache backend.

=====

## Main Points

### Redis is not Django
Redis is a separate service running in background.
In my case Redis is running inside Docker, and Django is just connecting to it.

Django does not store cache by itself.
It sends data to Redis and Redis stores it in memory.

=====

## What this project does

- There is a single view `/redis-time/`
- When we hit this endpoint:
  - Django first checks Redis
  - Then ff Redis has data → returns instantly
  - If not -> Django does slow work and then stores result in Redis

=====

## How cache logic works in code

- `cache.get("current_time")`
  checks if Redis already has this key

- If key exists:
  response comes from Redis (fast)

- If key does not exist:
  Django computes the value
  then stores it using `cache.set()`

- I set timeout to 14 seconds so Redis auto deletes it

=====

## How it should be tested

1. First refresh
   - Takes 3 seconds
   - Data comes from computation

2. Refresh again
   - Instant
   - Data comes from Redis

3. Wait 20 seconds
   - Cache expires
   - Django recomputes data again

=====

## Why Redis is beneficial?

Redis helps reduce:
- repeated computation
- repeated database hits
- response time

This is especially important for:
- APIs
- dashboards
- read-heavy endpoints

=====


