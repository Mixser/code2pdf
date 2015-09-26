from pygments.lexers import get_lexer_for_filename
from pygments.formatters.latex import LatexFormatter
from pygments.formatters.img import JpgImageFormatter
from pygments import highlight

from tex import latex2pdf

from PIL import Image

from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg, SvgRenderer


import xml.dom.minidom

class Code2Pdf(object):
    def __init__(self, input_file, output_file=None):
        self.__input_file = input_file
        self.__output_file = output_file if output_file else input_file + '.pdf'

    def highlight_file(self):
        lexer = get_lexer_for_filename(self.__input_file)
        formatter = LatexFormatter()
        with open(self.__input_file, 'r') as f:
            content = f.read()

        return highlight(content, lexer, formatter)

    def init_print(self):
        content = self.highlight_file()
        print latex2pdf(content)

def main(filename):
    pass

if __name__ == '__main__':
    c = Code2Pdf("temp.py")

    c.init_print()
