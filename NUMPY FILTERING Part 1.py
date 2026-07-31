import numpy as np

print("=" * 50)
print("NUMPY FILTERING Part 1")
print("=" * 50)

# Base array for all concepts
arr = np.array([8, 15, 23, 42, 36, 19, 54, 31])
print(f"\nBase array: {arr}")
print("=" * 30)

print("\n--- CONCEPT 1: BOOLEAN INDEXING ---")
print(arr[arr > 40])

print("\nTask 1:")
print(arr[arr > 8])

print("\nTask 2:")
print(arr[arr < 36])

print("\n" + "=" * 30)

print("\n--- CONCEPT 2: WHERE FUNCTION ---")
print(np.where(arr > 40, "High", "Low"))

print("\nTask 1:")
print(np.where(arr % 2 == 0, "Even", "Odd"))

print("\nTask 2:")
print(np.where(arr < 47, 0, 1))

print("\n" + "=" * 30)

print("\n--- CONCEPT 3: SELECT FUNCTION ---")
conditions = [arr < 15, arr < 30, arr < 50, arr < 70]
choices_str = ["Tiny", "Small", "Medium", "Large"]
choices_num = [0, 1, 2, 3]
default_str = "Huge"
default_num = 4

print(np.select(conditions, choices_str, default=default_str))

print("\nTask 1:")
print(np.select(conditions, choices_str, default=default_str))

print("\nTask 2:")
print(np.select(conditions, choices_num, default=default_num))

print("\n" + "=" * 50)
print("END OF Part 1.")
