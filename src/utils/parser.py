from argparse import ArgumentParser


class Parser:
    def __init__(self):
        self.parser = ArgumentParser(description="Parser for command line arguments")
        self.add_arguments()

    def add_arguments(self):
        self.parser.add_argument(
            "--dataset_path", type=str, required=True, help="Path for dataset files"
        )

    def parse(self):
        return self.parser.parse_args()
