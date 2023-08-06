from typing import Dict, Mapping


class DataKey(Dict[str, str]):
    def __init__(self, **kwargs):
        props = {k: str(v) for k, v in kwargs.items()}
        super().__init__(**props)

    def __hash__(self):
        return hash(tuple(sorted(self.items())))

    def __eq__(self, other):
        if isinstance(other, Mapping):
            return dict(self) == dict(other)

    def __repr__(self):
        return f"DataKey({', '.join([f'{k}={v}' for k, v in self.items()])})"
