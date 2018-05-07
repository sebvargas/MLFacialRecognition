#!/usr/bin/python
import sys
import backend

#todo, import these from backend
LOW_SECURITY = .6
MEDIUM_SECURITY = .5
HIGH_SECURITY = .4

def main():
    '''
    for i in range(1,len(sys.argv)):
        print str(sys.argv[i])
    '''
    output = "output"
    got = sys.argv
    
    if (sys.argv[1] == 'register'):
        username = sys.argv[2]
        img = sys.argv[3]
        if backend.register(username,[img]):
            output = 'success'
        else:
            output = 'register failed'
            
    elif (sys.argv[1] == 'login'):
        imgs = sys.argv[2:]
        if len(imgs) != 3:
            print "error, 3 URIS required, got:", len(imgs)
            return
        username = backend.login(imgs,MEDIUM_SECURITY)
        if not username:
            output = "NONEFOUND "
        else:
            output = username
            print username
    else:
        output = "failed"
    
    with open('backend_out', 'a') as the_file:
            the_file.write(output + '\n')

    with open('debug', 'a') as the_file:
            the_file.write(str(got) + '\n')
            
main()
