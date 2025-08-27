# Claude Refresh Time (CRT)

A lightweight command-line tool to track your Claude Code Pro token refresh times. Never miss your 5-hour refresh window again!

## Features

- 🕐 Shows next refresh time with countdown
- 🌍 Multiple timezone support (EST, PST, UTC, etc.)
- ⚙️ Easy calibration when refresh times change
- 💾 Persistent configuration storage
- 🪶 Zero dependencies (Python standard library only)

## Quick Start

```bash
# Show next refresh time
crt

# Output: Next refresh: 2025-08-27 02:00:00 PM EST (in 3 hours 45 mins)
```

## Installation

### Linux (Arch/Ubuntu/etc.)

```bash
# Clone the repository
git clone https://github.com/yourusername/claude_refresh_time.git
cd claude_refresh_time

# Install to ~/.local/bin
mkdir -p ~/.local/bin
cp crt.py ~/.local/bin/crt
chmod +x ~/.local/bin/crt

# Add to PATH (if not already there)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc  # or ~/.zshrc
source ~/.bashrc  # or source ~/.zshrc

# Test
crt
```

### macOS

```bash
# Clone the repository
git clone https://github.com/yourusername/claude_refresh_time.git
cd claude_refresh_time

# Install to /usr/local/bin (requires sudo)
sudo cp crt.py /usr/local/bin/crt
sudo chmod +x /usr/local/bin/crt

# Alternative: User-local installation
mkdir -p ~/.local/bin
cp crt.py ~/.local/bin/crt
chmod +x ~/.local/bin/crt
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Test
crt
```

### Windows

#### Option 1: Windows Subsystem for Linux (WSL)
Follow the Linux instructions above in your WSL environment.

#### Option 2: Native Windows (PowerShell/Command Prompt)
```cmd
# Clone the repository
git clone https://github.com/yourusername/claude_refresh_time.git
cd claude_refresh_time

# Create a batch wrapper (crt.bat)
echo @python "%~dp0crt.py" %* > crt.bat

# Add the directory to your PATH:
# 1. Open System Properties > Environment Variables
# 2. Add the script directory to your PATH
# 3. Or move crt.py and crt.bat to a directory already in PATH

# Test
crt
```

#### Option 3: Python Script (All platforms)
```bash
# Run directly with Python
python crt.py
python crt.py --timezone PST
python crt.py --calibrate "2025-08-27 3:00 PM EST"
```

## Usage

### Basic Commands
```bash
# Show next refresh time (EST by default)
crt

# Show in different timezone
crt --timezone PST
crt -tz UTC
crt -tz LOCAL

# Show help
crt --help
```

### Calibration
When Claude changes their refresh schedule, recalibrate:

```bash
# Set current time as new refresh point
crt --calibrate "now"

# Set specific time
crt --calibrate "2025-08-27 3:00 PM EST"
crt -c "08/27/2025 15:00 EST"

# Supported formats:
crt -c "2025-08-27 3:00 PM EST"
crt -c "2025-08-27 15:00 EST"  
crt -c "08/27/2025 3:00 PM EST"
crt -c "now"
```

### Supported Timezones
- `EST` - Eastern Standard Time (default)
- `EDT` - Eastern Daylight Time
- `PST` - Pacific Standard Time
- `PDT` - Pacific Daylight Time
- `UTC` - Coordinated Universal Time
- `LOCAL` - Your system timezone

## Examples

```bash
# Basic usage
$ crt
Next refresh: 2025-08-27 02:00:00 PM EST (in 3 hours 45 mins)

# Different timezone
$ crt -tz PST
Next refresh: 2025-08-27 11:00:00 AM PST (in 3 hours 45 mins)

# Calibrate to current time
$ crt -c "now"
✓ Calibrated refresh time to: 2025-08-27 10:15:00 AM UTC-05:00

# Check after calibration
$ crt
Next refresh: 2025-08-27 03:15:00 PM EST (in 5 hours 0 mins)
```

## How It Works

Claude Code Pro refreshes tokens every 5 hours. Given one known refresh time, the tool calculates all future refresh times by adding 5-hour intervals. The configuration is stored in `~/.crt_config.json`.

## Requirements

- Python 3.6+ (uses standard library only)
- No external dependencies required

## Development

```bash
# Clone and test locally
git clone https://github.com/yourusername/claude_refresh_time.git
cd claude_refresh_time
python crt.py

# Make changes and test
python crt.py --calibrate "now"
python crt.py --timezone UTC
```

## Contributing

Feel free to submit issues and pull requests!

## License

MIT License - see LICENSE file for details.