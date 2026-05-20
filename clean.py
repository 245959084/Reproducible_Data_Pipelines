from pathlib import Path
import pandas as pd

VALID_EVENT_TYPES = {
    "click",
    "view",
    "purchase",
    "signup",
    "login",
}


INPUT_PATH = Path("data/raw/events.csv")
OUTPUT_PATH = Path("data/clean/events.csv")


def main():
    df = pd.read_csv(INPUT_PATH)

    # Drop rows with missing fields
    df = df.dropna()

    # Keep only valid event types
    df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

    # Ensure positive duration
    df = df[pd.to_numeric(df["duration_seconds"], errors="coerce") > 0]

    # Normalize timestamp to ISO 8601
    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce",
    )

    # Remove invalid timestamps
    df = df.dropna(subset=["timestamp"])

    df["timestamp"] = df["timestamp"].dt.strftime(
        "%Y-%m-%dT%H:%M:%S"
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_PATH, index=False)


if __name__ == "__main__":
    main()