import struct, datetime

def is_field(name):
    #nameがアルファベットのみで構成されているかどうか
    return name.isalpha()

def deserialize(data, index, length, is_list = False):
    # 初期設定
    #dataにすべてのバイナリーデータが入ってる
    result = [] if is_list else {}
    end_pos = index + length
    while end_pos - index > 8 and is_field(data[index+4:index+8]):
        size = struct.unpack("@i", data[index: index+4])[0] #SMFの構造的に各ブロックの最初の4バイトはそのブロックのデータの中身のバイト数を表す
        index += 4 #dataサイズの4バイト分index加算
        field = data[index:index+4] # fieldは4文字のASCII.そのデータがどんなものかを表す.
        index += 4 #fieldサイズの4バイト分index加算
        value, index2 = deserialize(data, index, size, field in [b"btrs", b"bons"]) # fieldに[b"btrs", b"bons"]があるかどうか　btrs, bonsが来たら辞書じゃなくリストが作られる
        index = index2
        if is_list:
            result.append(value)
        else:
            #ここで配列のkey、最初の4文字をでコードしてる
            result[field.decode()] = value
    # これが実行される時はほぼない
    if len(result) == 0:
        body  = data[index:index+length]
        return body, index + len(body)
    else:
        return result, index

def process_packet(message):
    data = deserialize(message, 0, len(message), False)[0]
    data["head"]["ftyp"] = data["head"]["ftyp"].decode()
    data["head"]["vrsn"] = ord(data["head"]["vrsn"])
    data["sndf"]["ipad"] = struct.unpack("@BBBBBBBB", data["sndf"]["ipad"])
    data["sndf"]["rcvp"] = struct.unpack("@H", data["sndf"]["rcvp"])[0]
    if "skdf" in data:
        for item in data["skdf"]["bons"]:
            item["bnid"] = struct.unpack("@H", item["bnid"])[0]
            item["pbid"] = struct.unpack("@H", item["pbid"])[0]
            item["tran"] = struct.unpack("@fffffff", item["tran"])
    elif "fram" in data:
        data["fram"]["fnum"] = struct.unpack("@I", data["fram"]["fnum"])[0]
        data["fram"]["time"] = struct.unpack("@I", data["fram"]["time"])[0]
        data["fram"]["uttm"] = int(struct.unpack("@d", data["fram"]["uttm"])[0])
        # ここでuttmをUNIX時間からUTC時間の文字列に変換する
        data["fram"]["uttm"] = datetime.datetime.fromtimestamp(data["fram"]["uttm"], datetime.timezone(datetime.timedelta(hours=9)))
        # 文字列変換フォーマット、DBに入れるならdatetime型でいれるから文字列変換入らない
        # data["fram"]["uttm"] = data["fram"]["uttm"].strftime('%Y-%m-%d %H:%M:%S')
        # print(data["fram"]["uttm"])
        for item in data["fram"]["btrs"]:
            item["bnid"] = struct.unpack("@H", item["bnid"])[0]
            item["tran"] = struct.unpack("@fffffff", item["tran"])
    return data