import re

"""
INPUTS
  content = Pure text
OUTPUT
  pure text
"""

class Minifier:

  def __init__(self, content):
    self.content = content
    self.content=self.content.replace('$${','$${;')

  def minify(self, remove_comments=True, inject_collons=True, remove_tabs_and_break_lines=True):
    content = self.remove_comments(content=self.content)
    content = self.inject_collons(content=content)
    content = self.remove_tabs_and_break_lines(content=content)
    return content

  #https://codereview.stackexchange.com/questions/148305/remove-comments-from-c-like-source-code
  def remove_comments(self, content):
    COMMENTS = re.compile(r'''
      ((?<!https:)(?<!http:)//[^\n]*(?:\n|$))    # Everything between // and the end of the line/file
      |                     # or
      (/\*.*?\*/)           # Everything between /* and */
    ''', re.VERBOSE)
    return COMMENTS.sub('\n', content)

  def inject_collons(self, content):
    copy = content
    buffer=''
    for line in content.splitlines():
      p = re.compile(r".*?;[^A-Za-z0-9]*$", re.MULTILINE)
      q = re.compile(r".*(\$\$\{|\}\$\$)[^\w]*$", re.MULTILINE)
      if p.match(line) or q.match(line):
        buffer+=line
      else:
        if re.match('.*[A-Za-z0-9].*',line) and re.match('.*[^${}>][^A-Za-z0-9]*$', line):
          buffer+="{};".format(line)
    return buffer

  def remove_tabs_and_break_lines(self, content):
    return re.sub(r"(?<=;)(\s+)(?=[^\s])", "", content).strip()