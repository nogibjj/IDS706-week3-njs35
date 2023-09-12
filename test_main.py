"""
Various tests for pandas data analysis.
"""
import polars as pl
import os
import main
from polars_script import get_fish_dataframe, get_csv_stats, save_size_relationship_plot


def test_get_fish_dataframe():
    """Test that get_fish_dataframe() returns a DataFrame."""
    assert isinstance(get_fish_dataframe(), pl.DataFrame)


def test_stats_type():
    """Test that get_csv_stats() returns accurate stats."""
    stats_df = get_csv_stats()
    assert int(stats_df["Weight"][2]) == 398
    assert int(stats_df["Length"][2]) == 28
    assert int(stats_df["Weight"][3]) == 357
    assert int(stats_df["Length"][3]) == 10


def test_species_count_plot():
    """Test that save_species_count_plot() is saving a file."""
    main.save_size_relationship_plot()
    assert os.path.isfile("img/size_relationship.png")


def test_main(capsys):
    """Test that main() is printing an output."""
    main.main()
    captured = capsys.readouterr()
    assert captured.out.startswith("Fish statistics")
    assert os.path.isfile("img/size_relationship.png")
    assert os.path.isfile("summary_stats.md")
