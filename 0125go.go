func isAlphaNumeric(c rune) bool {
    return unicode.IsLetter(c) || unicode.IsDigit(c)
}

func isPalindrome(s string) bool {
    sRunes := []rune(s)
    i := 0
    j := len(s) - 1

    for i < j {
	for i < j && !isAlphaNumeric(sRunes[i]) {
	    i++
	}
	for i < j && !isAlphaNumeric(sRunes[j]) {
	    j--
	}
	if unicode.ToLower(sRunes[i]) != unicode.ToLower(sRunes[j]) {
	    return false
	}
	i++
	j--
    }
    return false
}
