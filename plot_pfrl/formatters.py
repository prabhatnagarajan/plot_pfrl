

def pct_formatter(y, pos):
    """
    Args:
        y (float): Tick value.
        pos (int): Position.
        
    Returns:
        str: Formatted tick label.
    """
    val = y
    return f'{val:.0f}%'


def millions_formatter(x, pos):
    """
    Args:
        x (float): Tick value.
        pos (int): Position.
        
    Returns:
        str: Formatted tick label.
    """
    val = x / 1000000
    return f'{val:.0f}M'


def thousands_formatter(y, pos):
    """
    Args:
        y (float): Tick value.
        pos (int): Position.
        
    Returns:
        str: Formatted tick label.
    """
    if y < 1_000_000:
        val = y / 1000
        return f'{val:.0f}K'
    else:
        val = y / 1_000_000
        return f'{val:.0f}M'

def hundreds_formatter(y, pos):
    """
    Args:
        y (float): Tick value.
        pos (int): Position.
        
    Returns:
        str: Formatted tick label.
    """
    val = y / 100
    if val == 0:
        return f'{val:.0f}'
    return f'{val:.0f}00'

def two_fifty_formatter(y, pos):
    """
    Args:
        y (float): Tick value.
        pos (int): Position.
        
    Returns:
        str: Formatted tick label.
    """
    if y < 0:
        result = f'{y}'
    if y == 0:
        result = f'{y:.0f}'
    elif y < 1000:
        if y == 500:
            result = f'500'
        elif y == 750:
            result = f'750'
        elif y == 250:
            result = f'250'
        else:
            result = f'{y}'
    else:
        val = float(y) / 1000
        if y % 500 == 0 and y % 1000 != 0:
            result = f'{val:.1f}K'
        elif y % 250 == 0 and y % 1000 != 0:
            result = f'{val:.2f}K'
        else:
            result = f'{val:.0f}K'
    return result

def five_hundreds_formatter(y, pos):
    """
    Args:
        y (float): Tick value.
        pos (int): Position.
        
    Returns:
        str: Formatted tick label.
    """
    if y < 0:
        result = f'{y}'
    if y == 0:
        result = f'{y:.0f}'
    elif y < 1000:
        if y == 500:
            result = f'500'
        else:
            result = f'{y}'
    else:
        val = float(y) / 1000
        if y % 500 == 0 and y % 1000 != 0:
            result = f'{val:.1f}K'
        else:
            result = f'{val:.0f}K'
    return result
