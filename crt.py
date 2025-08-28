#!/usr/bin/env python3

import sys
import json
import argparse
from datetime import datetime, timezone, timedelta
from pathlib import Path

__version__ = "1.1.0"
CONFIG_FILE = Path.home() / '.crt_config.json'

def load_config():
    """Load configuration from file or return default"""
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE) as f:
                return json.load(f)
        except:
            pass
    
    # Default config with known refresh time: 08/25/2025 2:00 AM EST
    return {
        'last_refresh': '2025-08-25T02:00:00-05:00'  # ISO format with EST timezone
    }

def save_config(config):
    """Save configuration to file"""
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)
    except Exception as e:
        print(f"Warning: Could not save config: {e}", file=sys.stderr)

def parse_datetime_input(dt_str):
    """Parse various datetime input formats"""
    if dt_str.lower() == 'now':
        return datetime.now().astimezone()
    
    # Try common formats
    formats = [
        '%Y-%m-%d %I:%M %p %Z',      # 2025-08-27 3:00 PM EST (backward compatibility)
        '%Y-%m-%d %H:%M %Z',         # 2025-08-27 15:00 EST (backward compatibility)
        '%Y-%m-%d %I:%M %p',         # 2025-08-27 3:00 PM (local timezone)
        '%Y-%m-%d %H:%M',            # 2025-08-27 15:00 (local timezone)
        '%m/%d/%Y %I:%M %p %Z',      # 08/27/2025 3:00 PM EST (backward compatibility)
        '%m/%d/%Y %H:%M %Z',         # 08/27/2025 15:00 EST (backward compatibility)
        '%m/%d/%Y %I:%M %p',         # 08/27/2025 3:00 PM (local timezone)
        '%m/%d/%Y %H:%M',            # 08/27/2025 15:00 (local timezone)
    ]
    
    # Handle timezone abbreviations (for backward compatibility)
    tz_map = {
        'EST': timezone(timedelta(hours=-5)),
        'EDT': timezone(timedelta(hours=-4)),
        'PST': timezone(timedelta(hours=-8)),
        'PDT': timezone(timedelta(hours=-7)),
        'UTC': timezone.utc
    }
    
    for fmt in formats:
        try:
            if '%Z' in fmt:
                # Extract timezone from string (backward compatibility)
                parts = dt_str.strip().split()
                if parts and parts[-1].upper() in tz_map:
                    tz_name = parts[-1].upper()
                    dt_without_tz = ' '.join(parts[:-1])
                    dt = datetime.strptime(dt_without_tz, fmt.replace(' %Z', ''))
                    return dt.replace(tzinfo=tz_map[tz_name])
            else:
                # Use local system timezone for formats without timezone
                dt = datetime.strptime(dt_str, fmt)
                return dt.replace(tzinfo=datetime.now().astimezone().tzinfo)
        except ValueError:
            continue
    
    raise ValueError(f"Could not parse datetime: {dt_str}")


def get_next_refresh_time():
    """Calculate next refresh time based on config"""
    config = load_config()
    last_refresh_str = config['last_refresh']
    
    # Parse the stored refresh time
    last_refresh = datetime.fromisoformat(last_refresh_str)
    refresh_interval = timedelta(hours=5)
    
    # Current time in UTC
    now = datetime.now(timezone.utc)
    last_refresh_utc = last_refresh.astimezone(timezone.utc)
    
    # Calculate how many intervals have passed
    time_diff = now - last_refresh_utc
    intervals_passed = int(time_diff.total_seconds() // refresh_interval.total_seconds())
    
    # Next refresh time
    if time_diff.total_seconds() % refresh_interval.total_seconds() == 0:
        next_refresh = now
    else:
        next_refresh = last_refresh_utc + refresh_interval * (intervals_passed + 1)
    
    return next_refresh

def format_output(next_refresh):
    """Format output with datetime first, then countdown"""
    now = datetime.now(timezone.utc)
    remaining = next_refresh - now
    
    # Always use auto-detected system timezone
    next_refresh_local = next_refresh.astimezone()
    tz_name = next_refresh_local.strftime('%Z')  # System timezone name
    
    # Format datetime
    datetime_str = next_refresh_local.strftime('%Y-%m-%d %I:%M:%S %p')
    
    if remaining.total_seconds() <= 0:
        return f"Next refresh: {datetime_str} {tz_name} (happening now!)"
    
    # Calculate time remaining
    hours = int(remaining.total_seconds() // 3600)
    minutes = int((remaining.total_seconds() % 3600) // 60)
    seconds = int(remaining.total_seconds() % 60)
    
    if hours > 0:
        countdown = f"in {hours} hours {minutes} mins"
    elif minutes > 0:
        countdown = f"in {minutes} mins {seconds} secs"
    else:
        countdown = f"in {seconds} secs"
    
    return f"Next refresh: {datetime_str} {tz_name} ({countdown})"

def calibrate(datetime_str):
    """Set new calibration point"""
    try:
        new_refresh = parse_datetime_input(datetime_str)
        
        # Convert to ISO format for storage
        iso_str = new_refresh.isoformat()
        
        config = load_config()
        config['last_refresh'] = iso_str
        save_config(config)
        
        print(f"✓ Calibrated refresh time to: {new_refresh.strftime('%Y-%m-%d %I:%M:%S %p %Z')}")
        
    except ValueError as e:
        print(f"Error: {e}")
        print("Examples:")
        print("  crt --calibrate 'now'")
        print("  crt --calibrate '2025-08-27 3:00 PM'")
        print("  crt --calibrate '08/27/2025 15:00'")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='Claude Refresh Time - Track your Claude Code Pro token refresh times',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  crt                              # Show next refresh time
  crt --calibrate 'now'            # Set current time as refresh point
  crt --calibrate '2025-08-27 3:00 PM'     # Set specific time (uses system timezone)
        """
    )
    
    parser.add_argument('--calibrate', '-c', metavar='DATETIME',
                       help='Set new refresh time calibration point (uses system timezone)')
    parser.add_argument('--version', '-v', action='version',
                       version=f'Claude Refresh Time (CRT) v{__version__}')
    
    args = parser.parse_args()
    
    try:
        if args.calibrate:
            calibrate(args.calibrate)
        else:
            next_refresh = get_next_refresh_time()
            print(format_output(next_refresh))
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()