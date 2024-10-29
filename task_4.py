import argparse
import sys


sys.argv = ['script_name.py', '5', 'Hello', '--verbose', '--repeat', '3']


def main():
    parser = argparse.ArgumentParser(description='Processing numbers and strings with additional options.')
    parser.add_argument('number', type=int, help='The number to output')
    parser.add_argument('text', type=str, help='Output string')
    parser.add_argument('--verbose', action='store_true', help='Output of additional information')
    parser.add_argument('--repeat', type=int, default=1, help='The number of repetitions of the line')
    args = parser.parse_args()
    if args.verbose:
        print(f'Received arguments: number={args.number}, text="{args.text}", repeat={args.repeat}')
    print(f'Number: {args.number}, String: {args.text * args.repeat}')


if __name__ == '__main__':
    main()