# Template

## 1. to find the first true

**T**, T, T, T, T, F, F, F

F, F, F, F, **T**, T, T, T

```python
def binary_search_first_true:
    lo, hi = 0, n
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if condition is True:
            hi = mid
        else
            lo = mid + 1

    return lo
```

## 2. to find the last true

T, T, T, T, **T**, F, F, F

F, F, F, F, T, T, T, **T**

```python
def binary_search_last_true:
    lo, hi = 0, n
    while lo < hi:
        # right biased `mid`
        mid = lo + (hi - lo + 1) // 2
        if condition is True:
            lo = mid
        else:
            hi = mid - 1

    return lo
```

## 3. to find the first false

T, T, T, T, T, **F**, F, F

**F**, F, F, F, T, T, T, T

```python
def binary_search_first_false:
    lo, hi = 0, n
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if condition is False:
            lo = mid + 1
        else:
            hi = mid

    return lo
```

## 4. to find the last false

T, T, T, T, T, F, F, **F**

F, F, F, **F**, T, T, T, T

```python
def binary_search_last_false:
    lo, hi = 0, n
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if condition is False:
            hi = mid - 1
        else:
            lo = mid

    return lo
```

## Resource

General Binary Search Thought Process: 4 Templates - [src](https://leetcode.com/problems/find-peak-element/solutions/788474/general-binary-search-thought-process-4-templates/)
