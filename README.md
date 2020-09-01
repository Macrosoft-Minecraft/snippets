# Macrosoft public snippets

Feel free to use this snippets or make a pullrequest. Fully open source.

* Join our community on [Discord](https://discord.gg/u6mWyg6).
* Or access our [website](https://macrosoft.site/) to checkout videos and more.
* Checkout our IDE/Framework to macros: [Rocket](https://rocket.macrosoft.site/) or watch some [video](https://www.youtube.com/playlist?list=PLMKq-ppHFNmjs4sF2p0uBZomA4CHdPi7J) about this.
* Or access the Macrosoft heart 💖: [CloudScript](https://cloudscript.macrosoft.site/) module and webservice.

Special thanks to Gorlem for building the [most awesome docs](https://beta.mkb.gorlem.ml/docs/actions/) for Macromod available ever. We love you.

## How to use python Indenter?
```py
from indenter import Indenter

mylines = [
	'IF(&a==&b);',
	'LOG("yo");',
	'ENDIF;'
]

i = Indenter(lines=mylines)
content = i.indent()

```

## How to use python Minifier?
```py
from minifier import Minifier

mycode = """
	IF(&a==&b);
		LOG("yo");
	ENDIF;
"""

i = Minifier(content=mycode)
content = i.minify(remove_comments=True, inject_collons=True, remove_tabs_and_break_lines=True)

```





