"""
Utilities shared among the tools
"""

def check_file_exists(filename):
    """Checks if a file exists"""
    try:
        open(filename, 'r')
    except IOError:
        print 'Error: ', filename, 'does not exists'
        sys.exit(1)
