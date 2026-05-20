from pathlib import Path
import pandas as pd

INPUT_PATH = Path("data/raw/events.csv")
OUTPUT_PATH = Path("data/clean/events.csv")


def main():
    df = pd.read_csv(INPUT_PATH)

    # Drop missing values
    df = df.dropna()

    # Normalize event_type (keep only valid ones if needed)
    valid_event_types = {"click", "view", "purchase", "signup", "login"}
    df = df[df["event_type"].isin(valid_event_types)]

    # FIX 1: force numeric conversion properly
    df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")

    # Drop invalid + non-positive durations
    df = df[df["duration_seconds"] > 0]

    # Convert to integer explicitly (important for tests expecting int-like values)
    df["duration_seconds"] = df["duration_seconds"].astype(int)

    # Parse timestamp safely
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])

    df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)


if __name__ == "__main__":
    main()