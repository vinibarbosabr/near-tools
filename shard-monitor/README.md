# near-tools

> A collection of tools for the NEAR ecosystem, focused on research, monitoring, and developer experience.

This repository contains high-quality, lightweight tools built for the NEAR Protocol. The main focus is on creating useful utilities for researchers, validators, developers, and security analysts working with NEAR.

## Current Tools

| Tool              | Description                                      | Status     |
|-------------------|--------------------------------------------------|------------|
| **shard-monitor** | Check the current number of active shards on NEAR Testnet/Mainnet | ✅ Active |

---

## shard-monitor

Monitor the number of active shards on NEAR in real time.

### Features

- Shows current shard count using the official RPC
- Supports both **Testnet** and **Mainnet**
- Watch mode for continuous monitoring
- JSON output for scripting and automation
- Zero external dependencies (pure Python standard library)

### Installation

```bash
git clone https://github.com/vinibarbosabr/near-tools.git
cd near-tools/shard-monitor
chmod +x shard-count.py
```

### Usage

```bash
# Check Testnet shards (default)
./shard-count.py

# Check Mainnet shards
./shard-count.py --network mainnet

# Continuous monitoring (updates every 30 seconds)
./shard-count.py --watch 30

# Output as JSON (useful for scripts)
./shard-count.py --json
```

### How It Works 

In NEAR’s Nightshade sharding architecture, each shard produces exactly one chunk per block. Therefore, the number of chunks included in a finalized block equals the number of currently active shards on the network.This method is also used internally by the official NEAR Lake indexer.

## Why near-tools?

These tools are built with the following goals:
- **Simplicity** — Minimal dependencies and easy to run
- **Reliability** — Use official NEAR RPC methods
- **Research-friendly** — Suitable for monitoring, dashboards, and data collection
- **NEAR-native** — Focused specifically on the NEAR ecosystem

## Contributing

Contributions are welcome! If you have ideas for new tools or improvements to existing ones, feel free to open an issue or submit a pull request.

Before contributing, please check the existing tools and try to follow the same code style and structure.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


