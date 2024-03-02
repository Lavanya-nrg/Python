# Write a Python program to display a given decimal value in scientific notation. Use decimal.Decimal

# Import the decimal module to handle decimal arithmetic
import decimal

# Function to format a decimal number in scientific notation
def format_e(n):
    # Convert the decimal number to scientific notation as a string
    a = '%E' % n
    # Split the string at 'E' to separate the mantissa and exponent parts
    mantissa = a.split('E')[0]
    exponent = a.split('E')[1]
    # Remove trailing zeros and the dot from the mantissa
    formatted_mantissa = mantissa.rstrip('0').rstrip('.')
    # Combine the formatted mantissa and exponent with 'E' in between
    result = formatted_mantissa + 'E' + exponent
    return result

# Display the original and scientific notation for a specific decimal value
print("Original decimal value: "+ "40800000000.00000000000000")
print("Scientific notation of the said decimal value:")
# Call the format_e function with the specified decimal value
print(format_e(decimal.Decimal('40800000000.00000000000000')))

# Repeat the process for two more decimal values
print("\nOriginal decimal value: "+ "40000000000.00000000000000")
print("Scientific notation of the said decimal value:")
print(format_e(decimal.Decimal('40000000000.00000000000000')))

print("\nOriginal decimal value: "+ "40812300000.00000000000000")
print("Scientific notation of the said decimal value:")
print(format_e(decimal.Decimal('40812300000.00000000000000')))
