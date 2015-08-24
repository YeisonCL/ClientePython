import pycurl, sys, getopt

def getResource(pUrlDirection):
    crawler = pycurl.Curl()
    crawler.setopt(pycurl.URL, pUrlDirection)
    crawler.setopt(pycurl.WRITEFUNCTION, lambda x: None)
    crawler.perform()
    crawler.close()

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:", ["url="])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    for o, a in opts:
        if o in("-u", "--url"):
            urlDirection = a
            getResource(urlDirection)
        else:
            assert False, "Opcion invalida"

if __name__ == "__main__":
    main()
