from pyrogram import Client
import time
import os
import asyncio

try:
    from vars import vars
except:
    print("ENV Vars not defined, Running 'python3 env.py' to define !")
    os.system('python3 env.py')
    from vars import vars

app = Client(
    api_id=vars['API_ID'],
    api_hash=vars['API_HASH'],
    session_string=vars['STRING_SESSION']
)

async def dialogs(ch: int) -> list:
    lis: list = []
    async for x in app.get_dialogs():
        lis.append(x)
    new: list = []
    if ch == 1:
        for x in lis:
            if x.chat.id < 0:
                if x.chat.type.name != 'CHANNEL':
                    new.append(x.chat.id)
    elif ch == 2:
        for x in lis:
            if x.chat.type.name != 'CHANNEL':
                new.append(x.chat.id)
    elif ch == 3:
        for x in lis:
            if x.chat.id > 0:
                new.append(x.chat.id)
    elif ch == 4:
        new = lis
    return new

async def get_target() -> list[int]:
    lis: list = []
    while True:
        print('ENTER YOUR CHOICE: ')
        print('1. Groups')
        print('2. Channels')
        print('3. Users')
        print('4. All')
        print('5. Exit')
        try:
            ch: int = int(input())
            if ch <= 5 or ch >= 1:
                break
            else:
                print('Choice must be from 1-5 !')
        except:
            print('Choice must be an Integer !')
    while True:
        try:
            ex: str = input('Wanna Exclude some chats?, Enter their IDs by seperating them with space else Just click enter.\nExample: 6278637846 728937198\nEnter IDs')
            ex = ex.strip()
            if ex:
                lis: list = list(map(int, ex.split()))
            else:
                lis: list = []
            tar: list = await dialogs(ch)
            for x in lis:
                if x in tar:
                    tar.remove(x)
            lis.clear()
            return tar
        except:
            print('Something Went Wrong, Try again !')

def get_broadcast_info() -> list:
    while True:
        try:
            chat_id: int = int(input("Enter chat id from where messages should be forwarded: "))
            msg_id: int = int(input("Enter message id to be broadcasted: "))
            return [chat_id, msg_id]       
        except:
            print('Must be Integers !')

async def broadcast(users: list[int]):
    inf: list = get_broadcast_info()
    try:
        m = await app.get_messages(inf[0], inf[1])
    except:
        print('Message does not exists or cannot reachable !')
        return
    s: int = 0
    f: int = 0
    print('Starting Broadcast, Close terminal to stop !')
    t: float = 0
    for x in users:
        try:
            await app.forward_messages(x, inf[0], inf[1])
            s += 1
        except:
            f += 1
        if t == 0:
            print(f'Success: {s}\nFailed: {f}\n')
            t = time.time()
        elif int(time.time() - t) >= 3:
            print(f'Success: {s}\nFailed: {f}\n')
            t = time.time()
    print('Broadcasting Done !')
    print(f'Success: {s}\nFailed: {f}\n')
        
async def main():
    await app.start()
    tar: list = await get_target()
    await broadcast(tar)
    await app.stop()

asyncio.run(main())
