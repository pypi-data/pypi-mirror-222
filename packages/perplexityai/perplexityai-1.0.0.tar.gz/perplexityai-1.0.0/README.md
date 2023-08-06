# PerplexityAI

A better, simpler, and faster version of nathanrchn's PerplexityAI.

## Get started:

```
python -m pip install -U perplexityai
```

Join my [Discord server](https://discord.gg/XH6pUGkwRr) for live chat, support, or if you have any issues with this package.

## Support this repository:
- ⭐ **Star the project:** Star this repository. It means a lot to me! 💕
- 🎉 **Join our Discord Server:** Try the bot and chat with others. [Join here](https://discord.gg/XH6pUGkwRr):

[![DiscordWidget](https://discordapp.com/api/guilds/1120833966035976273/widget.png?style=banner2)](https://discord.gg/XH6pUGkwRr)

## Example:

```python
import perplexityai
from asyncio import run


async def main():
    while True:
        prompt = input("👦: ")
        try:
            resp = await perplexityai.Completion.create(prompt)
            print(f"🤖: {resp}")
        except Exception as e:
            print(f"🤖: {e}")


run(main())
```
