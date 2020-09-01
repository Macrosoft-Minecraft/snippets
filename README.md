# Macrosoft public snippets

Feel free to use this snippets. Fully open source.

Join our community on [Discord](https://discord.gg/u6mWyg6).
Or access our [website](https://macrosoft.site/) to checkout videos and more.
Checkout our IDE/Framework to macros: [Rocket](https://rocket.macrosoft.site/) or watch some [video](https://www.youtube.com/playlist?list=PLMKq-ppHFNmjs4sF2p0uBZomA4CHdPi7J) about this.

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


