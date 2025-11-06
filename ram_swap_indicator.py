#!/usr/bin/env python3
import gi
gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3, Gtk, GLib
import psutil

APPINDICATOR_ID = 'ram_swap_indicator'

def format_size(bytes_value):
    """Convert bytes to human-readable format (e.g. 2.5G, 512M)."""
    for unit in ['B', 'K', 'M', 'G', 'T']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.1f}{unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.1f}P"

def get_usage():
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()

    # Match GNOME System Monitor (exclude cache and buffers)
    ram_used = mem.total - mem.available
    ram_total = mem.total
    swap_used = swap.used
    swap_total = swap.total

    ram_percent = (ram_used / ram_total) * 100 if ram_total else 0
    swap_percent = (swap_used / swap_total) * 100 if swap_total else 0

    def fmt(b): return format_size(b)

    return (
        f"RAM: {fmt(ram_used)}/{fmt(ram_total)} ({ram_percent:.0f}%) "
        f"| SWAP: {fmt(swap_used)}/{fmt(swap_total)} ({swap_percent:.0f}%)"
    )

def update(indicator):
    indicator.set_label(get_usage(), "")
    return True  # keep running

def quit(_):
    Gtk.main_quit()

def main():
    indicator = AppIndicator3.Indicator.new(
        APPINDICATOR_ID,
        "dialog-information",
        AppIndicator3.IndicatorCategory.SYSTEM_SERVICES
    )
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
    indicator.set_label("Loading...", "")

    # Add menu
    menu = Gtk.Menu()
    quit_item = Gtk.MenuItem(label='Quit')
    quit_item.connect('activate', quit)
    menu.append(quit_item)
    menu.show_all()
    indicator.set_menu(menu)

    # Update every 3 seconds
    GLib.timeout_add_seconds(3, update, indicator)

    Gtk.main()

if __name__ == "__main__":
    main()
