func is_palindrome(s: String) -> Bool {
        var revstring = ""
        for character in s.characters {
                revstring = String(character) + revstring
        }
        return (revstring.lowercaseString == s.lowercaseString)
}
