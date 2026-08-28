# Task: String Formatting
# Goal: Transform a raw SKU into a readable title.

def format_sku(sku_string):
    """
    Instructions: Convert 'engine-oil-10w30' to 'Engine Oil 10w30'.
    """
    # TODO: Implement logic
    split_str = sku_string.split('-')
    cap_str = []
    for s in split_str:
        cap_str.append(s[0].upper() + s[1:])

    return " ".join(cap_str)

# Test: format_sku("brake-pads-ceramic") -> "Brake Pads Ceramic"
print(format_sku('engine-oil-10w30'))