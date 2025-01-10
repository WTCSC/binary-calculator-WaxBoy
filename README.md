[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17658312)
# Binary Calculator

<!--

The following requirements must be met to receive full credit on this assignment. The calculator must handle binary arithmetic operations accurately while following proper error handling procedures and output formatting guidelines.

- Your solution must have a well-written and thorough README file.
- The solution must be implemented as a function called `binary_calculator()` with three parameters:
    - `bin1` - A string parameter representing the first binary number to be used in the calculation. Must contain only 0s and 1s.
    - `bin2` - A string parameter representing the second binary number to be used in the calculation. Must contain only 0s and 1s.
    - `operator` - A string containing one of the following arithmetic operators: `'+'`, `'-'`, `'*'`, or `'/'`
- Do not use Python's built-in `bin()` function.
- Implement your own binary-to-decimal and decimal-to-binary conversion logic.
- All binary inputs and outputs should be strings.
- Handle division by zero by returning `"NaN"`
- Handle decimal numbers by rounding down to the nearest whole number (flooring).
- Return `"Error"` for invalid binary inputs (containing characters other than `0` and `1`)
- Return `"Overflow"` for any operations that overflow (i.e. negative numbers, numbers greater than 8-bits).
- Outputs must be returned as 8-bit numbers (padded with leading zeros if necessary). For example, the decimal number `5` should be returned as `"00000101"` .

Your solution will be tested against various test cases including edge cases, invalid inputs, and all four arithmetic operations.

 -->
 
Run using the function binary_calculator(bin1, bin2, operator), requiring 3 parameters: Two 8-bit numbers (Only 0's and/or 1's) and an operator ('+', '-', '*', or '/').

## Usage:

"Error" error is thrown if:
* 'operator' is not '+', '-', '*', or '/'
* 'bin1' or 'bin2' is not 8 characters in length.
* 'bin1' or 'bin2' consists of anything other than 0's and/or 1's

"Overflow" error is thrown if:
* Result would exceeds 8 bits (255)
* Result is less than 0 (Negative numbers cannot be expressed)

"NaN" error is thrown if:
* Trying to divide by 0 (00000000)

## Code:

Check for "Error"

In lines 8 and 9, the two binary strings are converted into decimal numbers. A for loop looks at each number of the binary string, starting from the back, multiplying the either 1 or 0 by 2 to the power of its index, and summing them together.

The operations are then performed, accounting for "NaN", and flooring divison using '//' rather than a standard '/'.

Checks for overflow.

To convert back to binary, the decimal number is checked to be even or odd using % 2 == 1. If odd, a 1 is appended to the left of the output; else a 0. The number is then divided by 2 and floored, and the process repeats 8 times to get all 8 binary digits. Voila.
