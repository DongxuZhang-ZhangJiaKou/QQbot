from nonebot import on_command, CommandSession
import requests

__plugin_name__ = '服务器信息'
__plugin_usage__ = r"""
服务器信息

服务器信息
"""

'''
@on_command('weather', aliases=('天气', '天气预报', '查天气'))
async def weather(session: CommandSession):
    # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
    city = session.get('city', prompt='你想查询哪个城市的天气呢？')
    # 获取城市的天气预报
    weather_report = await get_weather_of_city(city)
    # 向用户发送天气预报
    await session.send(weather_report)
'''


@on_command('server_info', aliases=('服务器信息'))
async def send_info(session: CommandSession):
    server = 'test'
    server_Info = await get_server_info(server)
    await session.send(server_Info)


'''
def get_server_info() -> str:
    if str(requests_dict['status']) == 'True':
        requests_dict['status'] = '在线'
    else:
        requests_dict['status'] = '不在线'
    return f'当前状态：' + str(requests_dict['status']) + '\n' + \
           '在线玩家:' + str(requests_dict['current_players']) + '\n' + \
           '版本:' + str(requests_dict['version'])
'''


@send_info.args_parser
async def get_server_info(server: str) -> str:
    url = 'http://8.131.75.227:23333/api/status/new_server_4621000'
    r = requests.get(url)
    requests_dict = r.json()
    if str(requests_dict['status']) == 'True':
        return f'当前状态：' + '在线' + '\n' + \
               '在线玩家:' + str(requests_dict['current_players']) + '\n' + \
               '版本:' + str(requests_dict['version'])
    else:
        return f'服务器炸了'


# async def _(session: CommandSession):


'''
async def get_weather_of_city(city: str) -> str:
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回真实数据的天气 API，并拼接成天气预报内容
    r = requests.get(url + city)
    requests_dict = r.json()

    return f'{city}的温度是:'+'当前温度:'+str(requests_dict['tem'])+'\n'\
           '最高温度：'+str(requests_dict['tem1'])+\
           '最低温度:'+str(requests_dict['tem2'])+'\n'+\
           '风向：'+str(requests_dict['win'])+\
           '能见度:'+str(requests_dict['visibility'])
'''
