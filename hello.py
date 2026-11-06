"""Hello Bounty: a tiny repo for testing the OpenBounty claim, escrow and payout flow."""


def greet(name: str | None = None) -> str:
    if name is None or not name.strip():
        return "Hello, World!"
    return f"Hello, {name.strip()}!"


def main() -> None:
    print(greet())


if __name__ == "__main__":
    main()
