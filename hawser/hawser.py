'''
   Tool to check Dockerfiles against a set of rules

   @author: Iain emsley <iain.emsley@kellogg.ox.ac.uk>
'''
import re
import sys

'''
   Definitions
'''

class Hawser():
    '''
       Main functoin for Hawser
    '''

    #define the allowed subset of commands
    allowed_symbols = ['FROM','RUN','MAINTAINER','LABEL']

    #allowed keywords for RUN
    allowed_keywords = ['add-apt-repository', 'apt-get', 'rm']

    #allowed keywords for apt
    allowed_apt = ['install', 'update']

    #define the atoms
    Symbol = str
    Number = float

    def __init__(self, docker_file):
        self.parse_log = []
        self.errors_log = []
        self.docker_file = docker_file

    def evaluate(self):
        '''
           Run the evaluation
        '''
        evaluation = None
        with open(self.docker_file, 'rb') as f:
            data = f.read()
            evaluation = eval_token(read_from_tokens(tokenize(data)))
            f.write(evaluation)
        f.closed

        with open(self.docker_file + "_log.txt", 'wb') as fi:
            fi.write(evaluation)
        fi.closed

        if len(self.errors_log) > 0:
            #write the errors file
            with open('errors.txt', 'wb') as fi:
                fi.write("\n\n".join(self.errors.log))
            fi.closed()

    def read_from_tokens(self, tokens):
        '''
           Construct the AST
        '''
        if len(tokens) == 0:
            self.errors_log.append('No tokens given')
        ast = []
        for token in tokens:
            # remove both comments and empty lines
            if token[0:] == '#' or len(token) == 0:
                continue
            ast.append([token])

        return ast

    def tokenize(self, char):
        '''
         Split file into tokens
         @todo needs work on the spaces
        '''
        return char.replace('\\\n',' ').replace('    ',' ').split('\n')

    def eval_token(self, token):
        '''
           Evaluate the tokens
        '''
        if token[0] is "FROM":
            split_tok = token[1].split(':')
            if len(split_tok) is not 2:
                self.errors_log.append("Incorrect format in FROM")
            if split_tok is "ubuntu" and not str(split_tok[1]).endswith("04"):
                self.errors_log.append("LTS not found in FROM ubuntu")

        elif token[0] is "RUN":
           split_tok = token[1:].split(' ')
           if split_tok[1] in allowed_keywords:
               for t in range(len(split_tok)):
                   #check that apt-get is correct
                   if split_tok[t] is "apt-get" and \
                       split_tok[t+1] not in allowed_apt:
                           self.errors_log.append("apt-get is incorrectly formed")
                   if split_tok[t+1] is "install":
                       #check that the upgrade or install is forced
                       if "-y" not in split_tok[t+1:]:
                           self.errors_log.append("apt-get not forced")
                       #the op is forced and op is installed, check the packages
                       for pkg in split_tok[t+1:].split(' '):
                           #@todo regex this to check on success
                           if '=' not in pkg:
                               self.errors_log.append("Package does not appear to have a version number")
                       
                   #check rm is correct
                   if split_tok[t] is "rm":
                       if split_tok[t+1] is not "-r" or split_tok[t+1] is not "-rf":
                          self.errors_log.append("RM is not forced. ")
                
    def token_rules(self, token, depth=1):
        '''
           Rules from Dockerfile 
           Check that the keywords are correct
        '''
        if depth == 1 and token[0] is not "FROM":
            self.errors_log.append("FROM must be the first keyword")
        else:
            if token[0] not in allowed_keywords:
                self.errors_log.append("Invalid command called ".format(token[0]))
        depth += 1
        token_rules(token[depth:], depth)
