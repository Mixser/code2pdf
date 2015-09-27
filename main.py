import argparse

import sys

from pygments.lexers import get_lexer_for_filename
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

from xhtml2pdf import pisa

__version__ = "0.0.1"


class Code2Pdf(object):
    def __init__(self, input_file, output_file=None):
        self.__input_file = input_file
        self.__output_file = output_file if output_file else input_file + '.pdf'

    def highlight_file(self, linenos):
        lexer = get_lexer_for_filename(self.__input_file)
        formatter = HtmlFormatter(noclasses=True, linenos=linenos)
        try:
            with open(self.__input_file, 'r') as f:
                content = f.read()
        except IOError as exc:
            print exc.message
            sys.exit(1)

        return highlight(content, lexer, formatter)

    def init_print(self, linenos=False):
        content = self.highlight_file(linenos=linenos)
        with open(self.__output_file, "w+b") as out:
            pdf = pisa.CreatePDF(content, dest=out)
        return pdf.err


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Convert given source code into .pdf with syntax highlighting"),
    )

    parser.add_argument(
        "filename",
        help="Absolute path of the source file",
        type=str
    )

    parser.add_argument(
        "outputfile",
        help="absolute path of the output pdf file",
        nargs="?",
        type=str)

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s v. {}".format(__version__))
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    c = Code2Pdf(args.filename, args.outputfile)
    c.init_print()
