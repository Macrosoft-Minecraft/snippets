import re

"""
Inputs 
lines = a list of lines

Example usage:

l = ['IF(&a==&b);','LOG("Yo");','ENDIF;']
i = Indenter(lines=l)
content = i.indent()
"""

class Indenter:
  def __init__(self, lines):
    self.lines = lines
    self.level = []
    self.indentation = 0
    self.statements = [('IF','ELSEIF'),
                       ('IF','ELSE'),
                       ('IF','ENDIF'),
                       ('ELSEIF','ELSEIF'),
                       ('ELSEIF','ENDIF'),
                       ('ELSEIF','ELSE'),
                       ('ELSE','ENDIF'),
                       ('IFMATCHES','ELSE'),
                       ('IFMATCHES','ENDIF'),
                       ('IFMATCHES','ELSEIF'),
                       ('IFBEGINSWITH','ELSE'),
                       ('IFBEGINSWITH','ENDIF'),
                       ('IFBEGINSWITH','ELSEIF'),
                       ('IFENDSWITH','ELSE'),
                       ('IFENDSWITH','ENDIF'),
                       ('IFENDSWITH','ELSEIF'),
                       ('IFCONTAINS','ELSE'),
                       ('IFCONTAINS','ENDIF'),
                       ('IFCONTAINS','ELSEIF'),
                       ('FOR','NEXT'),
                       ('FOREACH','NEXT'),
                       ('DO','UNTIL'),
                       ('DO','WHILE'),
                       ('DO','LOOP'),
                       ('UNSAFE','ENDUNSAFE'),
                       ('$${','}$$')]

  def check_closing(self, line):
    """
      return <statement> if line close statement otherwise None
    """
    result = None
    if len(self.level):
      for statement in self.statements:
        current_level = self.level[len(self.level) - 1]["statement"]
        match = re.match(r'^[ \t\n\n]*({})\b.*'.format(statement[1]), line, re.IGNORECASE)
        if match is not None:
          groups = match.groups()
          if current_level.lower() == statement[0].lower() and len(groups) and groups[0].lower() == statement[1].lower():
            result = statement[1]
    return result

  def check_opening(self, line):
    """
      return <statement> if line open statement otherwise None
    """
    result = None
    for statement in self.statements:
      match = re.match(r'^[ \t\n\n]*({})\b.*'.format(statement[0]), line, re.IGNORECASE)
      if match is not None:
        groups = match.groups()
        if len(groups) and groups[0].lower() == statement[0].lower():
          result = statement[0]
    return result

  def indent(self):
    """

      Iterates line L

      Line L matches to the current level closing?
        yes: closes the current level and reduces the indent
      Apply indentation to line that matches the current level
      Line L matches to the current level opening?
        yes: open a level, increase the indent

      Add line to buffer

    """
    indented_lines = []
    for index, line in enumerate(self.lines): 

      #print(line)

      checking = self.check_closing(line)
      if checking is not None:
        #print("closing {}".format(checking))
        self.level.pop()
        self.indentation -= 1

      indented_line = "{}{}".format('\t' * self.indentation, line.strip(' \n\t\r'))

      checking = self.check_opening(line)
      if checking is not None:
        #print("opening {}".format(checking))
        self.level.append({"statement": checking, "index": index})
        self.indentation += 1

      indented_lines.append(indented_line)

    indented_lines = ["{};".format(i) for i in indented_lines if i]
    #print(indented_lines)
    #print(self.level)

    if len(self.level):
      raise Exception("Code not balanced! Forget closing some block? Invalid build!")

    return '\n'.join(indented_lines).replace("$${;","$${").replace("}$$;","}$$") #simple adjustment

  def __str__(self):
    return self.content





