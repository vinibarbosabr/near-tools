# NEAR Shard Monitor

Simple tool to check the current number of active shards on NEAR Testnet or Mainnet.

## Features

- Shows current shard count (based on chunks in the latest finalized block)
- Supports both Testnet and Mainnet
- Watch/monitoring mode
- JSON output for scripting
- No external dependencies (pure Python stdlib)

## Installation

```bash
git clone https://github.com/vinibarbosabr/vinib-tools/near/shard-monitor.git
cd shard-monitor
chmod +x shard-count.py
```

## Usage

The script currently defaults to `testnet`.
Add `--network mainnet` flag to get the mainnet shard count.

```bash
# Check Testnet (default)
./near_shards.py

# Check Mainnet
./near_shards.py --network mainnet

# Continuous monitoring
./near_shards.py --watch 30

# JSON output
./near_shards.py --json
```

## Why This Works

In NEAR’s Nightshade architecture, each shard produces one chunk per block.
Therefore, the number of chunks in a finalized block equals the number of currently active shards.

## License

MIT 


```
