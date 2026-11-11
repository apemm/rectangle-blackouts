"""Build the single-file export blackouts_enumeration.tex from main.tex.

Each \\input{...} in main.tex is replaced by the contents of that file, recursively. The
\\bibliographystyle and \\bibliography lines are replaced by main.bbl, which BibTeX writes
from enumeration.bib with jis.bst. Run pdflatex and bibtex on main.tex first. Comment lines
are dropped, since the journal asks for a file without % comments.

Usage, from this folder:
    py make_single_file.py
The output uses LF line endings.
"""

import os
import re
import sys

BS = chr(92)
PAT = re.compile(re.escape(BS + 'input{') + r'([^}]+)\}')
HERE = os.path.dirname(os.path.abspath(__file__))


def read(path):
    with open(os.path.join(HERE, path), encoding='utf-8', newline='') as fh:
        return fh.read().replace('\r\n', '\n')


def expand(text):
    def rep(mo):
        name = mo.group(1)
        if not name.endswith('.tex'):
            name += '.tex'
        return expand(read(name)).rstrip('\n')
    return PAT.sub(rep, text)


def main():
    text = expand(read('main.tex'))
    bib = BS + 'bibliographystyle{jis}\n' + BS + 'bibliography{enumeration}'
    if bib not in text:
        sys.exit('bibliography lines not found')
    text = text.replace(bib, read('main.bbl').rstrip('\n'))
    lines = [ln for ln in text.split('\n') if not ln.lstrip(' \t').startswith('%')]
    text = '\n'.join(lines)
    if '%' in text.replace(BS + '%', ''):
        sys.exit('an unescaped % is left in the output')
    target = os.path.join(HERE, 'blackouts_enumeration.tex')
    with open(target, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)
    print('wrote', target)


if __name__ == '__main__':
    main()
