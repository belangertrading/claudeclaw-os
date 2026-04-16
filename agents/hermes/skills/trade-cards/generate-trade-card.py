#!/usr/bin/env python3
"""
Generate Belanger Trading trade card graphics
Bloomberg dark style matching our charts
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import os
from datetime import datetime

# Bloomberg dark style colors
COLORS = {
    'bg': '#0a0a0b',
    'card_bg': '#161618',
    'border': '#2a2a2d',
    'text': '#e8e8e8',
    'text_muted': '#888888',
    'green': '#22c55e',
    'red': '#ef4444',
    'blue': '#3b82f6',
    'amber': '#f59e0b'
}

def generate_trade_card(
    ticker: str,
    strike: float,
    option_type: str,  # 'Call' or 'Put'
    expiration: str,
    entry: float,
    target: float,
    stop: float,
    pattern: str,
    win_loss: str,  # e.g., "5W - 1L"
    total_return: str,  # e.g., "466%"
    direction: str = 'BUY',  # 'BUY' or 'SELL'
    output_path: str = None
):
    # Calculate percentages
    target_pct = ((target - entry) / entry) * 100
    stop_pct = ((stop - entry) / entry) * 100
    
    # Create figure
    fig, ax = plt.subplots(figsize=(5, 6), facecolor=COLORS['bg'])
    ax.set_facecolor(COLORS['bg'])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Main card background
    card = FancyBboxPatch(
        (0.5, 0.5), 9, 11,
        boxstyle="round,pad=0.05,rounding_size=0.3",
        facecolor=COLORS['card_bg'],
        edgecolor=COLORS['border'],
        linewidth=2
    )
    ax.add_patch(card)
    
    # Direction badge
    badge_color = COLORS['green'] if direction == 'BUY' else COLORS['red']
    badge = FancyBboxPatch(
        (1, 10), 3.5, 1,
        boxstyle="round,pad=0.02,rounding_size=0.2",
        facecolor=badge_color,
        edgecolor='none',
        alpha=0.9
    )
    ax.add_patch(badge)
    ax.text(2.75, 10.5, f"{direction} ALERT", fontsize=11, fontweight='bold',
            color='white', ha='center', va='center', fontfamily='monospace')
    
    # Ticker and option details
    ax.text(5, 9, f"{ticker} ${strike} {option_type}", fontsize=18, fontweight='bold',
            color=COLORS['text'], ha='center', va='center', fontfamily='monospace')
    ax.text(5, 8.2, expiration, fontsize=12,
            color=COLORS['text_muted'], ha='center', va='center', fontfamily='monospace')
    
    # Divider line
    ax.plot([1, 9], [7.5, 7.5], color=COLORS['border'], linewidth=1)
    
    # Trade details
    details_y = 6.5
    ax.text(1.5, details_y, "Entry:", fontsize=11, color=COLORS['text_muted'], 
            va='center', fontfamily='monospace')
    ax.text(8.5, details_y, f"${entry:.2f}", fontsize=11, color=COLORS['text'], 
            va='center', ha='right', fontweight='bold', fontfamily='monospace')
    
    details_y -= 1
    ax.text(1.5, details_y, "Target:", fontsize=11, color=COLORS['text_muted'], 
            va='center', fontfamily='monospace')
    ax.text(8.5, details_y, f"${target:.2f}  (+{target_pct:.0f}%)", fontsize=11, 
            color=COLORS['green'], va='center', ha='right', fontweight='bold', fontfamily='monospace')
    
    details_y -= 1
    ax.text(1.5, details_y, "Stop:", fontsize=11, color=COLORS['text_muted'], 
            va='center', fontfamily='monospace')
    ax.text(8.5, details_y, f"${stop:.2f}  ({stop_pct:.0f}%)", fontsize=11, 
            color=COLORS['red'], va='center', ha='right', fontweight='bold', fontfamily='monospace')
    
    # Divider line
    ax.plot([1, 9], [3.8, 3.8], color=COLORS['border'], linewidth=1)
    
    # Pattern info
    ax.text(5, 3, pattern, fontsize=12, fontweight='bold',
            color=COLORS['blue'], ha='center', va='center', fontfamily='monospace')
    ax.text(5, 2.2, f"{win_loss}  |  {total_return} returns", fontsize=10,
            color=COLORS['text_muted'], ha='center', va='center', fontfamily='monospace')
    
    # Branding
    ax.text(5, 1, "BELANGER TRADING", fontsize=9, 
            color=COLORS['text_muted'], ha='center', va='center', 
            fontfamily='monospace', alpha=0.6)
    
    plt.tight_layout()
    
    # Save
    if output_path is None:
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        output_path = f"/var/www/html/charts/{ticker}_trade_card_{timestamp}.png"
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches='tight', 
                facecolor=COLORS['bg'], edgecolor='none')
    plt.close()
    
    return output_path


if __name__ == "__main__":
    # Example: DDOG trade card
    path = generate_trade_card(
        ticker="DDOG",
        strike=148,
        option_type="Call",
        expiration="Feb 27, 2026",
        entry=6.50,
        target=9.75,
        stop=3.25,
        pattern="U-Turn Velocity",
        win_loss="5W - 1L",
        total_return="466%",
        direction="BUY"
    )
    print(f"Generated: https://joshbelanger.com/charts/{os.path.basename(path)}")
