# Quick solves

_Some quick solutions found here and there._

---

- Access every item and thats item's index within an iterable (e.g., a list) with enumerate:
```python
>>> countries = ['Turks & Caicos', 'Grenada', 'Vanadu', 'Lebanon', 'Barbados']
>>> for idx, item in enumerate(countries):
... print(f'{idx} - {item}')
...
0 - Turks & Caicos
1 - Grenada
2 - Vanadu
3 - Lebanon
4 - Barbados
```

- How to check if a list is empty? [Source](https://dev.to/hrishikesh1990/how-to-check-if-a-list-is-empty-in-python-17ob)
    - Solution 1: **PEP 8 method**
    ```python
    l1 = ["Hire", "the", "top", "1%", "freelancers"]
    l2 = []

    if l2:
        print("list is not empty")
    else:
        print("list is empty")
    ```
    ```python
    l1 = ["Hire", "the", "top", "1%", "freelancers"]
    l2 = []

    if not l2:
        print("list is empty")
    else:
        print("list is not empty")
    ```
    - Solution 2: **bool() function**
    ```python
    l1 = ["Hire", "the", "top", "1%", "freelancers"]
    l2 = []

    if bool(l2):
        print("list is empty")
    else:
        print("list is not empty")
    ```

