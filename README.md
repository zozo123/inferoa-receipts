# inferoa-receipts

A tiny auth service with a **genuinely failing test** — the receipts repo for the
[Inferoa inference demo](https://zozo123.github.io/inferoa-demo/).

The interactive demo simulates an agent fixing `test_token_refresh`. This repo is the
real version of that scenario: the test fails because `token.py` issues tz-naive
expiry timestamps while `middleware.py` compares against tz-aware `datetime.now(timezone.utc)`.

```
pytest
# TypeError: can't compare offset-naive and offset-aware datetimes
```

A real agent, running in an isolated [islo.dev](https://islo.dev) sandbox, was given one task:
make the tests pass and open a PR. The PR on this repo **is the receipt** — diff, test output,
and transcript artifacts included.
