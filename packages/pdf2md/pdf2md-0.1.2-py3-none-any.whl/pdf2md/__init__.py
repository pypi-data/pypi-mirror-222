import os

from .parser import Parser
from .writer import Writer
from .syntax import BaseSyntax
from .syntax import UrbanSyntax


def convert_pdf_to_markdown(pdf, output, line_overlap=0.5, char_margin=2.0, word_margin=0.1, line_margin=0.5):
    filename = pdf
    title = os.path.splitext(os.path.basename(filename))[0]
    print('Parsing', filename)

    parser = Parser(filename, line_overlap, char_margin, word_margin, line_margin)
    parser.extract()
    piles = parser.parse()

    syntax = UrbanSyntax()

    writer = Writer(output)
    writer.set_syntax(syntax)
    writer.set_mode('simple')
    writer.set_title(title)
    writer.write(piles)

    print('Your markdown is at', writer.get_location())
