# Implement a Transactional Key-Value Store

**Company:** Applied Intuition
**Difficulty:** Medium

## Problem

Implement an in-memory key-value store that supports basic read/write operations and transactions. You should design and implement an external API so that changes made inside a transaction are buffered and either become visible atomically upon commit or are discarded upon rollback.

## Required Operations

- `GET key` — return the currently visible value for key; if it does not exist, return `NULL`.
- `SET key value` — set key to value.
- `DELETE key` — delete key (no-op if absent).
- `BEGIN` — start a new transaction.
- `COMMIT` — commit the current transaction, making all its changes visible.
- `ROLLBACK` — rollback the current transaction, discarding all its changes.

## Transaction Semantics

- **Read-your-writes:** within the same transaction, a GET after SET must see the new value.
- After `COMMIT`, changes must be visible to subsequent operations.
- After `ROLLBACK`, changes must have no effect.
- When no transaction is active, `SET`/`DELETE` apply directly to global state.
- If `COMMIT`/`ROLLBACK` is called with no active transaction: output `NO TRANSACTION`.

## I/O Format

Read commands line by line from stdin until EOF. Output one line per `GET`. For invalid `COMMIT`/`ROLLBACK`, output `NO TRANSACTION`.

## Examples

**Input:**
```
SET a 1
GET a
```

**Output:**
```
1
```

## Constraints

- Number of commands `N <= 2 * 10^5`
- `key` and `value` are strings without spaces, length `<= 64`
