# Changelog

All notable changes to Claude Refresh Time (CRT) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-08-27

### Added
- Initial release of Claude Refresh Time (CRT) tool
- Command-line interface to track Claude Code Pro token refresh times
- Automatic system timezone detection (default behavior)
- Manual timezone override support (EST, EDT, PST, PDT, UTC, LOCAL)
- Calibration system to adjust refresh time when Claude changes schedule
- Persistent configuration storage in `~/.crt_config.json`
- Flexible datetime input parsing for calibration
- Cross-platform support (Linux, macOS, Windows)
- Zero dependencies - uses only Python standard library
- Version tracking with `--version` option

### Features
- 🕐 Shows next refresh time with countdown
- 🌍 Multiple timezone support with auto-detection
- ⚙️ Easy calibration with `--calibrate` option
- 💾 Persistent configuration storage
- 🪶 Lightweight - no external dependencies