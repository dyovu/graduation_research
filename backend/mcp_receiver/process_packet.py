import struct

def is_field(name):
    #nameがアルファベットのみで構成されているかどうか
    return name.isalpha()

def deserialize(data, index, length, is_list = False):
    #is_listがtrueならからの[]を生成してそれ以外は辞書を生成する
    #dataにすべてのバイナリーデータが入ってる
    result = [] if is_list else {}
    end_pos = index + length
    while end_pos - index > 8 and is_field(data[index+4:index+8]):
        size = struct.unpack("@i", data[index: index+4])[0] #SMFの構造的に各ブロックの最初の4バイトはそのブロックのデータの中身のバイト数を表す
        index += 4 #dataサイズの4バイト分index加算
        field = data[index:index+4] # fieldは4文字のASCII.そのデータがどんなものかを表す.
        index += 4 #fieldサイズの4バイト分index加算
        value, index2 = deserialize(data, index, size, field in [b"btrs", b"bons"]) # fieldに[b"btrs", b"bons"]があるかどうか
        index = index2
        if is_list:
            result.append(value)
        else:
            result[field.decode()] = value
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
    print("process_packet is worked")
    if "skdf" in data:
        for item in data["skdf"]["bons"]:
            item["bnid"] = struct.unpack("@H", item["bnid"])[0]
            item["pbid"] = struct.unpack("@H", item["pbid"])[0]
            item["tran"] = struct.unpack("@fffffff", item["tran"])
    elif "fram" in data:
        data["fram"]["fnum"] = struct.unpack("@I", data["fram"]["fnum"])[0]
        data["fram"]["time"] = struct.unpack("@I", data["fram"]["time"])[0]
        for item in data["fram"]["btrs"]:
            item["bnid"] = struct.unpack("@H", item["bnid"])[0]
            item["tran"] = struct.unpack("@fffffff", item["tran"])
    return data