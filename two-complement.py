# TODO: move to dbuzzell-scripts
# Source: https://stackoverflow.com/a/26641777/14242484
def twos_complement(hex_num, num_bits=32):
    if hex_num >= 1 << (num_bits - 1):
        hex_num -= 1 << num_bits
    return hex_num


print(twos_complement(0xFFFFD8F1))
