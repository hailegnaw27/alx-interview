#!/usr/bin/python3
"""
0-island_perimeter.py
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    :param grid: List of list of integers (0 represents water, 1 represents land)
    :return: The perimeter of the island
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                # Start with a perimeter of 4 for the current land cell
                perimeter += 4
                
                # Check the cell above (if it exists and is land)
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Subtract 2 (1 for this cell and 1 for the adjacent cell)

                # Check the cell to the left (if it exists and is land)
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Subtract 2 (1 for this cell and 1 for the adjacent cell)

    return perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

