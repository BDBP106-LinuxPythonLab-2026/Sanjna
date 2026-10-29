# password validator
spch=["!", "@", "#", "$", "%", "&", "*"]

while True:
    p = input("Enter a password: ")
    has_digit = any(i.isdigit() for i in p)
    has_upper = any(i.isupper() for i in p)
    has_lower = any(i.islower() for i in p)
    has_sp= any(ch in p for ch in spch)
    min_len = len(p) >= 8
    no_space = " " not in p
    no_pswd = "password" not in p.lower()
    if has_digit and has_upper and has_lower and has_sp and min_len and no_space and no_pswd:
        print("Password accepted!")
        break
    rules=["Password must:"]
    if not (has_digit and has_upper and has_lower): rules.append("at least one uppercase letter, one lowercase letter and one digit")
    if not (min_len): rules.append("at least 8 characters")
    if not (no_space): rules.append("have no spaces")
    if not (no_pswd): rules.append("not contain the word \"password\" in any case")
    if not (has_sp): rules.append("have at least one special character from {\"!\", \"@\", \"#\", \"$\", \"%\", \"&\", \"*\"}")
    print(*rules, sep="\n")

