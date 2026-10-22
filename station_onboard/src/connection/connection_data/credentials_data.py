from dataclasses import dataclass

@dataclass
class CredentialsData:
    username: str
    password: str

# TODO: Consider Pydantic