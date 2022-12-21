from telethon import TelegramClient, functions, sync
import config


def open_file(name_file):
    with open(name_file, "r") as file:
        return file.read().split("\n")


async def get_chat():

    client = TelegramClient("Get Chats", config.api_id, config.api_hash)

    client.start()

    old, lst_chat = [], []
    with open("output.txt", "w", encoding="utf-8") as file:
        lst_chat.append("Запуск скрипта...")
        for title in open_file("names.txt"):
            for end in open_file("endings.txt"):
                name = f"{title}{end}"
                lst_chat.append(f"Подбираются чаты найденные по имени:{name}")
                name = name.lower()
                await client.connect()
                request = await client(
                    functions.contacts.SearchRequest(q=name, limit=10)
                )
                for channel in request.chats:
                    if channel.megagroup:
                        username = (
                            channel.username.lower()
                            if channel.username is not None
                            else ""
                        )
                        if username not in old and channel.title not in old:
                            lst_chat.append(f"Найден чат: t.me/{channel.username}")
                            file.write(f"t.me/{channel.username}\n")
                            old.append(channel.username)
                            lst_chat.append(
                                f"Найден чат с подобранным именем:{channel.title}"
                            )

    lst_chat.append("Скрипт завершил свою работу...")
    return lst_chat
