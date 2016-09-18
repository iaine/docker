import sys    
'''
       Takes the docker file as an argument
       Evaluates the file and parses data to a log file
       If it cannot evaluate, creates an error file that is also used to end
       end the process
    '''

    fname = sys.argv[1]
    try:
        evaluation = None
        with open(fname, 'rb') as f:
            data = f.read()
            evaluation = eval_token(read_from_tokens(tokenize(data)))
            f.write(evaluation)
        f.closed

        with open(fname + "_log.txt", 'wb') as fi:
            fi.write(evaluation)
        fi.closed
    except Exception as e:
        with open("error.txt", "wb") as fh:
            fh.write(e)
        fh.closed
