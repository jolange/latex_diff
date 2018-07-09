from setuptools import setup


long_desc = """
Create a LaTeX-compilable diff of two LaTeX files.

The main purpose is to produce diffs for documents in the CMS TDR document repository, but it can also be used for any other LaTeX document.

No real LaTeX parsing is performed (and there is no intention to implement this), so the resulting diff file might contain errors that need to be fixed by hand.
"""

setup(name='latex_diff',
      version='0.1dev',
      description='Create a LaTeX-compilable diff of two LaTeX files.',
      long_description=long_desc,
      long_description_content_type='text/markdown',
      url='https://github.com/jolange/latex_diff',
      author='Johannes Lange',
      license='GPL-3.0',
      packages=['latex_diff'],
      scripts=['bin/latex_diff', 'bin/tdr_diff'],
      python_requires='>=3',
      install_requires=['simplediff'])
