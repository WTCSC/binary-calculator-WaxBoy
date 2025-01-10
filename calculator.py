def binary_calculator(bin1, bin2, operator):

    #check that operator is valid, and that both binary strings contain 8 digits consisting of only 0 and/or 1
    if operator not in '+-*/' or len(bin1) != 8 or len(bin2) != 8 or not set(bin1) <= {'0', '1'} or not set(bin2) <= {'0', '1'}:
        return('Error')
    
    #convert the binary string into a decimal integer
    dec1 = sum(int(a)*(2 ** i) for i, a in enumerate(bin1[::-1])) #changed abs(i-7) and bin1 to i and bin1[::-1] because it makes more intuitive sense
    dec2 = sum(int(b)*(2 ** j) for j, b in enumerate(bin2[::-1]))
    
    #perform basic operations using 2 decimal numbers
    if operator in '+-*':
        dec3 = eval(f"{dec1} {operator} {dec2}")

    #if dividing, must account for divide by 0, and must floor the operation using '//'
    elif operator == '/':
        if dec2 == 0:
            return('NaN')
        dec3 = dec1 // dec2
    
    #check for any number not possible within 8 bits 0 <= x <= 255
    if dec3 > 255 or dec3 < 0:
        return('Overflow')

    #build output
    output = ''
    for _ in range(8):      #the most intuitive and efficient method I can think of
        output = '1' + output if dec3 % 2 == 1 else '0' + output
        dec3 = dec3 // 2
    return(output)

print(binary_calculator('01011111', '00100101', '+'))
