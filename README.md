# QOS strategy examples

Example strategies written with the QOS developer kit. Copy one as a starting point for your
own.

| Folder | Strategy |
|---|---|
| `rsi_reversion/` | RSI mean-reversion with tests |

## Before you start

You need Python 3.12+ and the `qos` command from the QOS developer kit (no broker account needed):

```bash
git clone https://github.com/qos-one/qos-examples.git && cd qos-examples
pip install "qos-sdk[test] @ git+https://github.com/qos-one/qos.git@v0.1.6#subdirectory=qos_sdk"
```

## Try an example

Each example has a `strategy.py`, a README and tests:

```bash
pytest rsi_reversion/tests                   # unit tests on generated bars
qos install rsi_reversion                    # install checks, then install into your local QOS
python -m qos.publish_check rsi_reversion --scan-only   # the Store's static code scan
```

Without a data catalog, `qos install` runs its checks (import, manifest, network, determinism,
lookahead) on generated bars. Any P&L figure it prints comes from those generated bars and says
nothing about real markets. If no QOS server is running, it installs the package and tells you to
run `qos evaluate` later.

The full `python -m qos.publish_check rsi_reversion` (without `--scan-only`) also runs a 90-day
backtest and a walk-forward, so it needs a data catalog with recent GBP/USD or AUD/USD bars
(`--catalog DIR`). See "Market data" in the [QOS README](https://github.com/qos-one/qos#readme)
for how to build one.

For a machine-learning starting point, use the SDK template: `qos new my_model --ml` (needs the
`ml` extra: install `qos-sdk[test,ml]` instead of `qos-sdk[test]`).

These examples are for learning. They are not investment advice, and backtest results do not
predict future returns.

## License

Apache-2.0 — see [LICENSE](LICENSE). You may use these examples in your own strategies under
any license.
