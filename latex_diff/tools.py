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
    # TODO repeat until finished
    for m in re.finditer('\\\\input\{(.*)\}', text):
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
    return text

