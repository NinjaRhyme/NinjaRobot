﻿# default
config = {
    # data
    'dict_path': 'Data/Dict/Dict.txt',
    'reply_path': 'Data/Reply.json',
    'handler_speed': 0.1,
    'heart_speed': 0.1,

    # login
    'smart_qq_url': 'http://w.qq.com/login.html',
    'qrcode_url': 'https://ssl.ptlogin2.qq.com/ptqrshow?appid={0}&e=0&l=M&s=5&d=72&v=4&t=0.7037167532536932',
    'qrcode_path': './qrcode.jpg',
    'qrcode_login_url': 'https://ssl.ptlogin2.qq.com/ptqrlogin?webqq_type=10&remember_uin=1&login2qq=1&aid={0}&u1=http%3A%2F%2Fw.qq.com%2Fproxy.html%3Flogin2qq%3D1%26webqq_type%3D10&ptredirect=0&ptlang=2052&daid=164&from_ui=1&pttype=1&dumy=&fp=loginerroralert&action=0-0-{1}&mibao_css={2}&t=undefined&g=1&js_type=0&js_ver={3}&login_sig={4}&pt_randsalt=0',
    'qrcode_login2_url': 'http://d1.web2.qq.com/channel/login2',
    'referer': 'http://d1.web2.qq.com/proxy.html?v=20151105001&callback=1&id=2',

    # msg
    'msg_url': 'http://d1.web2.qq.com/channel/poll2',
    'get_vfwebqq_url': 'http://s.web2.qq.com/api/getvfwebqq?ptwebqq={0}&clientid={1}&psessionid={2}&t={3}',
    # user
    'get_self_info_url': 'http://s.web2.qq.com/api/get_self_info2?t={0}',
    'get_uin_info_url': 'http://s.web2.qq.com/api/get_friend_uin2?tuin={0}&type=1&vfwebqq={1}',
    # buddy
    'send_buddy_url': 'http://d.web2.qq.com/channel/send_buddy_msg2',
    # group
    'get_group_list_url': 'http://s.web2.qq.com/api/get_group_name_list_mask2',
    'get_group_info_url': 'http://s.web2.qq.com/api/get_group_info_ext2?gcode={0}&vfwebqq={1}&t={2}',
    'send_group_url': 'http://d.web2.qq.com/channel/send_qun_msg2',

}

def load_config():
    global config
    try:
        with open("Config", 'r') as fin:
            lines = fin.readlines()
            for line in lines:
                words = line.split(' ')
                if type(config[words[0]]) is int:
                    config[words[0]] = int(words[1])
                else:
                    config[words[0]] = words[1]
    except:
        return