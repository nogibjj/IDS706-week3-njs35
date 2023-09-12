"""
This script is an exploration into the polars library.
"""
import os
import polars as pl
import matplotlib.pyplot as plt


def get_fish_dataframe() -> pl.DataFrame:
    """
    Read a CSV file from a URL and return its DataFrame.
    """
    return pl.read_csv("https://github.com/rickiepark/hg-mldl/raw/master/fish.csv")


def get_csv_stats() -> pl.DataFrame:
    """
    Read a CSV file from a URL and return its statistics.
    """
    fish_df = get_fish_dataframe()
    stats = fish_df.describe()
    return stats


def save_size_relationship_plot() -> None:
    """Save a scatter plot of the weight vs length data."""
    fish_df = get_fish_dataframe()
    x, y = fish_df["Weight"], fish_df["Length"]
    weight_length_ratio = x / y
    # Set up figure and axis
    _, ax = plt.subplots()
    # Scatter plot with labels and weight/length ratio as colormap
    sc = ax.scatter(
        x, y, c=weight_length_ratio, cmap="cool", alpha=0.7, label="Fish Data"
    )
    # Add title and labels
    ax.set_title("Weight vs Length Relationship in Fish")
    ax.set_xlabel("Weight")
    ax.set_ylabel("Length")
    # Add colorbar
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label("Weight/Length Ratio")
    # Add grid lines for better readability
    ax.grid(True, linestyle="--", alpha=0.7)

    # Save the figure
    plt.savefig("img/size_relationship.png")


def write_stats_to_markdown() -> None:
    """Write the statistics to a Markdown file."""
    stats = get_csv_stats()
    stats.write_csv("summary_stats.csv")  # Save to a CSV file
    with open("summary_stats.md", "w", encoding="utf-8") as f:
        with open("summary_stats.csv", "r", encoding="utf-8") as csv_file:
            csv_contents = csv_file.readlines()
            headers = csv_contents[0].strip().split(",")
            data = [line.strip().split(",") for line in csv_contents[1:]]
            f.write("| " + " | ".join(headers) + " |\n")
            f.write("| " + " | ".join(["---" for _ in headers]) + " |\n")
            for row in data:
                f.write("| " + " | ".join(row) + " |\n")
    os.remove("summary_stats.csv")  # Delete the CSV file
