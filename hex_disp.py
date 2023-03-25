def hex_disp(hex_string,reverse=1):
    print("print hex:", hex_string.upper())
    re_bin_string = ""
    binary_string = ''.join(['{:04b}'.format(int(hex_string[i], 16)) for i in range(0, len(hex_string))])
    if(reverse):
        re_bin_string = reverse_binary(binary_string)
    else:
        re_bin_string = binary_string
    print("\nByte:%d" % ((len(re_bin_string)+1)/8 - 1))
    for i in range(len(re_bin_string)):
        print("\t[",len(re_bin_string) - i - 1,"\t]:",re_bin_string[i], end='')
        if((i+1)%8==0 and i != len(re_bin_string) - 1):
            print("\nByte:%d" % ((len(re_bin_string)+1)/8 - (i+1)/8 - 1))
        

    
def subhex_disp(hex_string, start_bit, end_bit):
    binary_string = ''.join(['{:04b}'.format(int(hex_string[i], 16)) for i in range(0, len(hex_string))])
    re_bin_string = reverse_binary(binary_string)
    sub_binary_string = re_bin_string[start_bit:end_bit]
    subhex = hex(int(sub_binary_string, 2))[2:]
    print("subhex", "start",start_bit, ", end", end_bit)
    hex_disp(subhex,reverse=0)


def reverse_hex(hex_string):
    bytes_list = [hex_string[i] for i in range(0, len(hex_string))]
    bytes_list.reverse()
    return ''.join(bytes_list)

def reverse_binary(bin_string):
    bytes_list = [bin_string[i] for i in range(0, len(bin_string))]
    bytes_list.reverse()
    return ''.join(bytes_list)

hex_string = "20000080000001ff0000000000000200"
hex_disp(hex_string,reverse=0)
# subhex_disp(hex_string,2,62)

