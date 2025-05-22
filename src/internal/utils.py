from pathlib import Path

class ResolverPath:
    def __init__(self) -> None:
        self.ROOT_DIR = Path().absolute()
        self.SRC_DIR = self.ROOT_DIR / "src"
        self.TEMP_DIR = self.SRC_DIR / "_temp"
        self.INTERNAL_DIR = self.SRC_DIR / "internal"
        self.ANALYZER_DIR = self.INTERNAL_DIR / "analyzer"