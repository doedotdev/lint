import argparse
import logging
from pylint.lint import Run

logging.getLogger().setLevel(logging.INFO)

parser = argparse.ArgumentParser(prog="LINT")

parser.add_argument('-p',
                    '--path',
                    help='path to directory you want to run pylint on. %(default)s  %(type)s ',
                    default='./',
                    type=str)

parser.add_argument('-t',
                    '--threshold',
                    help='Foo the program',
                    default=7,
                    type=float)

args = parser.parse_args()
path = str(args.path)
threshold = float(args.threshold)

message = ('PyLint Starting | '
           'Path: {} | '
           'Threshold: {} '.format(path, threshold))

logging.info(message)

results = Run([path], do_exit=False)

final_score = results.linter.stats['global_note']

if final_score < threshold:

    message = ('PyLint Failed | '
               'Score: {} | '
               'Threshold: {} '.format(final_score, threshold))

    logging.error(message)
    raise Exception(message)

else:
    message = ('PyLint Passed | '
               'Score: {} | '
               'Threshold: {} '.format(final_score, threshold))

    logging.info(message)

    exit(0)
