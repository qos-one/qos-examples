# Contributing to QOS examples

Thanks for helping. This repository holds small, readable strategies that people copy as a
starting point. Clear code and honest READMEs matter more here than clever strategies.

## Questions, setup reports and bugs

- **Got stuck, or it worked?** Open an [issue in qos-one/qos](https://github.com/qos-one/qos/issues/new)
  titled "Setup report": your OS, Python version, the command you ran and its last lines of output.
  That is the most useful feedback we get.
- **A bug in an example here:** open an issue in this repository with the command and the output.
- **Security problems:** do not open an issue; see [SECURITY.md](SECURITY.md).

## Adding an example

Copy the layout of `rsi_reversion/`:

```
my_example/
  strategy.py        # one Strategy subclass with a unique `name`
  README.md          # what it does, markets and bar size, how to run it
  tests/test_strategy.py
```

Before you open a pull request, from the repository root:

```bash
pytest my_example/tests
python -m qos.publish_check my_example --scan-only
```

Both must pass. Then add one row for your folder to the table in [README.md](README.md).

### README rules for examples

- Say what the rules do in plain words, plus the markets and bar size.
- No performance claims: no returns, win rates, P&L figures or "profitable". A backtest shows how
  rules behaved on past data, not that they have an edge.
- No promises of automated income and no investment advice.

## Sign your work (DCO)

Like the main QOS repository, we use the [Developer Certificate of Origin](https://developercertificate.org/).
Sign every commit:

```bash
git commit -s -m "Add my_example"
```

Pull requests without a sign-off cannot be merged. By contributing you agree that your example is
released under this repository's Apache-2.0 [LICENSE](LICENSE).
