def divide(dividend, divisor):
    return dividend / divisor


#__name__ is a keyword in python that holds the name of the file you are in. When running in the same file __name__ will be __main__
#if this line is executed from another file from an import than __name__ will be the name of this file mymodule
print("mymodule.py", __name__)

import libs.mylib