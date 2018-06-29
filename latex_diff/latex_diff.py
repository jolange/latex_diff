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

import simplediff


def diff_to_LaTeX(diff_list):
    text_blocks = []
    for operation, token_list in diff_list:
        if operation == '=':
            text_blocks += token_list
        elif operation == '-':
            text_blocks.append(r'\textcolor{red}{%s}' % ' '.join(token_list))
        elif operation == '+':
            text_blocks.append(r'\textcolor{green}{%s}' % ' '.join(token_list))
    return ' '.join(text_blocks)


def word_diff(old, new):
    """ similar to simplediff.string_diff, but keeping newlines"""
    return simplediff.diff(old.split(' '), new.split(' '))

