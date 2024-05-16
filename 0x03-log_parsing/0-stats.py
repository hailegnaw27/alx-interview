#!/usr/bin/python3
import sys

def parse_line(line):
    # Parse the input line according to the specified format
    # Return IP Address, status code, and file size
    pass

def print_statistics(total_size, status_codes):
    # Print statistics: total file size and number of occurrences of each status code
    pass

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    lines_read = 0

    try:
        for line in sys.stdin:
            # Parse the line
            ip_address, status_code, file_size = parse_line(line.strip())

            # Update metrics
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

            lines_read += 1

            # Print statistics after every 10 lines
            if lines_read % 10 == 0:
                print_statistics(total_size, status_codes)
    except KeyboardInterrupt:
        # Handle keyboard interruption gracefully
        print_statistics(total_size, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()

