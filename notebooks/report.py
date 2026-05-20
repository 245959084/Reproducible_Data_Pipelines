import marimo

__generated_with = "0.11.0"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt

    return pd, plt


@app.cell
def _(pd):
    df = pd.read_csv("data/features/events.csv")

    return df


@app.cell
def _(df, plt):
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.hist(df["duration_minutes"], bins=20)

    ax.set_title("Distribution of Event Durations")
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Count")

    plt.tight_layout()

    fig
    return


if __name__ == "__main__":
    app.run()