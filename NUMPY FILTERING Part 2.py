import numpy as np

print("=" * 50)
print("NUMPY FILTERING Part 2")
print("=" * 50)

# Base array for all concepts
arr = np.array([8, 15, 23, 42, 36, 19, 54, 31])
arr_clean = np.array([5, np.nan, 12, np.inf, 7, np.nan, 25, np.inf, 18])
print(f"\nBase array: {arr}")
print(f"Array with NaN/Inf: {arr_clean}")
print("=" * 30)

print("\n--- CONCEPT 4: EXTRACT FUNCTION ---")
print(np.extract(arr > 40, arr))

print("\nTask 1:")
print(np.extract(arr > 19, arr))

print("\nTask 2:")
print(np.extract(arr < 23, arr))

print("\n" + "=" * 30)

print("\n--- CONCEPT 5: LOGICAL OPERATIONS ---")
print(arr[(arr > 20) & (arr < 50)])

print("\nTask 1:")
print(arr[(arr > 19) & (arr < 54)])

print("\nTask 2:")
print(arr[(arr < 19) | (arr > 47)])

print("\n" + "=" * 30)

print("\n--- CONCEPT 6: ISNAN / ISINF ---")
print(np.isnan(arr_clean))

print("\nTask 1:")
print(np.isnan(arr_clean))

print("\nTask 2:")
print(arr_clean[(~np.isnan(arr_clean)) & (~np.isinf(arr_clean))])

print("\n" + "=" * 50)
print("END OF Part 2.")
