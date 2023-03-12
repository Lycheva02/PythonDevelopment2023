#!/usr/bin/env python3
import asyncio
import cowsay
import shlex

clients = {}

async def chat(reader, writer):
    me = None
    r = asyncio.Queue()
    f = False
    while me not in cowsay.list_cows():
        inpt = await reader.readline()
        inpt = inpt.decode().strip()
        if inpt == 'who':
            writer.write((' '.join([i for i in clients]) + '\n').encode())
            await writer.drain()
        if inpt == 'cows':
            writer.write((' '.join(set(cowsay.list_cows()) - set([i for i in clients])) + '\n').encode())
            await writer.drain()
        if inpt == 'quit':
            f = True
            break	
        if len(inpt.split()) != 2:
            continue
        login, me = inpt.split()
        if login != 'login':
            me = None
    clients[me] = r
    send = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(clients[me].get())
    while not reader.at_eof() and not f:
        done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)
        for q in done:
            if q is send:
                send = asyncio.create_task(reader.readline())
                com = shlex.split(q.result().decode())
                match com:
                    case ['who']:
                        await clients[me].put(' '.join([i for i in clients]))
                    case ['cows']:
                        await clients[me].put(' '.join(set(cowsay.list_cows()) - set([i for i in clients])))
                    case ['say', nm, *txt]:
                        await clients[nm].put(' '.join(txt))
                    case ['yield', *txt]:
                        for i in clients.values():
                            if i is not clients[me]:
                                await i.put(' '.join(txt))
                    case ['quit']:
                        f = True
            else:
                receive = asyncio.create_task(clients[me].get())
                writer.write(f"{q.result()}\n".encode())
                await writer.drain()
    send.cancel()
    receive.cancel()
    print(me, "DONE")
    del clients[me]
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(chat, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())
