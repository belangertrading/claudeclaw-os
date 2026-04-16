# Trade-Alert API — Field Reference

Use the `fields` parameter to select specific columns. Use the `where` parameter to filter by any boolean field.

## Trade Fields (~120 fields)
Returned by: Trade Recaps, Spread Recaps

### Core
| Field | Type | Description |
|-------|------|-------------|
| `side` | int | NBBO side of trade |
| `size` | int | Trade size (contracts) |
| `price` | $ | Trade price |
| `exch` | string | Trade exchange |
| `time` | hh:mm:ss.sss | Trade time |
| `date` | yyyy-mm-dd | Trade date |
| `spot` | $ | Spot price at trade time |
| `spot_chg` | +/- | Spot price change on day |
| `volume` | int | Option volume at trade time |
| `open_int` | int | Open interest at trade date |

### NBBO Context
| Field | Type | Description |
|-------|------|-------------|
| `bid` | $ | NBBO bid at time of trade |
| `ask` | $ | NBBO ask at time of trade |
| `bsize` | int | NBBO bid size |
| `asize` | int | NBBO ask size |
| `bexch` | string | NBBO bid exchange |
| `aexch` | string | NBBO ask exchange |

### Greeks & Volatility
| Field | Type | Description |
|-------|------|-------------|
| `delta` | % | Delta at trade time |
| `vega` | real | Vega at trade time |
| `theta` | real | Theta at trade time |
| `gamma` | real | Gamma at trade time |
| `ivol` | real | Implied volatility at trade time |
| `ivol_chg` | real | IV change on day |
| `ivol_chg_pct` | real | IV change as percentage |
| `theo` | real | Theoretical value at trade time |

### Computed Values
| Field | Type | Description |
|-------|------|-------------|
| `net_delta` | real | Net delta when side is known |
| `net_vega` | real | Net vega when side is known |
| `notional` | $ | Notional value (contracts × spot × shares) |
| `premium` | $ | Premium value (contracts × price × shares) |
| `delta_impact` | real | Delta impact (contracts × delta × shares) |
| `vega_dollar` | $ | Vega dollar value (contracts × vega × shares) |
| `dollar_impact` | $ | Dollar impact (size × abs(delta) × spot × shares) |
| `gamma_shares` | real | Gamma shares (contracts × gamma × shares) |
| `gamma_dollar` | real | Gamma dollars (contracts × gamma × spot × shares) |
| `theta_dollar` | $ | Theta dollar (contracts × theta × shares) |
| `hedge_quantity` | real | Hedge quantity (size × delta × shares) |
| `edge` | real | Absolute difference between price and theo |

### Option Identity
| Field | Type | Description |
|-------|------|-------------|
| `usymbol` | string | Underlying symbol |
| `expiry` | yyyy-mm-dd | Expiration date |
| `strike` | real | Strike price |
| `put_call` | P/C | Option type |
| `symbol` | string | Security symbol |
| `osi_symbol` | string | OSI symbol |
| `root` | string | Option root |
| `shares` | int | Shares per contract |
| `dtx` | int | Days to expiration |
| `dow` | int | Trading day of week (1-5) |

### Market Side (string fields)
| Field | Type | Description |
|-------|------|-------------|
| `option` | string | "Put" or "Call" |
| `mktside` | string | "AskSide", "BidSide", "MidMkt" |
| `exchange` | string | Exchange mnemonic ("CBOE", "ISE", etc.) |
| `timestamp` | string | Timestamp as hh:mm:ss.sss |
| `condition` | string | Trade condition ("LATE", "SPD", "TIED", etc.) |
| `comments` | string | Context ("Pre-Earnings", "ExDiv", "52WeekHigh", etc.) |
| `sector` | string | Underlying sector |
| `subsector` | string | Underlying subsector |

