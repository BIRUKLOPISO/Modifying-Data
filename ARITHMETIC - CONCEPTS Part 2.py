import numpy as np

print("=" * 50)
print("NUMPY ARITHMETIC - CONCEPTS 6-10")
print("=" * 50)

# Base arrays
arr1 = np.array([2, 3, 4])
arr_comp = np.array([5, 7, 9, 10])
arr_decimal = np.array([2.3, 3.7, 4.2, 5.8])
A = np.array([[2, 3], [4, 1]])
B = np.array([[1, 4], [2, 3]])

print("\n--- CONCEPT 6: COMPARISON OPERATORS ---")
print("1. Greater than 3:")
print(arr1 > 3)

print("\n2. Greater than 1:")
print(arr1 > 1)

print("\n3. Less than 4:")
print(arr1 < 4)

print("\n--- CONCEPT 7: BOOLEAN OPERATIONS ---")
mask1 = arr1 > 2
mask2 = arr1 < 4

print("4. NOT operation (~):")
print(~(arr1 == 3))

print("\n5. AND operation (&):")
print((arr1 > 2) & (arr1 < 4))

print("\n6. OR operation (|):")
print((arr1 < 3) | (arr1 > 3))

print("\n--- CONCEPT 8: MATRIX MULTIPLICATION ---")
print("7. A @ B (matrix multiplication):")
print(A @ B)

print("\n8. B @ A (matrix multiplication reverse order):")
print(B @ A)

print("\n9. Element-wise multiplication:")
print(A * B)

print("\n--- CONCEPT 9: CUMULATIVE OPERATIONS ---")
arr_cum = np.array([3, 4, 3])
print("10. Cumulative sum:")
print(np.cumsum(arr_cum))

print("\n11. Cumulative product:")
print(np.cumprod(arr_cum))

print("\n12. Stack with cumulative sum:")
print(np.vstack([arr_cum, np.cumsum(arr_cum)]))

print("\n--- CONCEPT 10: ROUNDING OPERATIONS ---")
print("13. Round to nearest:")
print(np.round(arr_decimal))

print("\n14. Floor (round down):")
print(np.floor(arr_decimal))

print("\n15. Ceil (round up):")
print(np.ceil(arr_decimal))

print("\n" + "=" * 50)
print("END OF CONCEPTS 6-10")
print("=" * 50)