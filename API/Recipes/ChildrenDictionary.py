class ChildrenDictionary(dict):
    """
    Overloaded dictionary for marking purposes
    """

    def __init__(self):
        # whatever here
        super().__init__()

    def __setitem__(self, key: str, value: object):
        # whaterver here for checking
        super().__setitem__(key, value)

    def __getitem__(self, key: str):
        # whatever here for checking
        return super().__getitem__(key)

    def __contains__(self, key: str) -> bool:
        # whatever here
        return super().__contains__(key)

    def __len__(self) -> int:
        return super().__len__()

    def __str__(self) -> str:
        return super().__str__()
