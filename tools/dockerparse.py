import sys

#define the allowed subset of commands
allowed_symbols = ['FROM','RUN','MAINTAINER','LABEL']

#allowed keywords for RUN
allowed_keywords = ['add-apt-repository', 'apt-get', 'rm']

#alloweed keywords for apt
allowed_apt = ['install', 'upgrade', 'update']

#define the atoms
Symbol = str
Number = float

def read_from_tokens(tokens):
    '''
       Construct the AST
    '''
    if len(tokens) == 0:
        raise Exception('No tokens given')
    ast = []
    for token in tokens:
        # remove both comments and empty lines
        if token[0:] == '#' or len(token) == 0:
            continue
        ast.append([token])

    return ast

def tokenize(char):
   '''
     Split file into tokens
     @todo needs work on the spaces
   '''
   return char.replace('\\\n',' ').replace('    ',' ').split('\n')

def eval_token(token):
    '''
       Evaluate the tokens
    '''
    if token[0] is "FROM":
        split_tok = token[1].split(':')
        if len(split_tok) is not 2:
            raise Exception("Incorrect format in FROM")
        if split_tok is "ubuntu" and not str(split_tok[1]).endswith("04"):
            raise Exception("LTS not found in FROM ubuntu")

    elif token[0] is "RUN":
       split_tok = token[1:].split(' ')
       if split_tok[1] in allowed_keywords:
           for t in range(len(split_tok)):
               #check that apt-get is correct
               if split_tok[t] is "apt-get" and \
                   split_tok[t+1] not in allowed_apt:
                       raise Exception("apt-get is incorrectly formed")
               if split_tok[t+1] is "upgrade" or split_tok[t+1] is "install" and "-y" not in split_tok[t+1:]:
                       raise Exception("apt-get not forced")
               #check rm is correct
               if split_tok[t] is "rm":
                   if split_tok[t+1] is not "-r" or split_tok[t+1] is not "-rf":
                      raise Exception("RM is not forced. ")
                
def token_rules(token, depth=1):
    '''
       Rules from Dockerfile 
       Check that the keywords are correct
    '''
    if depth == 1 and token[0] is not "FROM":
        raise Exception("FROM must be the first keyword")
    else:
        if token[0] not in allowed_keywords:
            raise Exception("Invalid command called ".format(token[0]))
    depth += 1
    token_rules(token[depth:], depth)

if __name__ == '__main__':
    fname = sys.argv[1]
    try:
        with open(fname, 'rb') as f:
            data = f.read()
            print(eval_token(read_from_tokens(tokenize(data))))
        f.closed
    except Exception as e:
        printf("parsing exception %s"%e)
