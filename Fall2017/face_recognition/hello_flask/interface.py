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
        if len(imgs) != 1:
            print "error, 1 URIS required, got:", len(imgs)
            return
        if backend.register(username,imgs[0]):
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
    else:
        output = "failed"
    
    with open('backend_out', 'a') as the_file:
            the_file.write(output)

    with open('debug', 'w') as the_file:
            the_file.write(got)
            
main()
