"""
Wimbledon Champions Data Analysis
Estimate: 45 minutes
Actual:   60 minutes
"""


def load_data(filename):
    """Load Wimbledon data from CSV file."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()
    return [line.strip().split(',') for line in lines[1:]]  # Skip header


def get_champions(data):
    """Return dictionary of champions and their win counts."""
    champions = {}
    for row in data:
        name = row[2]  # Champion name column
        champions[name] = champions.get(name, 0) + 1
    return champions