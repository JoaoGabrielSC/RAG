from argparse import ArgumentParser, Namespace


class Parser:
    def __init__(self) -> None:
        self.parser = ArgumentParser(description="Parser for command line arguments")
        self.add_arguments()

    def add_arguments(self) -> None:
        self.parser.add_argument(
            "--dataset_path", type=str, required=True, help="Path for dataset files"
        )

    def parse(self, args: list[str] | None = None) -> Namespace:
        """
        Here you can pass a list of arguments to parse.
        """
        parse_namespace = self.parser.parse_args(args)

        return parse_namespace
