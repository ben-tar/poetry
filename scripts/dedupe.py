import json,sys,hashlib
seen=set()
for line in sys.stdin:
    r=json.loads(line)
    h=hashlib.sha256(r["text"].strip().encode("utf-8")).hexdigest()
    if h in seen:
        continue
    seen.add(h)
    r["hash"]=f"sha256:{h}"
    print(json.dumps(r,ensure_ascii=False))
