from intrepyd.iec611312py.translator import translate

def main():
    translate('tests/openplc/simple1.xml', 'encoding.py')

if __name__ == "__main__":
    main()
