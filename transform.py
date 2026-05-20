from pathlib import Path
import pandas as pd


INPUT_PATH = Path("data/clean/events.csv")
OUTPUT_PATH = Path("data/transformed/events.csv")


def main():
    df = pd.read_csv(INPUT_PATH)

    df["date"] = pd.to_datetime(
        df["timestamp"]
    ).dt.strftime("%Y-%m-%d")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_PATH, index=False)


if __name__ == "__main__":
    main()