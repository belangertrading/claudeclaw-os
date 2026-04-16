# Trade-Alert API — Complete Command Reference

## Trade Recaps
| Command | Description |
|---------|-------------|
| `Top` | Top trades + sweeps by size, with market side |
| `Trades` | Top trades only (no sweeps) |
| `Sweep` | Top sweeps and split tickets |
| `Impact` | Top trades by delta impact |
| `Vtop` | Top trades by $vega |
| `Gtop` | Top trades by gamma |
| `Premium` | Top trades by premium |
| `Notional` | Top trades by notional value |
| `Recent` | Most recent trades (single underlying/option only) |
| `Cancel` | Most recent cancels |
| `Blocks` | Top underlying block trades |

### Per-Exchange Trade Filters
`Amex`, `Arca`, `Box`, `Bxo`, `Bzx`, `C2`, `Cboe`, `Edgx`, `Emld`, `Gem`, `Ise`, `Merc`, `Miax`, `Mprl`, `Nom`, `Phlx`, `Memx`, `Sphr`

Field glossaries: Trade Fields, Option Fields, Underlying Fields

## Spread Recaps
| Command | Description |
|---------|-------------|
| `Spread` | All identified spread trades |
| `OtherSpread` | Other/unclassified spread trades |
| `Combo` | Combo trades |
| `RiskReversal` | Risk reversal trades |
| `Vertical` | Vertical spreads |
| `TimeSpread` | Calendar/time spreads |
| `Diagonal` | Diagonal spreads |
| `Straddle` | Straddle trades |
| `Strangle` | Strangle trades |
| `GutStrangle` | Gut strangle trades |
| `RatioSpread` | Ratio spread trades |
| `RatioRiskReversal` | Ratio risk reversal trades |
| `Butterfly` | Butterfly trades |
| `TimeButterfly` | Calendar butterfly trades |
| `PutCollar` | Put collar trades |
| `CallCollar` | Call collar trades |
| `PutRatioCollar` | Put ratio collar trades |
| `CallRatioCollar` | Call ratio collar trades |
| `Condor` | Condor trades |
| `IronCondor` | Iron condor trades |
| `JellyRoll` | Jelly roll trades |
| `StraddleSwap` | Straddle swap trades |
| `StrangleSwap` | Strangle swap trades |
| `IronButterfly` | Iron butterfly trades |
| `BoxSpread` | Box spread trades |
| `TiedOutright` | Tied outright trades |
| `TiedSpread` | Tied spread trades |
| `RevCon` | Reversal/conversion trades |

## Security Analysis (Option-Level)
| Command | Description |
|---------|-------------|
| `Moso` | Most active options |
| `OI` | Options with most open interest |
| `OIChg` | Top changes in open interest |
| `OIUp` | Top increases in open interest |
| `OIDown` | Top decreases in open interest |
| `StrikeOi` | Total OI by strike |

## Market Analysis (Underlying-Level)
| Command | Description |
|---------|-------------|
| `Most` | Most active underlyings |
| `Bullish` | Unusual call volume ranked by %ask |
| `Bearish` | Unusual put volume ranked by %bid |
| `Uvol` | Unusual total option volume |
| `Wuvol` | Time-weighted unusual option volume |
| `Movers` | Largest underlying price changes |
| `Gainers` | Largest price increases |
| `Losers` | Largest price decreases |
| `Richest` | Richest ATM IV vs 30-day historical vol |
| `Cheapest` | Cheapest ATM IV vs 30-day historical vol |
| `High` | 52-week price highs |
| `Low` | 52-week price lows |
| `IvHigh` | 52-week ATM IV highs |
| `IvLow` | 52-week ATM IV lows |
| `OiTurn` | Largest OI turnover |
| `TotOi` | Top total open interest |
| `TotOiChg` | Top total OI changes |
| `TotOiUp` | Top total OI increases |
| `TotOiDown` | Top total OI decreases |
| `PutCall` | Put/call sentiment detail |
| `CallPut` | Call/put sentiment detail |
| `Volume` | Option volume breakdown |
| `VTB` | Volume type breakdown |

## IV Analysis
| Command | Description |
|---------|-------------|
| `IVGap` | Largest implied volatility changes |
| `IVUp` | Largest IV increases |
| `IVDown` | Largest IV decreases |

### Tenor-Specific IV Commands
Format: `IV{tenor}{direction}` where tenor = 30/60/90/120/180/360/720 and direction = Gap/Up/Down

Examples: `IV30Gap`, `IV30Up`, `IV30Down`, `IV60Gap`, `IV90Up`, `IV720Down`, etc.

| Command | Description |
|---------|-------------|
| `Steep` | Highest percentile 30d 25-delta put/call IV skew |
| `Flat` | Lowest percentile 30d 25-delta put/call IV skew |
| `Steepen` | Greatest increase in normalized 30d 25-delta skew |
| `Flatten` | Greatest decrease in normalized 30d 25-delta skew |

## 13F / Institutional
| Command | Description |
|---------|-------------|
| `13F` | Option holders for a ticker from most recent 13F filings |
| `13FNew` | Filers who reported option holdings this quarter but not prior |
| `13FDead` | Filers who reported last quarter but not this quarter |
| `Holdings` | All 13F option holdings for a specific filer (matches partial name) |

## Notes / Commentary
| Command | Description |
|---------|-------------|
| `Color` | Market color and commentary |
| `News` | News headlines |
| `New` | Newest system features |

## Other
| Command | Description |
|---------|-------------|
| `Futures` | Futures activity |
| `Flow` | Bucketed trade flow |
| `Bucket` | Strike-bucketed statistics for volume and OI |
| `Range` | Historical 52-week range data |
| `Cal` | Event calendar |
| `Expiries` | Upcoming expiration dates for ticker/group |
| `Pin` | Near-term options closest to spot (max gamma) |
| `Edge` | Cboe options edge data |
| `Flex` | Flex option open interest |
| `FlexNew` | New flex option open interest |
| `Hashtags` | List of note hashtags in use |
| `Events` | Recent events (halts, SSR, 52wk highs/lows, earnings) |
| `Borrow` | Borrow rate indication |
| `BGap` | Largest change in indicative borrow rate |
| `BUp` | Largest increase in borrow rate |
| `BDown` | Largest decrease in borrow rate |
| `EGap` | Implied earnings event deviation |
| `EventVol` | Implied event deviation |
| `Sector` | Sector activity |
| `SubSector` | Subsector activity |

## Meta Commands
| Command | Description |
|---------|-------------|
| `GetApiDoc` | Returns API documentation (output=html) |
