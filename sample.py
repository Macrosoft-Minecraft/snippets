from indenter import Indenter
from minifier import Minifier

mycode = """
&hello_cloudscript="foo";
#hi_bar="bazz"
@&global_var="foo";
IF(&hello_cloudscript==@&global_var);
LOG("yo")
ENDIF;
"""

# Minify
minifier = Minifier(mycode)
minified_code = minifier.minify(
    remove_comments=True, inject_collons=True, remove_tabs_and_break_lines=True)
print(minified_code)


# Indent
mylines = mycode.split(';')
indenter = Indenter(mylines)
indented_code = indenter.indent()

print(indented_code)
