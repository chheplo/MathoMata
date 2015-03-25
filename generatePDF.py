__author__ = 'chheplo'

from pylatex import Document, Section, Subsection, Table, Math, TikZ, Axis, \
    Plot, Figure, Package
from pylatex.numpy import Matrix
from pylatex.utils import italic, escape_latex
import content


def generate_pdf(n_var_repetition, n_var_method_list, n_var_complex_list):
    doc = Document()
    doc.packages.append(Package('geometry', options=['tmargin=2cm',
                                                     'lmargin=2cm',
                                                     'rmargin=1cm']))
    doc.packages.append(Package('array'))
    doc.packages.append(Package('longtable'))
    generate_pages(doc, n_var_repetition, n_var_method_list, n_var_complex_list)
    doc.generate_pdf()


def generate_pages(doc, n_var_repetition, n_var_method_list, n_var_complex_list):
    if sum(n_var_complex_list) is not 0 and sum(n_var_method_list) is not 0 and n_var_repetition is not 0:
        for i in range(len(n_var_method_list)):
            method = n_var_method_list[i]
            if method is not 0:
                for j in range(len(n_var_complex_list)):
                    complexity = n_var_complex_list[j]
                    if complexity is not 0:
                        for k in range(n_var_repetition):
                            # doc = content.generate_content(doc, i, j)
                            doc = content.generate_content2(doc)
                            doc.append(r'\newpage')