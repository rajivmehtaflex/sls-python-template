import numpy as np


def main(event, context):
    foo = np.arange(15).reshape(3, 5)

    print("Your numpy array V1:")
    print(foo)
    # callback(None,foo)

if __name__ == "__main__":
    main('', '')