"""Hello Bounty: a tiny repo for testing the OpenBounty claim, escrow and payout flow."""

import argparse


def greet(name: str | None = None) -> str:
    if name is None or not name.strip():
        return "Hello, World!"
    return f"Hello, {name.strip()}!"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="name to greet")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
