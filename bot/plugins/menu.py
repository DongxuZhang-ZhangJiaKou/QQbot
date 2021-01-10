from nonebot import on_command, CommandSession


@on_command('menu', aliases='菜单')
async def menu(session: CommandSession):
    await session.send('服务器信息(显示pacman破服务器的状态)' + '\n' +
                       '天气(由于pacman没钱用的是免费的api，bug若干正在修复)')
