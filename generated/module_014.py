"""Auto-generated benign utility module #014."""


def scale_14(value, factor=14):
    """Multiply ``value`` by a fixed factor."""
    return value * factor


def clamp_14(value, low=0, high=140):
    """Clamp ``value`` into the inclusive range [low, high]."""
    return max(low, min(high, value))


def summarize_14(items):
    """Return basic stats for a list of numbers."""
    if not items:
        return {"count": 0, "total": 0, "mean": 0}
    total = sum(items)
    return {"count": len(items), "total": total, "mean": total / len(items)}
