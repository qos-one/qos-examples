# QOS strategy examples

Example strategies written with the QOS developer kit. Copy one as a starting point for your
own.

| Folder | Strategy |
|---|---|
| `rsi_reversion/` | RSI mean-reversion with tests |

Each example has a `strategy.py`, a README and tests:

```bash
python -m qos.publish_check rsi_reversion    # the same checks the Store runs
qos install rsi_reversion                    # install into your local QOS
```

For a machine-learning starting point, use the SDK template: `qos new my_model --ml`.

These examples are for learning. They are not investment advice, and backtest results do not
predict future returns.

## License

Apache-2.0 — see [LICENSE](LICENSE). You may use these examples in your own strategies under
any license.
