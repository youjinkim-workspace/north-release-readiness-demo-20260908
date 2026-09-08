"""Bounded batching for demonstration exports."""
def batches(rows, size=100):
    if size <= 0:
        raise ValueError("size must be positive")
    for start in range(0, len(rows), size):
        yield rows[start:start + size]
