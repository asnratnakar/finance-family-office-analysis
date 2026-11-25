from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    forbidden = [".env", "input", "data/api_keys.keys"]
    findings = [item for item in forbidden if (ROOT / item).exists()]
    if findings:
        print("Untracked local-only path present:", ", ".join(findings))
        return 0
    print("No local secret or real-data path found.")
    return 0


if __name__ == "__main":
    raise SystemExit(main())
