# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

import os
import asyncio
from userge import userge


async def worker() -> None:  # pylint: disable=missing-function-docstring
    chat_id = int(os.environ.get("CHAT_ID") or 0)
    await userge.send_message(chat_id, 'testing_userge')


async def main() -> None:  # pylint: disable=missing-function-docstring
    print('starting userge...!')
    await userge.begin(worker())
    print('stopping userge...!')

loop = asyncio.get_event_loop()
print('creating loop...!')
loop.run_until_complete(main())
print('closing loop...!')
loop.close()

print('userge test has been finished!')
