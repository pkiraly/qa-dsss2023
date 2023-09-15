from jsonschema import Draft202012Validator
from json import load
import getopt, sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:i:", ["help", "schema=", "instances="])
    except getopt.GetoptError as err:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    
    schemaFile = None
    instanceFile = None
    for key, value in opts:
        if key in ("-h", "--help"):
            usage()
            sys.exit()
        elif key in ("-s", "--schema"):
            schemaFile = value
        elif key in ("-i", "--instances"):
            instanceFile = value
        else:
            assert False, "unhandled option"

    if (schemaFile is None or instanceFile is None):
        print("Missing input file(s)")
        usage()
        sys.exit()

    with open(schemaFile) as f:
        schema = load(f)

    with open(instanceFile) as f:
        instances = load(f)

    validator = Draft202012Validator(schema)
    for error in validator.iter_errors(instances):
        if len(error.path) == 0:
            print(error.message)
        elif len(error.path) == 1:
            print('Error in "%s" property: %s' % (error.path[0], error.message))
        else:
            print('Error in "%s" property of instance #%s: %s' % (error.path[1], error.path[0], error.message))
        

def usage():
    print("usage: %s -h|--help -s|--schema <JSON schema file> -i|--instances <file with JSON instances>" % sys.argv[0])

if __name__ == "__main__":
    main()
