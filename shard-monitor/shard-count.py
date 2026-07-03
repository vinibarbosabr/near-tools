#!/usr/bin/env python3
"""
NEAR Shard Monitor
Check the current number of active shards on NEAR Testnet or Mainnet.
"""

import argparse
import json
import urllib.request
import datetime
import sys
import time


def get_shard_info(network: str = "testnet"):
    rpc_url = f"https://rpc.{network}.near.org"
    
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "block",
        "params": {"finality": "final"}
    }
    
    req = urllib.request.Request(
        rpc_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read())
    except Exception as e:
        print(f"❌ Error connecting to {rpc_url}: {e}", file=sys.stderr)
        sys.exit(1)
    
    result = data.get("result", {})
    header = result.get("header", {})
    chunks = result.get("chunks", [])
    
    shard_count = header.get("chunks_included") or len(chunks)
    
    return {
        "network": network,
        "shards": shard_count,
        "height": header.get("height"),
        "timestamp": header.get("timestamp"),
        "rpc_url": rpc_url
    }


def format_output(info: dict, json_output: bool = False):
    if json_output:
        print(json.dumps(info, indent=2))
        return
    
    ts = datetime.datetime.fromtimestamp(
        info["timestamp"] / 1e9, tz=datetime.timezone.utc
    ).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    explorer_base = "testnet.nearblocks.io" if info["network"] == "testnet" else "nearblocks.io"
    explorer_url = f"https://{explorer_base}/blocks/{info['height']}"
    
    print(f"🌐 NEAR {info['network'].capitalize()} Shards: {info['shards']}")
    print(f"📦 Block Height: {info['height']}")
    print(f"🕒 Timestamp:   {ts}")
    print(f"🔗 Explorer:    {explorer_url}")


def main():
    parser = argparse.ArgumentParser(
        description="Check current number of shards on NEAR Protocol",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--network", 
        choices=["testnet", "mainnet"], 
        default="testnet",
        help="NEAR network to query"
    )
    parser.add_argument(
        "--json", 
        action="store_true", 
        help="Output result as JSON (useful for scripting)"
    )
    parser.add_argument(
        "--watch", 
        type=int, 
        metavar="SECONDS",
        help="Continuously monitor every N seconds"
    )
    
    args = parser.parse_args()
    
    if args.watch:
        print(f"Monitoring NEAR {args.network} every {args.watch}s (Ctrl+C to stop)...\n")
        try:
            while True:
                info = get_shard_info(args.network)
                format_output(info, args.json)
                print("-" * 50)
                time.sleep(args.watch)
        except KeyboardInterrupt:
            print("\nStopped.")
    else:
        info = get_shard_info(args.network)
        format_output(info, args.json)


if __name__ == "__main__":
    main()