### Boolean Flags (usable in `where` filter)
| Field | Description |
|-------|-------------|
| `sweep` | Multi-part trade (sweep or split ticket) |
| `split` | Single-exchange split ticket |
| `cancel` | Trade cancel |
| `part_of_sweep` | Part of a multi-part trade |
| `part_of_spread` | Part of identified complex trade |
| `complex` | Any complex trade |
| `buyer` | Assumed buyer |
| `seller` | Assumed seller |
| `bidsid` | Trade on bid side |
| `askside` | Trade on ask side |
| `put` | Trade was a put |
| `call` | Trade was a call |
| `itm` | In-the-money at trade time |
| `otm` | Out-of-the-money |
| `atm` | At-the-money |
| `normal` | Normal trade (OPRA cond) |
| `spread` | Spread trade (OPRA cond) |
| `tied` | Tied trade (exchange cond) |
| `late` | Late trade |
| `iso` | Intermarket sweep |
| `auction` | Auction trade |
| `cross` | Cross trade |
| `floor` | Floor trade |
| `cob` | COB trade |
| `legged` | Legged trade |
| `weekly` | Weekly expiry |
| `quarterly` | Quarterly expiry |
| `third_friday` | Third Friday expiry |
| `leap` | LEAP option |
| `gth` | Global trading hours trade |
| `ssr` | Short-sale restriction active |
| `ivhigh` | ATM IV at 52-week high |
| `ivlow` | ATM IV at 52-week low |
| `newhigh` | Spot at 52-week high |
| `newlow` | Spot at 52-week low |
| `earnings` | Pending earnings |
| `post_earnings` | Post-earnings |
| `exdiv` | Ex-dividend tomorrow |
| `divcapture` | Dividend capture trade |
| Month flags: `jan` through `dec` (3rd Friday expiry in that month) |
| Exchange flags: `amex`, `arca`, `box`, `bxo`, `bzx`, `c2`, `cboe`, `edgx`, `emld`, `gem`, `ise`, `nom`, `merc`, `miax`, `pearl`, `phlx`, `memx`, `sphr` |
| Exercise: `amer`, `euro`, `asian`, `cliquet` |
| Settlement: `am`, `pm`, `cash_settled`, `physical` |

### Post-Trade Fields
| Field | Type | Description |
|-------|------|-------------|
| `opt_close` | $ | Option closing price |
| `next_day_oi` | int | Open interest next day |
| `next_day_oi_chg` | int | OI change next day |

---

## Underlying Fields (~150 fields)
Returned by: Market Analysis commands

### Identity & Price
| Field | Type | Description |
|-------|------|-------------|
| `usymbol` | string | Underlying symbol |
| `date` | yyyy-mm-dd | Trading date |
| `spot` | real | Current spot price |
| `spot_chg` | real | Spot change on day |
| `close` | real | Closing price (historical) |
| `chg` | real | Price change on day (historical) |
| `atm` | real | ATM strike (midpoint if between strikes) |
| `atm1` | real | Lower ATM strike |
| `atm2` | real | Upper ATM strike |

### Volume
| Field | Type | Description |
|-------|------|-------------|
| `option_volume` | int | Total contracts traded |
| `put_volume` | int | Total put contracts |
| `call_volume` | int | Total call contracts |
| `put_pct` | % | Put percentage of total |
| `call_pct` | % | Call percentage of total |
| `directional_pct` | real | % directional volume (excl. spreads, late) |
| `put_trades` | int | Total put trades |
| `call_trades` | int | Total call trades |
| `trades` | int | Total trades |
| `adv` | int | Average daily contract volume |
| `avg_total_puts` | int | Avg put contracts (22 days) |
| `avg_total_calls` | int | Avg call contracts (22 days) |
| `equity_volume` | real | Total equity share volume |
| `avg_volume` | real | Avg daily share volume (22 days) |

### Volume Multiples
| Field | Type | Description |
|-------|------|-------------|
| `option_mult` | int | Option vol multiple vs ADV |
| `option_tw_mult` | int | Time-weighted vol multiple |
| `option_mw_mult` | int | Time & market-weighted vol multiple |
| `equity_mult` | int | Equity vol multiple vs avg |
| `pct_adv` | real | Option vol % of ADV |
| `tw_pct_adv` | real | Time-weighted % of ADV |

### Sentiment & Premium
| Field | Type | Description |
|-------|------|-------------|
| `bullish_pct` | % | Percentage bullish contracts |
| `bearish_pct` | % | Percentage bearish contracts |
| `neutral_pct` | % | Percentage neutral contracts |
| `put_ask_pct` | % | Puts traded on ask |
| `put_bid_pct` | % | Puts traded on bid |
| `put_mid_pct` | % | Puts traded at mid |
| `call_ask_pct` | % | Calls traded on ask |
| `call_bid_pct` | % | Calls traded on bid |
| `call_mid_pct` | % | Calls traded at mid |
| `put_prem` | real | Total put premium |
| `call_prem` | real | Total call premium |
| `bullish_c_prem` | real | Bullish call premium (on ask) |
| `bearish_c_prem` | real | Bearish call premium (on bid) |
| `bearish_p_prem` | real | Bearish put premium (on ask) |
| `bullish_p_prem` | real | Bullish put premium (on bid) |
| `bullish_on_ask` | real | Bullish contracts on ask |
| `bearish_on_ask` | real | Bearish contracts on ask |

