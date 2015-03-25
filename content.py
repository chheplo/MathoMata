__author__ = 'chheplo'

from pylatex import Document, Section, Subsection, Table, Math, TikZ, Axis, \
    Plot, Figure, Package
from pylatex.numpy import Matrix
from pylatex.utils import italic, escape_latex


def generate_content(doc, i, j):
    if i is 0 and j is 0:
        pass

    return


def generate_content2(doc):
    with doc.create(Table('p{0.1cm} p{4cm} p{0.1cm} p{4cm} p{0.1cm} p{4cm} p{0.1cm} p{4cm}')) as table:
        table.add_empty_row()
        table.add_empty_row()
        table.add_empty_row()
        table.add_row(("", 1733, "", 345, "", 456, "", 23234))
        table.add_row(("+", "", "+", "", "+", "", "+", ""))
        table.add_row(("", 1223, "", 345, "", 456, "", 23234))
        table.add_row(("", "------", "", "-----", "", "-----", "", "--------"))
        table.add_empty_row()
        table.add_empty_row()
        table.add_empty_row()

        table.add_empty_row()
        table.add_empty_row()
        table.add_empty_row()
        table.add_row(("", 1233, "", 345, "", 456, "", 23234))
        table.add_row(("+", "", "+", "", "+", "", "+", ""))
        table.add_row(("", 1223, "", 345, "", 456, "", 23234))
        table.add_row(("", "------", "", "-----", "", "-----", "", "--------"))
        table.add_empty_row()
        table.add_empty_row()
        table.add_empty_row()

        table.add_empty_row()
        table.add_empty_row()
        table.add_empty_row()
        table.add_row(("", 1233, "", 345, "", 456, "", 23234))
        table.add_row(("+", "", "+", "", "+", "", "+", ""))
        table.add_row(("", 1223, "", 345, "", 456, "", 23234))
        table.add_row(("", "------", "", "-----", "", "-----", "", "--------"))
        table.add_empty_row()
        table.add_empty_row()
        table.add_empty_row()

        table.add_empty_row()
        table.add_empty_row()
        table.add_empty_row()
        table.add_row(("", 1233, "", 345, "", 456, "", 23234))
        table.add_row(("+", "", "+", "", "+", "", "+", ""))
        table.add_row(("", 1223, "", 345, "", 456, "", 23234))
        table.add_row(("", "------", "", "-----", "", "-----", "", "--------"))
        table.add_empty_row()
        table.add_empty_row()
        table.add_empty_row()

        table.add_empty_row()
        table.add_empty_row()
        table.add_empty_row()
        table.add_row(("", 1233, "", 345, "", 456, "", 23234))
        table.add_row(("+", "", "+", "", "+", "", "+", ""))
        table.add_row(("", 1223, "", 345, "", 456, "", 23234))
        table.add_row(("", "------", "", "-----", "", "-----", "", "--------"))
        table.add_empty_row()
        table.add_empty_row()
        table.add_empty_row()
        return doc