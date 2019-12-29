# Example for calculating mix_col
import AES.utils.functions as aes
from logical_operations.logic import convert_hex_to_bin_string
from logical_operations.logic import xor_binString as xor

ca = [0x1E, 0xEA, 0x24, 0xB3]
cb = [0x10, 0x90, 0xB5, 0x9C]
cc = [0xD3, 0x1D, 0xCE, 0x45]
cd = [0x23, 0x24, 0x34, 0xF8]

round_key_1 = convert_hex_to_bin_string(0xF5135F3F89A87757203ED1B212E003F9, 128)


all_c_combine = [
    ''.join(aes.mix_col_get_keys(aes.generate_mix_col_list(ca))),
    ''.join(aes.mix_col_get_keys(aes.generate_mix_col_list(cb))),
    ''.join(aes.mix_col_get_keys(aes.generate_mix_col_list(cc))),
    ''.join(aes.mix_col_get_keys(aes.generate_mix_col_list(cd)))
]

all_c_combine = ''.join(all_c_combine)

xor_round_key = xor(all_c_combine, round_key_1, 128)

print(f"Key: {xor_round_key}")
