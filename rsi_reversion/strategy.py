"""RSI Reversion — buy when RSI is oversold, sell when overbought, exit when RSI returns to 50"""
from qos.sdk import Param, Strategy


class RsiReversion(Strategy):
    name = "rsi_reversion"
    label = "RSI Reversion"
    version = "1.0.0"
    instruments = ["GBP/USD", "AUD/USD"]
    timeframe = "15m"
    summary = "RSI {period} {low}/{high}"

    period = Param(14, min=2, max=100, grid=[7, 14], help="RSI period (bars)")
    low = Param(30, min=5, max=49, grid=[25, 30], help="oversold level → long")
    high = Param(70, min=51, max=95, grid=[70, 75], help="overbought level → short")

    def on_configure(self):
        if self.p.low >= self.p.high:
            raise ValueError("low must be below high")

    def on_start(self):
        self.rsi = self.indicator("rsi", self.p.period)

    def on_bar(self, bar):
        if not self.ready():
            return
        rsi = self.rsi.value * 100                     # Nautilus RSI is 0–1
        pos = self.position()
        if rsi < self.p.low:
            self.target(+1)
        elif rsi > self.p.high:
            self.target(-1)
        elif (pos > 0 and rsi >= 50) or (pos < 0 and rsi <= 50):
            self.target(0)
