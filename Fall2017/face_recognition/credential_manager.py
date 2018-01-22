import keyring

def set_pass(service, username, password):
    return keyring.set_password(service,username,password)

def get_pass(service, username):
    return keyring.get_password(service, username)

'''
def main():
    print 'Starting the credential manager'
    set_pass("someservice","elijah","elijah_pass")
    print get_pass("someservice", "elijah")

    return

main()
'''
