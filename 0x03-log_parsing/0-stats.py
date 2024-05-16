#!/usr/bin/python3

import re
import sys

def extract_input(input_line):
    patterns = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    log_format = '{}\\-{}{}{}{}\\s*'.format(*patterns)
    match = re.fullmatch(log_format, input_line)
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    if match is not None:
        info['status_code'] = match.group('status_code')
        info['file_size'] = int(match.group('file_size'))
    return info

def print_statistics(total_file_size, status_codes_stats):
    print('Total file size: {:d}'.format(total_file_size))
    for status_code in sorted(status_codes_stats.keys()):
        count = status_codes_stats.get(status_code, 0)
        if count > 0:
            print('{:s}: {:d}'.format(status_code, count))

def update_metrics(line, total_file_size, status_codes_stats):
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']

def run():
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        for line in sys.stdin:
            total_file_size = update_metrics(
                line.strip(),
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)

if __name__ == '__main__':
    run()

