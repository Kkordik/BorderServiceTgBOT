import asyncio
from MyUser import UsersTable
from MyChat import ChatsTable
from config import HOST, USER, PASSWORD, NAME, PORT
from Table import Database


async def run_db(_loop, host, user, password, name, port) -> Database:
    _db = Database(host, user, password, name, port)
    await _db.make_pool(_loop)
    return _db


if __name__ == "run_db":
    # Register database and pool
    loop = asyncio.get_event_loop()
    db: Database = loop.run_until_complete(run_db(loop, HOST, USER, PASSWORD, NAME, PORT))

    # Register tables
    USERS_TB = UsersTable(db)
    CHATS_TB = ChatsTable(db)
