# rsi_reversion — example rule-based package

Buys when RSI(14) < 30, sells when RSI > 70, goes flat when RSI crosses back to 50. GBP/USD (first) and AUD/USD, 15-minute bars.

```
pytest tests
qos install .
```

Default parameters are the textbook 14 / 30 / 70. On the 90 days to 27 Oct 2026 (GBP/USD 15m, 20,000 units) the backtest
made about +350 USD with a small drawdown, so it reaches `backtested` — that is one period, not proof of an edge;
walk-forward and the paper soak are the real tests.
