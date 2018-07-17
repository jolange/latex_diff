# Copyright 2018 Johannes Lange
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import re


def find_included_file(base_path, incname):
    return os.path.join(base_path, incname)


def resolve_inputs(base_path, text):
    still_inputs = False
    for m in re.finditer('\\\\input\{(.*)\}', text):
        still_inputs = True
        inc_statement, incname = m.group(0), m.group(1)
        incname = find_included_file(base_path, incname).strip()
        if not incname.endswith('.tex'):
            incname += '.tex'
        try:
            with open(incname) as f:
                inc_content = f.read()
        except FileNotFoundError:
            inc_content = '!!!input file "%s" not found!!!' % incname
        text = text.replace(m.group(0), inc_content)

    if still_inputs:
        text = resolve_inputs(base_path, text)

    return text


def clean_latex(text):
    # get rid of multiple-spaces/newlines to avoid diff noise
    text = re.sub(' +', ' ', text)
    text = re.sub(r'\n\s*\n', '\n\n', text)

    # remove spaces in inline-math to avoid diffs starting inside

    # exclude comments
    math_texts = text.splitlines()
    math_texts = [l for l in math_texts if not l.startswith('%')]
    math_texts = [l for l in math_texts if r'\RCS' not in l]
    math_texts = '\n'.join(math_texts)
    # find all sequences enclosed by '$' (assuming $ appears only pairwisely)
    math_texts = math_texts.split('$')[1::2]
    replacements = []
    for mt in math_texts:
        mt = '$' + mt + '$'
        mtrep = mt.replace(' ', '')
        replacements.append((mt, mtrep))
        text = text.replace(mt, mtrep)

    text = text.replace('\n', ' %__NEWLINE__% ')
    replacements.append(('\n', ' %__NEWLINE__% '))

    return text, replacements
