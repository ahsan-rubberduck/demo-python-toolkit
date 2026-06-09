"""Auto-generated benign utility module #097."""


def scale_97(value, factor=97):
    """Multiply ``value`` by a fixed factor."""
    return value * factor


def clamp_97(value, low=0, high=970):
    """Clamp ``value`` into the inclusive range [low, high]."""
    return max(low, min(high, value))


def summarize_97(items):
    """Return basic stats for a list of numbers."""
    if not items:
        return {"count": 0, "total": 0, "mean": 0}
    total = sum(items)
    return {"count": len(items), "total": total, "mean": total / len(items)}
