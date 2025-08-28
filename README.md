# Claude Refresh Time (CRT)

A lightweight command-line tool to track your Claude Code Pro token refresh times. Never miss your 5-hour refresh window again!

## Features

- 🕐 Shows next refresh time with countdown
- 🌍 Automatic timezone detection (EST/EDT/PST/PDT)
- ⚙️ Easy calibration when refresh times change
- 💾 Persistent configuration storage
- 🪶 Zero dependencies (Python standard library only)

## Quick Start

```bash
# Show next refresh time
crt

# Output: Next refresh: 2025-08-27 02:00:00 PM EDT (in 3 hours 45 mins)
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
python crt.py
python crt.py --calibrate "2025-08-27 3:00 PM"
```

## Usage

### Basic Commands
```bash
# Show next refresh time (auto-detects your timezone)
crt

# Show help
crt --help
```

### Calibration
When Claude changes their refresh schedule, recalibrate:

```bash
# Set current time as new refresh point
crt --calibrate "now"

# Set specific time (uses your system timezone)
crt --calibrate "2025-08-27 3:00 PM"
crt -c "08/27/2025 15:00"

# Supported formats:
crt -c "2025-08-27 3:00 PM"
crt -c "2025-08-27 15:00"  
crt -c "08/27/2025 3:00 PM"
crt -c "now"
```

### Timezone Handling
CRT automatically detects your system timezone and displays times accordingly:
- **Eastern Time**: Shows as EST (winter) or EDT (summer)
- **Pacific Time**: Shows as PST (winter) or PDT (summer)  
- **Other timezones**: Uses your system's timezone settings

No need to specify timezones manually - everything is handled automatically!

## Examples

```bash
# Basic usage
$ crt
Next refresh: 2025-08-27 02:00:00 PM EDT (in 3 hours 45 mins)

# Calibrate to current time
$ crt -c "now"
✓ Calibrated refresh time to: 2025-08-27 10:15:00 AM EDT

# Check after calibration
$ crt
Next refresh: 2025-08-27 03:15:00 PM EDT (in 5 hours 0 mins)
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
python crt.py
```

## Contributing

Feel free to submit issues and pull requests!

## License

MIT License - see LICENSE file for details.