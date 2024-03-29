class TxtLoader:
    def load(self, source):
        """Loads the content of a text file."""
        try:
            with open(source, "r") as file:
                return file.read()
        except FileNotFoundError:
            raise ValueError(f"File not found: {source}")
