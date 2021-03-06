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

from . import tools

import os
import re
import simplediff


def latex_diff_files(fname_old, fname_new, only_body=False):
    with open(fname_old) as f:
        text_old = f.read()
    with open(fname_new) as f:
        text_new = f.read()
    # flatten the contents
    text_old = tools.resolve_inputs(os.path.dirname(os.path.realpath(fname_old)), text_old)
    text_new = tools.resolve_inputs(os.path.dirname(os.path.realpath(fname_new)), text_new)

    if only_body:
        # extract the body
        m = re.search(r'(.*)\\begin{document}(.*)\\end{document}(.*)', text_old, re.MULTILINE | re.DOTALL)
        assert len(m.groups()) == 3, 'wrong document structure!'
        pre_old, text_old, post_old = m.groups()
        m = re.search(r'(.*)\\begin{document}(.*)\\end{document}(.*)', text_new, re.MULTILINE | re.DOTALL)
        assert len(m.groups()) == 3, 'wrong document structure!'
        pre_new, text_new, post_new = m.groups()

    # get rid of diff noise
    text_old, replacements_old = tools.clean_latex(text_old)
    text_new, replacements_new = tools.clean_latex(text_new)

    diff = word_diff(text_old, text_new)
    ldiff = diff_to_latex(diff)

    # reinsert spaces in math
    for repl in replacements_old + replacements_new:
        ldiff = ldiff.replace(repl[1], repl[0])

    if only_body:
        ldiff = pre_new + ldiff + post_new
    return ldiff


def diff_to_latex(diff_list):
    text_blocks = []
    for operation, token_list in diff_list:
        if operation == '=':
            text_blocks += token_list
        elif operation == '-':
            text_blocks.append(r'\color{red}%s\normalcolor{}' % ' '.join(token_list))
        elif operation == '+':
            text_blocks.append(r'\color{green}%s\normalcolor{}' % ' '.join(token_list))
    return ' '.join(text_blocks)


def word_diff(old, new):
    """ similar to simplediff.string_diff, but keeping newlines"""
    return simplediff.diff(old.split(' '), new.split(' '))

