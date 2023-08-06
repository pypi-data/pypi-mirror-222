from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

from .pile import Pile


class Parser(object):
    def __init__(self, filename, line_overlap, char_margin, word_margin, line_margin):
        self._document = self._read_file(filename)
        self._device, self._interpreter = self._prepare_tools(line_overlap=line_overlap,
                                                              char_margin=char_margin,
                                                              line_margin=line_margin,
                                                              word_margin=word_margin)
        self._pages = {}

        self._HTML_DEBUG = True

    def extract(self, max_page_num=None):
        for page in PDFPage.create_pages(self._document):
            self._interpreter.process_page(page)
            layout = self._device.get_result()

            if max_page_num != None and layout.pageid > max_page_num:
                break

            self._pages[layout.pageid] = layout

    def parse(self, page_num=None):
        piles = []
        if page_num == None:
            for page_num, page in self._pages.items():
                piles += self._parse_page(page)
        else:
            page = self._pages[page_num]
            piles = self._parse_page(page)
        return piles

    def _read_file(self, filename):
        parser = PDFParser(open(filename, 'rb'))
        document = PDFDocument(parser)
        return document

    def _prepare_tools(self, line_overlap, char_margin, line_margin, word_margin):
        laparams = LAParams(
                line_overlap=line_overlap,
                char_margin=char_margin,
                line_margin=line_margin,
                word_margin=word_margin
        )
        rsrcmgr = PDFResourceManager()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        return device, interpreter

    def _parse_page(self, page):
        pile = Pile()
        pile.parse_layout(page)
        piles = pile.split_piles()
        return piles
