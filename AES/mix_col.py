# Example for calculating mix_col
import AES.utils.functions as aes

input_bytes = [0x1E, 0xEA, 0x24, 0xB3]

print(aes.mix_col_get_keys(aes.mix_col(input_bytes)))
