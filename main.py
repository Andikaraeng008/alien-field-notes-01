import os

TEXT = "Day two on Earth: everyone carries a tiny sun in their pocket and still stops everything to watch the big one go down. Gorgeous planet, awful signal. Four stars."

# Kit gate: /output/entry.txt must be UTF-8, 1-200 chars, not whitespace-only.
assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "entry violates the 1-200 char gate"


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
