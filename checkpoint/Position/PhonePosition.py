import asyncio
import phonenumbers
from phonenumbers import PhoneNumber
from checkpoint.Position.Position import Position


class PhonePosition(Position):
    def __init__(self, phone_number, phone_obj: phonenumbers.PhoneNumber = None, country_code: str = None):
        super().__init__(country_code=country_code)
        self._phone_number: str = self._adjust_phone_number(phone_number)
        self._phone_obj: PhoneNumber = phone_obj

    @staticmethod
    def _adjust_phone_number(phone_number) -> str:
        phone_number = str(phone_number)

        if '+' not in phone_number:
            phone_number = '+' + phone_number
        return phone_number

    @staticmethod
    def _is_kazakhstan(phone_number) -> bool:
        if phone_number[:3] in ['+76', '+77']:
            return True
        else:
            return False

    async def find_country_code(self) -> str:
        if not self._phone_obj:
            self._phone_obj = phonenumbers.parse(self._phone_number)

        if self._phone_obj.country_code == '+7' and self._is_kazakhstan(self._phone_number):
            self.set_country_code('KZ')  # Kazakhstan, Ukraine loves you, you are not russia

        else:
            country_code = phonenumbers.region_code_for_country_code(self._phone_obj.country_code)

            if country_code in ['ZZ', '001']:
                country_code = 'NAC'  # Not A Country

            self.set_country_code(country_code)

        await asyncio.sleep(0)
        return self._country_code
