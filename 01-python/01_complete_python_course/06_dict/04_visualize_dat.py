def create_dat(possible_key_range, actual_keys_values):
    # Step 1: Create DAT with None
    dat = [None] * possible_key_range

    # Step 2: Insert actual key-value pairs
    for key, value in actual_keys_values.items():
        if 0 <= key < possible_key_range:
            dat[key] = value
        else:
            print(f"⚠️ Key {key} is out of bounds and will be ignored.")

    return dat

def visualize_dat(dat):
    total_slots = len(dat)
    occupied = {i: val for i, val in enumerate(dat) if val is not None}
    empty = [i for i, val in enumerate(dat) if val is None]

    print("\n📊 Direct Access Table (DAT) Visualization")
    print("════════════════════════════════════════════")
    print(f"🔢 Total possible keys: {total_slots}")
    print(f"✅ Actual entries      : {len(occupied)}")
    print(f"🚫 Empty entries       : {len(empty)}")
    print("\n✅ Populated Keys and Values:")
    for k, v in occupied.items():
        print(f"   [{k}] → {v}")

    print("\n🚫 Empty Keys:")
    print(f"   {empty if len(empty) <= 20 else str(empty[:20]) + ' ...'}")  # Truncate if too long

# Example usage
possible_key_range = 20  # 0 to 19
actual_data = {
    3: "Ali",
    7: "Zara",
    10: "Fahad",
    15: "Huzair",
    18: "Ayesha",
    1:'huz',
    21:'aa'
}

dat = create_dat(possible_key_range, actual_data)
visualize_dat(dat)
