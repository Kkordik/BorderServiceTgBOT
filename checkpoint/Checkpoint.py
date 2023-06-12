from MyUser import MyUser
from MyChat import MyChat


class Checkpoint:
    type: int

    def __init__(self, my_chat, my_user, fulfilled: bool = None):
        self.my_chat: MyChat = my_chat
        self.my_user: MyUser = my_user
        self.has_passed: bool = fulfilled

    async def check_documents(self) -> bool:
        await self.my_chat.find_requirements()
        await self.my_user.find_phone_position()
        await self.my_user.find_geo_position()
        doc_check_results = [
            self.my_chat.phone_requirement.check_value(value=self.my_user.phone_position.get_country_code()),
            self.my_chat.geo_requirement.check_value(value=self.my_user.geo_position.get_country_code())
        ]

        if True in doc_check_results:
            self.has_passed = True
        else:
            self.has_passed = False

        return self.has_passed
