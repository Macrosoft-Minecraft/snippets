from indenter import Indenter
from minifier import Minifier

mycode = """
IF(&a==&b);
LOG("yo");
ENDIF;
"""

## Minify
i = Minifier(content=mycode)
content = i.minify(remove_comments=True, inject_collons=True, remove_tabs_and_break_lines=True)
print(content)


## Indent
mylines =  content.split(';')
i = Indenter(lines=mylines)
content = i.indent()

print(content)