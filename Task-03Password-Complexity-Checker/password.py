import re
import math
from getpass import getpass

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLOR = True
except ImportError:
    COLOR = False


def color(text, c):
    return c + text + Style.RESET_ALL if COLOR else text

def load_common_passwords():
    try:
        with open("sample.txt", "r") as f:
            return set(p.strip().lower() for p in f.readlines())
    except FileNotFoundError:
        return set()


def has_repeating_pattern(password):
    return bool(re.search(r"(.)\1{2,}", password))


def has_keyboard_pattern(password):
    patterns = ["qwerty", "asdf", "zxcv", "1234", "abcd"]
    return any(p in password.lower() for p in patterns)


def contains_dictionary_word(password):
    dictionary = ["admin", "welcome", "hello", "india", "user"]
    return any(word in password.lower() for word in dictionary)


def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        charset += 32

    if charset == 0:
        return 0

    return round(math.log2(charset ** len(password)), 2)


def crack_time(entropy):
    if entropy < 40:
        return "Seconds (Very Unsafe)"
    elif entropy < 60:
        return "Hours to Days"
    else:
        return "Years (Strong)"


def attack_risk(entropy, dictionary_used):
    if dictionary_used:
        return "High risk (Dictionary attack)"
    elif entropy < 40:
        return "High risk (Brute-force attack)"
    elif entropy < 60:
        return "Moderate risk"
    else:
        return "Low risk"

def check_password(password, common_passwords):
    score = 0
    feedback = []

    # Length (Weighted)
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Consider using 12+ characters for better security")
    else:
        feedback.append("Password is too short (minimum 8 characters)")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    if has_repeating_pattern(password):
        feedback.append("Avoid repeating characters or patterns")

    if has_keyboard_pattern(password):
        feedback.append("Avoid keyboard patterns (qwerty, 1234, etc.)")

    dictionary_used = contains_dictionary_word(password)
    if dictionary_used:
        feedback.append("Avoid dictionary words")

    if password.lower() in common_passwords:
        score = 0
        feedback.append("Blacklisted password – extremely unsafe")

    return score, feedback, dictionary_used

def main():
    print("\n🔐 ADVANCED PASSWORD COMPLEXITY CHECKER\n")

    password = getpass("Enter your password: ")

    common_passwords = load_common_passwords()
    score, feedback, dictionary_used = check_password(password, common_passwords)

    entropy = calculate_entropy(password)
    crack_estimate = crack_time(entropy)
    risk = attack_risk(entropy, dictionary_used)

    if score <= 2:
        strength = color("WEAK ❌", Fore.RED)
    elif score <= 4:
        strength = color("MEDIUM ⚠️", Fore.YELLOW)
    else:
        strength = color("STRONG ✅", Fore.GREEN)

    print("\n📊 PASSWORD SECURITY ANALYSIS")
    print("--------------------------------")
    print(f"Strength          : {strength}")
    print(f"Entropy           : {entropy} bits")
    print(f"Crack Time        : {crack_estimate}")
    print(f"Attack Risk       : {risk}")

    if feedback:
        print("\n🔧 SECURITY IMPROVEMENTS:")
        for f in feedback:
            print("•", f)
    else:
        print("\n🛡️ Excellent! Your password follows strong security practices.")

    print("\n🔒 Privacy Notice: Passwords are processed locally and never stored.\n")


if __name__ == "__main__":
    main()
