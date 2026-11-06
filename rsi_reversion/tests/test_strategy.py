import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from qos.sdk import quick_backtest, validate  # noqa: E402
from qos.sdk.testing import synthetic_bars  # noqa: E402
from strategy import RsiReversion  # noqa: E402

BARS = synthetic_bars("GBP/USD.IDEALPRO", 15, n=3000, period=40)


def test_manifest_is_valid():
    assert validate(RsiReversion) == []


def test_trades_and_exits():
    r = quick_backtest(RsiReversion, bars=BARS)
    assert r["closed_positions"] > 0 and 0 in [v for _, v in r["actions"]]


def test_same_decisions_every_run():
    assert quick_backtest(RsiReversion, bars=BARS)["actions"] == quick_backtest(RsiReversion, bars=BARS)["actions"]


def test_rejects_bad_levels():
    with pytest.raises(ValueError):
        quick_backtest(RsiReversion, {"period": 1}, bars=BARS)
