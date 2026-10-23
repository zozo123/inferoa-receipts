# inferoa-receipts

A tiny Python auth service with a real failing test and the agent-written fix: the
evidence repo behind the [Inferoa inference demo](https://zozo123.github.io/inferoa-demo/).
Status: complete; the fix is merged on `main`.

The interactive demo simulates an agent fixing `test_token_refresh`. This repo is the
real run of that scenario.

## The failure

The repo started with a real failing test: `token.py` issued tz-naive expiry timestamps
while `middleware.py` compared them with tz-aware `datetime.now(timezone.utc)`. To see the
failure, check out the first commit and run the tests:

```
git checkout e4d7630 && pytest
# TypeError: can't compare offset-naive and offset-aware datetimes
```

On `main` the fix from PR #1 is merged and both tests pass.

## The receipt

The receipt is [PR #1](https://github.com/zozo123/inferoa-receipts/pull/1): diagnosis,
failing and passing pytest output, and a one-file diff to `auth_service/token.py`. It ran
in an isolated [islo.dev](https://islo.dev) sandbox and was made with
[Cursor](https://cursor.com). The task prompt named the suspected cause, so this shows the
sandboxed fix-verify-publish loop, not unguided diagnosis.
