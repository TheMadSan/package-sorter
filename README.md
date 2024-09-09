# Package Sorter

This Python function sorts packages based on their dimensions and mass according to predefined rules for a robotic automation system. The function decides whether the package should be dispatched to the `STANDARD`, `SPECIAL`, or `REJECTED` stack.

## Sorting Rules:

1. **Bulky**: 
   - Volume ≥ 1,000,000 cm³ 
   - OR any dimension (width, height, length) ≥ 150 cm
2. **Heavy**: 
   - Mass ≥ 20 kg
3. **Stacks**:
   - `STANDARD`: Packages that are neither bulky nor heavy.
   - `SPECIAL`: Packages that are either bulky or heavy.
   - `REJECTED`: Packages that are both bulky and heavy.

## Example Usage:

```python
# Import and use the function
from sort_packages import sort

print(sort(100, 100, 100, 10))  # Output: STANDARD
print(sort(200, 100, 100, 10))  # Output: SPECIAL (bulky)
print(sort(100, 100, 100, 25))  # Output: SPECIAL (heavy)
print(sort(200, 200, 200, 25))  # Output: REJECTED (both bulky and heavy)
