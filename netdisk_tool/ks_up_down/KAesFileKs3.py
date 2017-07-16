#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import hashlib
from encrypt_key import global_encrypt_key

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(0) 
unpad = lambda s : s[0:-ord(s[-1])]
s_ivec = 'kfile@kingsoft.c'
INDEX_ARR[] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
SPECIAL_CHARS = "-!~@#$%^&*()"
CHARACTER_ARR = "-!~@#$%^&*()0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# 将字符串转换成二进制的buff块
def parse_hex(hex_str):
    l=int(math.ceil(len(hex_str)/2))
    buf=''
    for i in range(0,l):
        s=hex_str[(i*2):((i+1)*2)]
        buf=buf+chr(int(s,16))
    return buf

def encrypt_data(raw_buf,key_hex,iv_hex):
   # 解析加密的key
    key = parse_hex(key_hex)
    iv = parse_hex(iv_hex)

    # 新建一个AES的对象
    aes_obj = AES.new(key, AES.MODE_CBC,iv)

    # padding算法
    defdding_zero=pad(raw_buf)

    # 开始加密
    encrypt_buf=aes_obj.encrypt(padding_zero)
    return encrypt_buf


def decrypt_data(encrypt_buf,key_hex,iv_hex):
   # 解析加密的key
    key = parse_hex(key_hex)
    iv = parse_hex(iv_hex)

    # 新建一个AES的对象
    aes_obj = AES.new(key, AES.MODE_CBC,iv)

    # padding算法
    defdding_zero=pad(raw_buf)

    # 解密
    buff=aes_obj.decrypt(encrypt_buf)
    return buff

def calc_sha1(str_in):
     sha1 = hashlib.sha1()
     sha1.update(str_in)
     strSha1 = sha1.hexdigest()
     return strSha1

def kk_gen2_ex(client_key,timestamp,xid,domain_id,user_xid):
    raw_str_1 = '%s\nTIME:%u\nXID:%u\nDOMAIN:%u\nUSER:%u\n'%(client_key,timestamp,xid,domain_id,user_xid)
    raw_str_2 = '%s\nUSER:%u\nDOMAIN:%u\nXID:%u\nTIME:%u\n'%(user_xid,domain_id,xid,timestamp,client_key)
    ret_key = [0 for x in range(0,2048)]
    sha1_1_str_len = len(raw_str_1)
    sha1_2_str_len = len(raw_str_2)
    sha1_1_str =  raw_str_1
    sha2_1_str =  raw_str_2
    special_len = len(SPECIAL_CHARS)
    digit = 0
    number = 0
    count  = 0
    j = 0
    for i in rane(0,16):
	tc = sha1_1_str[INDEX_ARR[i]%sha1_1_str_len]
	if (tc <= ord('9') && tc >= ord('0')):
	     digit +=1
	     number = tc - ord('0');
	     count += number;
	     if (digit >= 3):
		tc = ord('A') + number
		digit = 0
	    elif (count >= 4):
		tc = SPECIAL_CHARS[(number+INDEX_ARR[i])%special_len]
		count = 0
	ret_key[j] = tc
	j += 2

    j = 1
    for i in rane(0,16):
	tc = sha1_2_str[sha1_2_str_len-INDEX_ARR[i]%sha1_2_str_len]
	if (tc <= ord('z') && tc >= ord('a')):
	    count += (tc - ord('a'))
	    if (count >= j):
		tc = ord('A') + (((tc ^ INDEX_ARR[i]) & 0X3F) % (ord('Z') - ord('A'))
		count=i
	ret_key[j] = tc
	j += 2

     ret_key[32] = ord('\0')
     return ret_key

def HexDecodToByteBuffer(hexString,countOfBytes):
    pByteBuffer = [0 for x in range(0,countOfBytes)]
    for i in range(0,countOfBytes):
	szOneByte = [0 for x in range(0,3)]
	szOneByte[0] = pHexString[i * 2]
	szOneByte[1] = pHexString[i * 2 + 1]
	oneByte = int(szOneByte,16)
	pByteBuffer[i] = oneByte
    return pByteBuffer

def DecryptHexKKey(strServHexKey,dynamic_key,dynamic_ivec):
    fsize = len(strServHexKey)/2
    buffer = HexDecodToByteBuffer(strServHexKey,fsize)
    outdata = decrypt_data(buffer,dynamic_key,dynamic_ivec)
    return outdata

def gen_encrypt_key():
    retkey = kk_gen2_ex(global_encrypt_key.client_key,global_encrypt_key.timestamp,global_encrypt_key.xid,global_encrypt_key.domain_id,global_encrypt_key.user_xid)
    tempkeyivec = retkey[0,16]
    tempkey = retkey
    strKey = DecryptHexKKey(global_encrypt_key.m_strHexKey,tempkey,tempkeyivec)
    strIvec = strKey[0,16]
    return strKey,strIvec

def decrypt_file(src_file,dst_file):
    key_hex ,hex_ivec = gen_encrypt_key()
    with open(src_file,'rb') as in_f:
	encrypt_buf = in_f.read()
	in_f.close()
	buff = decrypt_data(encrypt_buf,key_hex,s_ivec)
	with open(dst_file,'wb') as of:
	    of.write(buff)
	    return 0
	print 'faild to open output file %s'%(dst_file)
	return -2
	print 'faild to open intput file %s'%(dst_file)
    return -1




