import json

from pydantic import BaseModel

from AndroidQQ.proto import *

from AndroidQQ.Tcp import *

import AndroidQQ.package.OidbSvc as OidbSvc
import AndroidQQ.package.StatSvc as StatSvc
from AndroidQQ.package.head import *


class info_model(BaseModel):
    class device(BaseModel):
        app_id: int = None
        IMEI: bytes = None
        var: bytes = None
        Guid_md5: bytes = None

    class UN_Tlv_list(BaseModel):
        T10A_token_A4: bytes = None
        T143_token_A2: bytes = None

    uin: str = None
    uin_bytes: bytes = None
    seq: int = 5267
    share_key: bytes = None
    UN_Tlv_list: UN_Tlv_list
    device: device


class AndroidQQ:
    def __init__(self):
        self._tcp = start_client('198.18.1.229', 8080, self.UN_data)
        self.pack_list = {}
        self.info = info_model()
        IMEI = '866174040000000'
        self.info.device.app_id = 537119623
        self.info.device.IMEI = bytes(IMEI, 'utf-8')
        self.info.device.var = bytes(IMEI, 'utf-8')

    def Set_TokenA(self, data):
        json_data = json.loads(data)
        uin = json_data['UIN']
        self.info.uin = str(json_data['UIN'])
        self.info.uin_bytes = self.info.uin.encode('utf-8')
        self.info.UN_Tlv_list.T10A_token_A4 = bytes.fromhex(json_data['token_A4'])
        self.info.UN_Tlv_list.T143_token_A2 = bytes.fromhex(json_data['token_A2'])
        self.info.share_key = bytes.fromhex(json_data['Sharekey'].replace(' ', ''))
        self.info.device.Guid_md5 = bytes.fromhex(json_data['GUID_MD5'])

    def UN_data(self, data):
        """解包"""
        pack = pack_u(data)
        pack.get_int()
        pack_way = pack.get_byte()

        pack.get_byte()  # 00
        _len = pack.get_int()
        pack.get_bin(_len - 4)  # Uin bin
        _data = pack.get_all()
        if pack_way == 2:
            _data = TEA.decrypt(_data, '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00')
        elif pack_way == 1:
            _data = TEA.decrypt(_data, self.info.share_key)
        else:
            _data = b''
            print('未知的解密类型')

        if _data == b'':
            return
        else:
            pack = pack_u(_data)
            _len = pack.get_int()
            part1 = pack.get_bin(_len - 4)
            _len = pack.get_int()
            part2 = pack.get_bin(_len - 4)
            # part1
            pack = pack_u(part1)
            ssoseq = pack.get_int()
            pack.get_int()
            pack.get_int()
            _len = pack.get_int()
            Cmd = pack.get_bin(_len - 4).decode('utf-8')
            if ssoseq > 0:
                print('包序号', ssoseq, '包类型', Cmd, part2.hex())
                self.pack_list.update({ssoseq: part2})
            else:
                print('推送包', '包类型', Cmd, part2.hex())

    def Tcp_send(self, data):
        self._tcp.sendall(data)
        start_time = time.time()  # 获取当前时间
        ssoseq = self.info.seq
        while time.time() - start_time < 3:  # 检查是否已过去三秒
            data = self.pack_list.get(ssoseq)
            if data is not None:
                break
            time.sleep(0.1)
        self.info.seq = ssoseq + 1

        return data

    def no_tail_login(self):
        """无尾登录包"""
        data = OidbSvc.P_0x88d_1(self.info)
        data = self.Tcp_send(data)
        data = OidbSvc.P_0x88d_1_res(data)
        return data

    def get_dev_login_info(self, **kwargs):
        """
           获取设备登录信息。
               **kwargs: 可变数量的关键字参数，包括：
                   type (int): 设备类型。1 表示在线设备，2 表示离线设备，3 表示全部设备。默认为 3。

           Returns:
               返回获取到的设备登录信息。
           """
        data = StatSvc.GetDevLoginInfo(self.info, **kwargs)
        data = self.Tcp_send(data)
        data = StatSvc.GetDevLoginInfo_res(data)
        return data
