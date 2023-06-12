from MyUser import MyUser
from MyChat import MyChat


class Checkpoint:
    type: int

    def __init__(self, my_chat, my_user, fulfilled: bool = None):
        self.my_chat: MyChat = my_chat
        self.my_user: MyUser = my_user
        self._fulfilled: bool = fulfilled

    def check_documents(self) -> bool:
        pass


class PhoneCheckpoint(Checkpoint):
    def check_documents(self) -> bool:
        pass


class GeoCheckpoint(Checkpoint):
    def check_documents(self) -> bool:
        pass