### Delta & Vega
| Field | Type | Description |
|-------|------|-------------|
| `net_delta` | real | Total net delta$ on day |
| `net_vega` | real | Total net vega$ on day |
| `rolling_net_delta` | real | Net delta$ last 10 min |
| `rolling_puts` | int | Puts last 10 min |
| `rolling_calls` | int | Calls last 10 min |
| `rolling_buys` | int | Buys last 10 min |
| `rolling_sells` | int | Sells last 10 min |
| `rolling_bullish` | int | Bullish last 10 min |
| `rolling_bearish` | int | Bearish last 10 min |

### Open Interest
| Field | Type | Description |
|-------|------|-------------|
| `option_open_int` | int | Total OI |
| `option_oi_chg` | int | Total OI change |
| `put_open_int` | int | Put OI |
| `call_open_int` | int | Call OI |
| `oi_puts_chg` | int | Put OI change |
| `oi_calls_chg` | int | Call OI change |
| `volume_oi_pct` | real | Volume as % of OI |

### IV & Volatility
| Field | Type | Description |
|-------|------|-------------|
| `atm_ivol` | real | ATM 30-day implied vol |
| `atm_ivol_chg` | real | ATM IV change on day |
| `atm_ivol_chg_pct` | real | ATM IV change % |
| `volatility20day` | real | 20-day historical vol |

### ATM/OTM/ITM Breakdown
For each bucket (atm_p, atm_c, otm_p, otm_c, itm_p, itm_c):
| Suffix | Description |
|--------|-------------|
| `_buy` | Contracts on buy side |
| `_sell` | Contracts on sell side |
| `_vol` | Total volume |
| `_oi` | Open interest |
| `_vega` | Net dollar vega |
| `_delta_buy` | Net dollar delta on buy side |
| `_delta_sell` | Net dollar delta on sell side |

Example: `otm_c_buy` = OTM calls on buy side

### Edge
| Field | Type | Description |
|-------|------|-------------|
| `total_edge` | real | Total edge for normal trades |
| `spread_edge` | real | Total edge for spread trades |
| `size_edge` | int | Total size for normal trades |

### Classification
| Field | Type | Description |
|-------|------|-------------|
| `sectype` | I/E/S/C | Index, ETF, Stock, Crypto |
| `cap` | S/M/L | Small, Mid, Large cap |
| `sector` | string | Industry sector |
| `subsector` | string | Industry subsector |
| `naics_code` | string | NAICS code |

### Per-Exchange Volume
All 18 exchanges available: `amex`, `arca`, `bzx`, `box`, `bxo`, `c2`, `cboe`, `ise`, `nom`, `miax`, `pearl`, `phlx`, `gem`, `edgx`, `merc`, `emld`, `memx`, `sphr`
- `{exchange}` = total contracts on exchange
- `{exchange}_puts` = put contracts on exchange
- `{exchange}_calls` = call contracts on exchange

### Boolean Flags (for `where` filter)
`ssr`, `ivhigh`, `ivlow`, `newhigh`, `newlow`, `earnings`, `post_earnings`, `exdiv`

---

## Option Fields (~60 fields)
Returned by: Security Analysis commands (Moso, OI, OIChg, etc.)

| Field | Type | Description |
|-------|------|-------------|
| `sold` | int | Volume on bid side |
| `bot` | int | Volume on ask side |
| `volume` | int | Total volume |
| `trades` | int | Total trades |
| `open_int` | int | Current OI |
| `oichg` | int | OI change from previous day |
| `bid_pct` | % | Percent on bid |
| `mid_pct` | % | Percent at mid |
| `ask_pct` | % | Percent on ask |
| `delta` | real | Delta at last trade |
| `vega` | real | Vega at last trade |
| `gamma` | real | Gamma at last trade |
| `ivol` | real | IV at last trade |
| `ivolchg` | real | IV change on day |
| `vwap_total` | real | Volume-weighted avg price |
| `delta_buy` | real | Net delta impact (buy side) |
| `delta_sell` | real | Net delta impact (sell side) |
| `vega_dollar` | real | Net vega dollar |
| `next_day_oi` | int | Next day OI |
| `on_bid_hist` | int | Life-to-date volume on bid |
| `on_mid_hist` | int | Life-to-date volume at mid |
| `on_ask_hist` | int | Life-to-date volume on ask |
| `comments` | string | Context flags |
| `spot` | $ | Spot price |
| `spot_chg` | $ | Spot change |
| `avg_volume` | real | Avg volume of underlying |

Plus standard option identity fields: `usymbol`, `expiry`, `strike`, `put_call`, `symbol`, `root`, `dtx`, `shares`, `nonstd`, `flex`, `ex_style`, `am_pm`, `settle`, and boolean type/expiry flags.

---

## Note Fields
Returned by: Color, News commands

| Field | Type | Description |
|-------|------|-------------|
| `text` | string | Note/commentary text |
| `comments` | string | Additional context |
| `time` | string | Timestamp |
