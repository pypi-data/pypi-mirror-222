import argparse
import spreadsheet
import sniper.engine

parser = argparse.ArgumentParser(description='delete resources across regions in AWS', prog='Sniper',epilog='Sniper, by Parallelz')
parser.add_argument('-d', '--delete', action='store_true', default=False, help='actually delete the resource (rather than dry-run, which is default)')
parser.add_argument('-f', '--file', help="a CSV file with columns Identifier, Type, and Region")
args = parser.parse_args()

if args.file == None:
    parser.print_help()
    exit(0)

rows = spreadsheet.fileToRows(args.file)

sniper.engine.process(rows, args)
