import re

"""
INPUTS
  content = Pure text
OUTPUT
  pure text
"""


class Minifier:

  def __init__(self, content):
    self.content = content.replace('$${', '$${;')

  def minify(self, remove_comments=True, inject_collons=True, remove_tabs_and_break_lines=True):
    if(remove_comments):
      self.remove_comments()

    if(inject_collons):
      self.inject_collons()

    if(remove_tabs_and_break_lines):
      self.remove_tabs_and_break_lines()
      
    return self.content

  # https://codereview.stackexchange.com/questions/148305/remove-comments-from-c-like-source-code
  def remove_comments(self):
    COMMENTS = re.compile(r'''
      ((?<!https:)(?<!http:)//[^\n]*(?:\n|$))    # Everything between // and the end of the line/file
      |                     # or
      (/\*.*?\*/)           # Everything between /* and */
    ''', re.VERBOSE)
    self.content = COMMENTS.sub('\n', self.content)

  def inject_collons(self):
    self.content
    buffer = ''
    for line in self.content.splitlines():
      p = re.compile(r".*?;[^A-Za-z0-9]*$", re.MULTILINE)
      q = re.compile(r".*(\$\$\{|\}\$\$)[^\w]*$", re.MULTILINE)
      if p.match(line) or q.match(line):
        buffer += line
      else:
        if re.match('.*[A-Za-z0-9].*', line) and re.match('.*[^${}>][^A-Za-z0-9]*$', line):
          buffer += "{};".format(line)
      self.content = buffer

  def remove_tabs_and_break_lines(self):
    self.content = re.sub(
        r"(?<=;)(\s+)(?=[^\s])", "", self.content).strip()
