def first_non_repeating_char(s: str) -> str:
    """
    Find the first non-repeating character in a string.
    
    Args:
        s: Input string (case-sensitive)
        
    Returns:
        First non-repeating character, or empty string if none exists
    """
    if not s:
        return ""
    
    # Count frequency of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find first character with count 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    return ""


# Unit Tests
def test_first_non_repeating_char():
    """Test cases for first_non_repeating_char function"""
    
    # Basic cases
    assert first_non_repeating_char("swiss") == "w"
    assert first_non_repeating_char("hello") == "h"
    assert first_non_repeating_char("aabb") == ""
    
    # Edge cases
    assert first_non_repeating_char("") == ""  # Empty string
    assert first_non_repeating_char("aa") == ""  # All repeating
    assert first_non_repeating_char("a") == "a"  # Single character
    
    # Case sensitivity
    assert first_non_repeating_char("sS") == "s"
    assert first_non_repeating_char("Ss") == "S"
    
    # Mixed cases
    assert first_non_repeating_char("stress") == "t"
    assert first_non_repeating_char("hhello") == "e"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_first_non_repeating_char()