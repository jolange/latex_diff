Create a LaTeX-compilable diff of two LaTeX files.

The main purpose is to produce diffs for documents in the [CMS TDR document repository](https://twiki.cern.ch/twiki/bin/view/CMS/Internal/TdrProcessing), but it can also be used for any other LaTeX document.

No real LaTeX parsing is performed (and there is no intention to implement this), so the resulting diff file might contain errors that need to be fixed by hand.

Copyright 2018 Johannes Lange (see LICENSE.txt)

## Installation
- requires python3 and simplediff

- install development version from git:
```
git clone git@github.com:jolange/latex_diff.git
pip install [-e] .
```

## Usage
- note that your LaTeX document has to use the `xcolor` package to display the diff markup

TODO
![Example output](img/example1_diff.png "Example output")

