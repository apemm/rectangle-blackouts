"""Check saved finite partitions without importing the queue scheduler."""

import hashlib
import json
from itertools import combinations
from math import isqrt
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    source = here / "continuation_monotone_queue_certificates.json"
    raw = source.read_bytes()
    certificates = json.loads(raw)["witnesses"]
    results = []
    for certificate in certificates:
        h = certificate["h"]
        a, k = (h + 1) // 2, h // 2
        used = set()
        pair_count = 0
        classes = certificate["classes"]
        for chain in classes:
            points = [tuple(v) for v in chain]
            for i, j in points:
                assert 0 <= i < a and 0 <= j < k
                assert (i, j) not in used
                used.add((i, j))
            for (i, j), (ip, jp) in combinations(points, 2):
                assert 0 < jp - j <= ip - i
                horizontal_squared = 16 * (ip - i) ** 2
                for vertical in (2 * (j - ip) + 1, 2 * (jp - i) + 1):
                    norm = horizontal_squared + vertical * vertical
                    root = isqrt(norm)
                    assert not (root < h and root * root == norm)
                pair_count += 1
        assert len(used) == a * k
        assert len(classes) == certificate["colors"]
        assert max(map(len, classes)) == certificate["longest"]
        results.append({"height": h, "classes": len(classes),
                        "labels": len(used), "checked_pairs": pair_count,
                        "status": "PASS"})
    result = {"status": "PASS", "source_sha256": hashlib.sha256(raw).hexdigest(),
              "scope": "finite monotone, Lipschitz-one, strong-P certificates only",
              "certificates": results}
    (here / "continuation_monotone_certificates_check.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
