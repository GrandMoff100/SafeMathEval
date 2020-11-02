import sys


class Parser:
    OPS = [
        '*',
        '/',
        '+',
        '-'
    ]

    IGNORED = [
        ' ',
        '_',
        '\"',
        '\'',
        '\n'
    ]

    def _parse(self, expr):
        tokens = []
        skipping = False
        stop_index = 0
        for token, index in zip(str(expr), range(len(list(str(expr))))):
            if skipping:
                if index == stop_index + 1:
                    skipping = False
                else:
                    continue
            if token == '(':
                stop_index = expr.rindex(')')
                tokens.append(self._parse(expr[index+1:stop_index]))
                skipping = True
            else:
                if token.isdecimal() \
                or token in self.OPS:
                    tokens.append(token)
                else:
                    if not token in self.IGNORED:  
                        raise SyntaxError(f'\'{token}\' is not a decimal digit, and is not supported.')
        return tokens
    
    def _eval(self, tokens):
        value_string = ''
        for token in tokens:
            if type(token) == str:
                value_string += token
            elif type(token) == list:
                value_string += self._eval(token)
        try:
            return str(eval(value_string))
        except SyntaxError as err:
            raise SyntaxError('There was an Error whilst evaluating your expression.')
    
    def eval(self, expr):
        return self._eval(self._parse(expr))

parser = Parser()

print(*[parser.eval(arg) for arg in sys.argv[1:]], sep=', ')