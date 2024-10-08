# dpDCABot.mq5

`dpDCABot.mq5` is a highly flexible MetaTrader 5 Expert Advisor (EA) that supports multiple trading strategies such as VWAP-based trading, DCA (Dollar Cost Averaging), and martingale. This guide explains the configuration and use of the parameters for various strategies, including VWAP, DCA, and manual trading.

## Features

- **VWAP-Based Trading**
- **Dollar Cost Averaging (DCA) Strategy**
- **Martingale Strategy**
- **Manual Trading with Hotkey Support**
- **Take Profit and Stop Loss Management**
- **Periodic Profit Withdrawal**

---

## Parameters and Configuration

### EA Properties

| Parameter                    | Description                                                                                                                                                                  | Default Value |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ------------- |
| `eaBotMode`                   | Defines the trading strategy: `VWAP`, `DCA`, `MANUAL`, etc.                                                                                                                  | `VWAP`        |
| `vlIncreaseType`              | Volume increase strategy: `STEPS`, `MTC`, `X2`, etc.                                                                                                                         | `STEPS`       |
| `eaVolume`                    | Initial trade volume for the first position.                                                                                                                                  | `0.01`        |
| `maxAllowedVolume`            | Maximum allowed trade volume for each position.                                                                                                                              | `10`          |
| `maxPositions`                | Maximum number of positions the EA can open.                                                                                                                                  | `20`          |
| `exitPosition`                | The position number where the EA will start executing the exit strategy.                                                                                                     | `11`          |
| `exitPositionPercentage`      | Target profit/loss percentage when exiting DCA positions. Positive values target profit, negative values reduce losses.                                                       | `0.2`         |
| `recalculateExitVolume`       | If true, recalculates volume for exit trades to recover losses and meet the `exitPositionPercentage`.                                                                         | `false`       |
| `eaTP`                        | Take profit in points.                                                                                                                                                       | `500`         |
| `eaSTL`                       | Stop loss in points.                                                                                                                                                         | `500`         |
| `distanceInPoints`            | Minimum price movement in points required before opening the next DCA position.                                                                                              | `50`          |
| `eaComments`                  | Comment added to the trade for identification.                                                                                                                               | `"bb-dca-bot"`|

### VWAP Properties

| Parameter                     | Description                                                                                                                                                                  | Default Value |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ------------- |
| `enableVwap`                   | Enables VWAP-based trading. If true, the EA uses VWAP for trend determination.                                                                                               | `false`       |
| `InputStdDevMultiplier1...5`   | Standard deviation multipliers for VWAP bands (controls how far the upper and lower VWAP bands extend from the VWAP mean).                                                   | `2.5`, `3.0`  |
| `vwapTimeFrame`                | Timeframe used for calculating VWAP.                                                                                                                                        | `PERIOD_CURRENT` |
| `vwapSession`                  | Enables session-based VWAP calculation, defining start/end times for VWAP calculation.                                                                                       | `true`        |
| `vwapPeriod`                   | Period used for VWAP calculation. If set to 0, the EA will use daily VWAP.                                                                                                   | `50`          |
| `vwapExpandPoints`             | Points to expand the VWAP bands in `VWAPEXPANDED` mode.                                                                                                                     | `600`         |

### DCA Properties

| Parameter                     | Description                                                                                                                                                                  | Default Value |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ------------- |
| `isBuy`                        | Whether to open Buy positions. Useful for manual or semi-automated strategies.                                                                                               | `false`       |
| `isSell`                       | Whether to open Sell positions. Useful for manual or semi-automated strategies.                                                                                              | `false`       |
| `mtcVolumeSteps`               | Volume multipliers for DCA positions, e.g., `"1-9:1.5,10-20:2"` (positions 1-9 have a volume multiplier of 1.5, and 10-20 have 2).                                           | `"1-9:1.5,10-20:2"` |
| `mtcRangeTP`                   | Take profit ranges for DCA positions, e.g., `"1-9:400,10-20:100"` (positions 1-9 have a take profit of 400 points, and 10-20 have 100).                                       | `"1-9:400,10-20:100"` |
| `distanceInPoints`             | Minimum price movement in points required before opening the next DCA position.                                                                                              | `50`          |

### Withdrawal Properties

| Parameter                     | Description                                                                                                                                                                  | Default Value |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ------------- |
| `withDrawalEnable`             | Enables periodic withdrawals during backtests.                                                                                                                               | `true`        |
| `withDrawalSize`               | Percentage of profit to withdraw.                                                                                                                                           | `100`         |
| `withDrawalFrequency`          | Frequency of withdrawals: `DAILY`, `WEEKLY`, or `MONTHLY`.                                                                                                                  | `DAILY`       |

### Time-Based Filters

| Parameter                     | Description                                                                                                                                                                  | Default Value |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ------------- |
| `isTimeFilter`                 | Enables trading based on time.                                                                                                                                               | `true`        |
| `eaStartTime`                  | Start time (hour) for trading.                                                                                                                                               | `7`           |
| `eaEndTime`                    | End time (hour) for trading.                                                                                                                                                 | `17`          |
| `isStartOnlyNewSession`        | If true, opens trades only when a new session starts.                                                                                                                        | `true`        |

### Manual and Hotkey Controls

| Hotkey                        | Action                                                                                                                                                                       |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `KEY_B`                        | Manually opens a Buy position.                                                                                                                                               |
| `KEY_S`                        | Manually opens a Sell position.                                                                                                                                              |
| `KEY_H`                        | Opens both Buy and Sell (hedge) positions manually.                                                                                                                          |
| `KEY_C`                        | Closes all open positions.                                                                                                                                                   |

### Exit Strategies

| Parameter                     | Description                                                                                                                                                                  | Default Value |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ------------- |
| `dcaExitMode`                  | Exit strategy for DCA positions: `RANGE`, `NUMBER_POSITION`, `TIME`.                                                                                                         | `NUMBER_POSITION` |

---

## How to Configure the EA for Different Use Cases

### 1. **VWAP-Based Strategy**

1. Set `eaBotMode = VWAP`.
2. Enable VWAP properties (`enableVwap = true`).
3. Configure `InputStdDevMultiplier1...5` and `vwapTimeFrame`.
4. Set `distanceInPoints` to define how far the price must move before adding new positions.

### 2. **DCA (Dollar Cost Averaging) Strategy**

1. Set `eaBotMode = DCA`.
2. Adjust `mtcVolumeSteps`, `mtcRangeTP`, and `distanceInPoints` to control position entries.
3. Set `exitPosition` and `exitPositionPercentage` to define the exit conditions.

### 3. **Martingale Strategy**

1. Set `vlIncreaseType = X2` to double the volume for each subsequent trade.
2. Adjust `eaVolumeX` to control the multiplier factor for volume growth.

### 4. **Manual Trading**

1. Set `eaBotMode = MANUAL`.
2. Use the hotkeys to open and manage trades manually during specific market conditions.

---

## Closing Notes

`dpDCABot.mq5` is designed to handle various trading strategies and offers great flexibility in configuration. The EA can be customized to handle everything from VWAP-based trading to advanced DCA and Martingale strategies. 

Before using the EA in live markets, ensure to thoroughly backtest and demo trade it to understand how the different parameters interact.

Always use appropriate risk management when deploying in a live account.

