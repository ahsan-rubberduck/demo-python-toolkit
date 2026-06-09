"""Auto-generated benign utility module #025."""


def scale_25(value, factor=25):
    """Multiply ``value`` by a fixed factor."""
    return value * factor


def clamp_25(value, low=0, high=250):
    """Clamp ``value`` into the inclusive range [low, high]."""
    return max(low, min(high, value))


def summarize_25(items):
    """Return basic stats for a list of numbers."""
    if not items:
        return {"count": 0, "total": 0, "mean": 0}
    total = sum(items)
    return {"count": len(items), "total": total, "mean": total / len(items)}
