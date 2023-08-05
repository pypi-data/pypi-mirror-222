# flake8: noqa

LETTERS_WITH_DIACRITICS = {
    # A/a
                        'Ă': 'A', 'ă': 'a', 'Â': 'A', 'â': 'a',
    'À': 'A', 'à': 'a', 'Ằ': 'A', 'ằ': 'a', 'Ầ': 'A', 'ầ': 'a',
    'Ả': 'A', 'ả': 'a', 'Ẳ': 'A', 'ẳ': 'a', 'Ẩ': 'A', 'ẩ': 'a',
    'Ã': 'A', 'ã': 'a', 'Ẵ': 'A', 'ẵ': 'a', 'Ẫ': 'A', 'ẫ': 'a',
    'Á': 'A', 'á': 'a', 'Ắ': 'A', 'ắ': 'a', 'Ấ': 'A', 'ấ': 'a',
    'Ạ': 'A', 'ạ': 'a', 'Ặ': 'A', 'ặ': 'a', 'Ậ': 'A', 'ậ': 'a',
    # E/e
                        'Ê': 'E', 'ê': 'e',
    'È': 'E', 'è': 'e', 'Ề': 'E', 'ề': 'e',
    'Ẻ': 'E', 'ẻ': 'e', 'Ể': 'E', 'ể': 'e',
    'Ẽ': 'E', 'ẽ': 'e', 'Ễ': 'E', 'ễ': 'e',
    'É': 'E', 'é': 'e', 'Ế': 'E', 'ế': 'e',
    'Ẹ': 'E', 'ẹ': 'e', 'Ệ': 'E', 'ệ': 'e',
    # I/i
    'Ì': 'I', 'ì': 'i',
    'Ỉ': 'I', 'ỉ': 'i',
    'Ĩ': 'I', 'ĩ': 'i',
    'Í': 'I', 'í': 'i',
    'Ị': 'I', 'ị': 'i',
    # O/o
                        'Ô': 'O', 'ô': 'o', 'Ơ': 'O', 'ơ': 'o',
    'Ò': 'O', 'ò': 'o', 'Ồ': 'O', 'ồ': 'o', 'Ờ': 'O', 'ờ': 'o',
    'Ỏ': 'O', 'ỏ': 'o', 'Ổ': 'O', 'ổ': 'o', 'Ở': 'O', 'ở': 'o',
    'Õ': 'O', 'õ': 'o', 'Ỗ': 'O', 'ỗ': 'o', 'Ỡ': 'O', 'ỡ': 'o',
    'Ó': 'O', 'ó': 'o', 'Ố': 'O', 'ố': 'o', 'Ớ': 'O', 'ớ': 'o',
    'Ọ': 'O', 'ọ': 'o', 'Ộ': 'O', 'ộ': 'o', 'Ợ': 'O', 'ợ': 'o',
    # U/u
                        'Ư': 'U', 'ư': 'u',
    'Ù': 'U', 'ù': 'u', 'Ừ': 'U', 'ừ': 'u',
    'Ủ': 'U', 'ủ': 'u', 'Ử': 'U', 'ử': 'u',
    'Ũ': 'U', 'ũ': 'u', 'Ữ': 'U', 'ữ': 'u',
    'Ú': 'U', 'ú': 'u', 'Ứ': 'U', 'ứ': 'u',
    'Ụ': 'U', 'ụ': 'u', 'Ự': 'U', 'ự': 'u',
    # Y/y
    'Ỳ': 'Y', 'ỳ': 'y',
    'Ỷ': 'Y', 'ỷ': 'y',
    'Ỹ': 'Y', 'ỹ': 'y',
    'Ý': 'Y', 'ý': 'y',
    'Ỵ': 'Y', 'ỵ': 'y',
    # D/d
    'Đ': 'D', 'đ': 'd'
}


def remove_tone(text):
    return ''.join((
        LETTERS_WITH_DIACRITICS.get(char, char)
        for char in text
    ))
