import requests
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str)
    parser.add_argument('--ip', type=str)
    parser.add_argument('--port', type=int, default=5009)
    return parser.parse_args()


def main():
    args = get_args()
    r = requests.post(f"http://{args.ip}:{args.port}/api/american", json={'text': args.text})
    print(r.status_code, r.reason)
    print(r.json())


if __name__ == '__main__':
    main()
