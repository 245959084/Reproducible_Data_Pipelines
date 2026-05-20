from pathlib import Path
import pandas as pd


INPUT_PATH = Path("data/transformed/events.csv")
OUTPUT_PATH = Path("data/features/events.csv")


def main():
    df = pd.read_csv(INPUT_PATH)

    timestamps = pd.to_datetime(df["timestamp"])

    # duration_minutes feature
    df["duration_minutes"] = (
        df["duration_seconds"] / 60
    )

    # weekday feature
    df["weekday"] = timestamps.dt.day_name()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_PATH, index=False)


if __name__ == "__main__":
    main()