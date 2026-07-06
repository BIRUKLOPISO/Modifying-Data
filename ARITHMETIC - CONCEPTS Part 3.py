import numpy as np

print("=" * 50)
print("NUMPY ARITHMETIC - CONCEPTS 11-15")
print("=" * 50)

# Base arrays
arr_mod = np.array([5, 7, 9, 10])
arr_abs = np.array([-5, 3, -9, 2, -1])
arr_power = np.array([2, 3, 4])
arr_trig = np.array([0, np.pi/2, np.pi])
arr_stats = np.array([2, 3, 4, 5, 6])

print("\n--- CONCEPT 11: MODULO AND REMAINDER ---")
print("1. Modulo 3:")
print(arr_mod % 3)

print("\n2. Modulo 4:")
print(arr_mod % 4)

print("\n3. Modulo 5:")
print(arr_mod % 5)

print("\n--- CONCEPT 12: ABSOLUTE VALUE ---")
print("4. np.abs():")
print(np.abs(arr_abs))

print("\n5. np.absolute():")
print(np.absolute(arr_abs))

print("\n6. np.fabs() (returns floats):")
print(np.fabs(arr_abs))

print("\n--- CONCEPT 13: POWER AND EXPONENTS ---")
print("7. Square (power 2):")
print(arr_power ** 2)

print("\n8. Cube (power 3):")
print(arr_power ** 3)

print("\n9. Square root:")
print(np.sqrt(arr_power))

print("\n--- CONCEPT 14: TRIGONOMETRIC FUNCTIONS ---")
print("10. Sine:")
print(np.sin(arr_trig))

print("\n11. Cosine:")
print(np.cos(arr_trig))

print("\n12. Tangent:")
print(np.tan(arr_trig))

print("\n--- CONCEPT 15: STATISTICAL OPERATIONS ---")
print("13. Mean (average):")
print(np.mean(arr_stats))

print("\n14. Standard deviation:")
print(np.std(arr_stats))

print("\n15. Original array:")
print(arr_stats)

print("\n" + "=" * 50)
print("COMPLETE! ")
print("=" * 50)