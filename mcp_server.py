import sys
import json
from client import STDPSynapse

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "stdp_update":
        syn = STDPSynapse(params.get("initial_weight", 0.5))
        return syn.update_weight(params.get("t_pre", 10.0), params.get("t_post", 15.0))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
