[![Coverage Status](https://coveralls.io/repos/github/i386x/vutils-parsing/badge.svg?branch=main)](https://coveralls.io/github/i386x/vutils-parsing?branch=main)
![CodeQL](https://github.com/i386x/vutils-parsing/actions/workflows/codeql.yml/badge.svg)

# vutils-parsing: Grammars, Automata, and Parsing Library

```python
class CLexer(Lexer):
    def __init__(self):
        self.add_rule()

Usage: prog [OPTIONS] COMMAND [ARGS]...

@usage("prog [OPTIONS] COMMAND [ARGS]").where(
    kw_option("template,t", help="")
)

@cmdline(prog + options + command + [args])
@options(
    
)

def foo_option(opt, parser):
    value = parser.consume()
    parser.not_set(opt_set)
    parser.send(opt, value)

options = Options(
    keyval,
    flag,
    switch,
    option("foo|f", action=foo_option),
)

@options(
  common_options(),
  positional("TEMPLATE", "a template"),
)
class Application(BaseCommand):
    def __init__(self):
        BaseCommand.__init__(self, None)
    def main(self, argv):
        self.validate
```
