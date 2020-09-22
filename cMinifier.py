"""cMinifier.py: Minifies and/or unminifies Macro/Keybind mod code. """

import re

import re
from typing import List, Dict

# TODO: support flags
VARIABLE_TYPES = {
    "&": "string",
    "#": "number"
}

CHARTABLE = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_"


class MacroVariable():

  def __hash__(self):
    return hash(self.__str__())

  def __str__(self):
    return f"{'@' if self.is_global else ''}{self.type}{self.name}"

  def __eq__(self, value):
    if(isinstance(value, MacroVariable)):
      return self.name == value.name and self.type == value.type and self.is_global == value.is_global

    if(isinstance(value, str)):
      return str(self) == value

    return False

  def __init__(self, type: str, name: str, is_global: bool = False):
    if(type not in VARIABLE_TYPES):
      raise Exception(f"unsupported variable type: {type}")

    self.type = type
    self.name = name
    self.is_global = is_global

  def get_pattern(self):
    return f'({self.type})({self.name}(?!\\w))'


class MacroMinifier():
  """
  Minifies the Macro/Keybind mod Code, including variables.
  
  Example use:
    minified_code = MacroMinifier(TEST_CODE).minify()

  if you want the globals to be minified as well, pass "True" to the "minify" function.
  """

  def __init__(self, macro_code):
    self.macro_code: str = str(macro_code).strip().replace('\t', '').replace(
        '\r', '').replace('\n', ';').replace(";;", ';').strip(';')
    self.is_parsed: bool = False
    self.variables: List[MacroVariable] = []
    self.original_minified_map: Dict[MacroVariable, MacroVariable] = {}

  def parse(self):
    """Parses the code into separate statements."""
    #TODO: detect other statements and not only variables.
    self.raw_statements: List[str] = list(s.strip() for s in self.macro_code.split(';'))
    var_regex = re.compile(r"(@?[#&])(\w+)")

    for statement in self.raw_statements:
      match = var_regex.match(statement)
      if(match is None):
        continue

      is_global = match.group(1).startswith('@')
      if(str(match) not in self.variables):
        self.variables.append(MacroVariable(match.group(1)[-1], match.group(2), is_global))

    self.is_parsed = True


  def minify(self, minify_globals: bool=False) -> str:
    """Minifies the code. Parses it if it wasn't parsed before."""

    if(not self.is_parsed):
      self.parse()

    for original in self.variables:
      if((not minify_globals) and original.is_global):
        continue

      self.original_minified_map[original] = MacroVariable(
          original.type, self._generate_unique_key(), original.is_global)

    self.macro_code = ";".join(self.raw_statements)
    for (original, minified) in self.original_minified_map.items():
      # TODO: optimize this
      self.macro_code = self.macro_code.replace(str(original), str(minified))

    return self.macro_code

  # simple base conversion alg (maybe optimizable?)
  def _generate_unique_key(self):
    toReturn: str = ""
    index: int = len(self.original_minified_map)
    if(index == 0):
      toReturn = "a"

    while index:
      toReturn += CHARTABLE[index % len(CHARTABLE)]
      index = int(index / len(CHARTABLE))

    return toReturn

  def beautify(self, map: Dict[MacroVariable, MacroVariable]):
    #TODO: given a map, undo the minifying
    raise NotImplementedError()


if __name__ == "__main__":
  TEST_CODE = """
  &string="teste";
  @&gString="teste";
  #int=0;
  """
  parser = MacroMinifier(TEST_CODE)

  print(parser.minify())
