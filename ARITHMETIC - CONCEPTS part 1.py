import numpy as np

print("=" * 50)
print("NUMPY ARITHMETIC - CONCEPTS 1-5")
print("=" * 50)

# Base arrays
arr1 = np.array([2, 3, 4])
arr2d = np.array([[2, 3, 4], [1, 2, 3]])
arr_decimal = np.array([2.3, 3.7, 4.2, 5.8])

print("\n--- CONCEPT 1: BASIC ARRAY OPERATIONS ---")
print("1. Multiplication by 2:")
print(arr1 * 2)

print("\n2. Subtraction:")
print(arr1 - 1)

print("\n3. Self subtraction:")
print(arr1 - arr1)

print("\n--- CONCEPT 2: BROADCASTING ---")
print("4. Add scalar:")
print(arr1 + 3)

print("\n5. Power operation:")
print(arr1 ** 2)

print("\n6. Tile/repeat array:")
print(np.tile(arr1, (3, 1)))

print("\n--- CONCEPT 3: UNIVERSAL FUNCTIONS (ufuncs) ---")
print("7. Square root:")
print(np.sqrt(arr1))

print("\n8. Exponential:")
print(np.exp(arr1))

print("\n9. Sine:")
print(np.sin(arr1))

print("\n--- CONCEPT 4: AGGREGATIONS/REDUCTIONS ---")
print("10. Sum:")
print(np.sum(arr1))

print("\n11. Median:")
print(np.median(arr1))
print("\n12. Maximum:")
print(np.max(arr1))

print("\n--- CONCEPT 5: AXIS-WISE OPERATIONS ---")
print("13. Sum along axis=0 (columns):")
print(np.sum(arr2d, axis=0))

print("\n14. Sum along axis=1 (rows):")
print(np.sum(arr2d, axis=1))

print("\n15. Stack with column sums:")
print(np.vstack([arr2d, np.sum(arr2d, axis=0)]))


print("\n" + "=" * 50)
print("END OF CONCEPTS 1-5")
print("=" * 50)