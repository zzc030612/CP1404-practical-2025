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