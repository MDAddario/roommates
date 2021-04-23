# Roommates

`roommates` helps you figure out equalization payments

## Installation

```
pip install roommates
```

## Usage

```
from roommates import split

# Register all previous payments
ribs = {
    'Alice': 50.00,
    'Bob':   30.40,
    'Eve':    0.00,
}

ice_cream = {
    'Bob': 20.00,
    'Eve': 15.00,
}

# Print equalization payments
split(ribs, ice_cream)
```

## Concerns

For any concerns, please email michael [dot] lindner [dot] daddario [at] gmail [dot] com
