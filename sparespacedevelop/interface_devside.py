def main():
    print "in interface_devside.py"
    with open('tempfile', 'a') as the_file:
        the_file.write("hello ")
    return "in interface_dev!"


main()
