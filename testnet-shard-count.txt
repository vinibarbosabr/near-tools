# this script will return the current shard count on NEAR testnet
# built to monitor tests of the dynamic resharding implementation on nearcore v2.13
# by vinib (vinibarbosabr) on July 3, 2026

python3 -c "
import urllib.request, json, datetime
req = urllib.request.Request('https://rpc.testnet.near.org', data=json.dumps({'jsonrpc':'2.0','id':1,'method':'block','params':{'finality':'final'}}).encode(), headers={'Content-Type':'application/json'})
with urllib.request.urlopen(req, timeout=10) as r: d = json.load(r)
h = d['result']['header']
shards = h.get('chunks_included') or len(d['result'].get('chunks', []))
ts = datetime.datetime.fromtimestamp(h['timestamp']/1e9, tz=datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
print(f'🌐 NEAR Testnet Shards: {shards}')
print(f'📦 Block Height: {h[\"height\"]}')
print(f'🕒 Time: {ts}')
print(f'🔗 https://testnet.nearblocks.io/blocks/{h[\"height\"]}')
"
