import argparse
import base64

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--e', type=str, default=None, required=False)
    parser.add_argument('--d', type=str, default=None, required=False)
    args = parser.parse_args()
    if args.e is not None and args.d is None:
        stE = args.e.encode()
        res = base64.b64encode(stE)
        print(res.decode())
    elif args.e is None and args.d is not None:
        stD = base64.b64decode(args.d)
        print(stD.decode())

