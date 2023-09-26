# python-scripts
A collection of my python scripts

## Calculator app

### Usage

When you run this script you will be presented with two options; Console Calculation or File Calculation (and an Exit option).

#### Console Calculation

In console calculation mode you will be asked firstly for the first number, then the second, and then the operator (+, -, *, / or ^).

Once these have been entered it will output the full calculation with an answer. It may output in scientific notation for large numbers.

#### File Calculation

For file calculations you need to create a .txt file with all the calculations you wish to run (an (example file)[calc_test_data.txt] is included).

> [!important]
> Make sure your terminal is running in the same directory as the calculations test file.

The format is:

```
<number1> <operator> <number2>
```

When you select the File Calculation option you will be asked for the file name, enter the file name and extention, e.g. calculations.txt. The terminal will then output the calculations with results, one per line.

## Ciphers

### affine.py

This is a class implementation of the affine cipher, see affine_usage.py for usage info.

### cypher.py

This script takes your input and outputs a new string encoded with each letter moved by 15, spaces symbols remain the same.