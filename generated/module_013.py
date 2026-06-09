"""Auto-generated benign utility module #013."""


def scale_13(value, factor=13):
    """Multiply ``value`` by a fixed factor."""
    return value * factor


def clamp_13(value, low=0, high=130):
    """Clamp ``value`` into the inclusive range [low, high]."""
    return max(low, min(high, value))


def summarize_13(items):
    """Return basic stats for a list of numbers."""
    if not items:
        return {"count": 0, "total": 0, "mean": 0}
    total = sum(items)
    return {"count": len(items), "total": total, "mean": total / len(items)}
