from dataclasses import dataclass


@dataclass
class User:
    id: int
    user_id: int
    username: str
    full_name: str
    has_access: bool
    role: str

@dataclass
class Character:
    id: int
    name: str
    description: str
    role_settings: str
    voice_id: int
    use_count: int


@dataclass
class Keyboard:
    id: int
    text: str
    category: str
    callback: str
    link: str


@dataclass
class Category:
    id: int
    name: str
    description: str
    keyboards: list[Keyboard] | None = None
    use_count: int = None


@dataclass
class Item:
    id: int
    name: str
    description: str
    use_count: int


@dataclass
class Channel:
    id: int
    channel_id: int
    username: str
    link: str
    name: str
    description: str
    use_count: int
