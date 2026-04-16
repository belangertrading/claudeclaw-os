#!/usr/bin/env python3
"""
Trade Sheet Updater — All Services

Usage:
  update_sheet.py <service> <action> [args...]

Services:
  options-insider (or oi)
  hot-money (or hm)
  48hr (or 48hr-cashflow)

Actions:
  buy   — open new trade
  sell  — close trade
  delete — undo (delete open row or re-open closed)

Examples:
  update_sheet.py oi buy SCHW "Two-Way Trigger" "Strangle" "2/27/26" "C/P" 96 93 3.22 3.86 "10-day" "2/13/26" "https://..."
  update_sheet.py hm sell STM 3.00 "2/9/2026" "https://..."
  update_sheet.py 48hr buy FIG "Put Spread" "Feb 20, 2026" 0.10 21 20.5
  update_sheet.py 48hr sell FIG 0 "2/20/2026" "https://..."
  update_sheet.py oi delete SCHW "2/27/26"
"""

import json
import sys
import subprocess

WEBHOOKS = {
    "options-insider": "https://script.google.com/macros/s/AKfycby8b-gFkH_UkfIhg0nYTCmCeagXfiJzXRFU-j3movoU9HE03K7qtR07mn5_5Wi7Fc1oTw/exec",
    "hot-money": "https://script.google.com/macros/s/AKfycbz4o0eF_rqmqPwERnu61Yt-mw2QI_pPOGu-Yh5to61bdzCpJOwVaudkmxrPA0v9X42t/exec",
    "48hr": "https://script.google.com/macros/s/AKfycbyPMKg4GL32cBRjBziHE4zXE0u68CMRixcmSCqrSy_6wh2k_NXc9Ym-ivbIav7Om8eQ/exec",
}

ALIASES = {"oi": "options-insider", "hm": "hot-money", "48hr-cashflow": "48hr"}


def send(service, payload):
    url = WEBHOOKS[service]
    cmd = ["curl", "-s", "-w", "%{redirect_url}", "-o", "/dev/null",
           "-X", "POST", "-H", "Content-Type: application/json",
           "-d", json.dumps(payload), url]
    redirect = subprocess.run(cmd, capture_output=True, text=True).stdout.strip()
    if redirect:
        result = subprocess.run(["curl", "-sL", redirect], capture_output=True, text=True)
        return json.loads(result.stdout) if result.stdout else {"error": "No response"}
    return {"error": "No redirect URL"}


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    svc_raw = sys.argv[1].lower()
    service = ALIASES.get(svc_raw, svc_raw)
    if service not in WEBHOOKS:
        print(f"Unknown service: {svc_raw}. Use: options-insider, hot-money, 48hr")
        sys.exit(1)

    action = sys.argv[2].lower()
    args = sys.argv[3:]

    if action == "buy":
        if service == "options-insider":
            # args: ticker signalType strategy expCycle type leg1 leg2 entryPrice tp sl entryDate [buyLink]
            payload = {
                "action": "buy", "ticker": args[0], "signalType": args[1],
                "strategy": args[2], "expCycle": args[3], "type": args[4],
                "leg1Strike": args[5], "leg2Strike": args[6],
                "entryPrice": args[7], "takeProfit": args[8], "stopLoss": args[9],
                "entryDate": args[10] if len(args) > 10 else None,
                "buyAlertLink": args[11] if len(args) > 11 else None,
            }
        elif service == "hot-money":
            # args: ticker strategy expCycle type longStrike entryPrice tp sl [shortStrike] [entryDate] [buyLink]
            payload = {
                "action": "buy", "ticker": args[0], "strategy": args[1],
                "expCycle": args[2], "type": args[3], "longStrike": args[4],
                "entryPrice": float(args[5]), "takeProfit": float(args[6]),
                "stopLoss": float(args[7]),
                "shortStrike": args[8] if len(args) > 8 else "",
                "entryDate": args[9] if len(args) > 9 else None,
                "buyAlertLink": args[10] if len(args) > 10 else None,
            }
        elif service == "48hr":
            # args: ticker strategy expCycle entryPrice shortStrike longStrike [entryDate] [earnings] [buyLink]
            payload = {
                "action": "buy", "ticker": args[0], "strategy": args[1],
                "expCycle": args[2], "entryPrice": float(args[3]),
                "shortStrike": float(args[4]), "longStrike": float(args[5]),
                "entryDate": args[6] if len(args) > 6 else None,
                "earnings": args[7] if len(args) > 7 else None,
                "buyAlertLink": args[8] if len(args) > 8 else None,
            }

    elif action == "sell":
        # args: ticker exitPrice [exitDate] [sellLink]
        payload = {
            "action": "sell", "ticker": args[0],
            "exitPrice": float(args[1]) if args[1] else 0,
            "exitDate": args[2] if len(args) > 2 else None,
            "sellAlertLink": args[3] if len(args) > 3 else None,
        }
        if service == "options-insider" and len(args) > 4:
            payload["expCycle"] = args[4]

    elif action == "delete":
        # args: ticker [expCycle]
        payload = {"action": "delete", "ticker": args[0]}
        if len(args) > 1:
            payload["expCycle"] = args[1]

    elif action == "update" and service == "hot-money":
        # args: ticker field=value ...
        payload = {"action": "update", "ticker": args[0]}
        for pair in args[1:]:
            k, v = pair.split("=", 1)
            payload[k] = v

    else:
        print(f"Unknown action: {action}")
        sys.exit(1)

    # Remove None values
    payload = {k: v for k, v in payload.items() if v is not None}

    result = send(service, payload)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result.get("success") else 1)


if __name__ == "__main__":
    main()
