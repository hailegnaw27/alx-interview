#!/usr/bin/python3

import sys

def parse_line(line):
    # Implement parsing logic for each line here
    pass

def print_statistics(total_size, status_code_counts):
    # Implement logic to print statistics here
    pass

def main():
    total_size = 0
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    
    try:
        for line in sys.stdin:
            # Process each line using the parse_line function
            # Update total_size and status_code_counts accordingly
            
            # Check if 10 lines have been processed and print statistics
            # Use the print_statistics function
            
    except KeyboardInterrupt:
        # Handle keyboard interruption and print final statistics

if __name__ == "__main__":
    main()

