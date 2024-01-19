```

import asyncio, os, time, aiohttp
import aiohttp
from pyrogram import filters
from daxxhub import daxxhub as papadaxx
from DAXXMUSIC import app

@app.on_message(filters.command("daxxhub"))
async def daxxhub(_, message):
    text = message.text[len("/daxxhub") :]
    papadaxx(f"{text}").save(f"daxxhub_{message.from_user.id}.png")
    await message.reply_photo(f"daxxhub_{message.from_user.id}.png")
    os.remove(f"daxxhub_{message.from_user.id}.png")

```
```
sh pip install daxxhub

```




# DAXXHUB 


![Project Image](https://github.com/DAXXTEAM/daxxhub/blob/main/out.png)

