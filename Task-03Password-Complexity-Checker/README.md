Password Complexity Checker (Python CLI)

I. Project Overview

The Password Complexity Checker is a Python-based command line security tool designed to evaluate the strength of user passwords using multiple security-focused criteria. The tool analyzes password structure, entropy, common attack patterns, and provides detailed feedback to help users create strong and secure passwords.

This project is implemented as Task-03 under the PRODIGY_CS_07 repository and focuses on real-world cybersecurity practices rather than simple rule-based validation.

II. Objectives

1. To analyze password strength using modern security parameters
2. To identify weak and commonly used passwords
3. To estimate the resistance of passwords against common attack techniques
4. To provide actionable feedback for improving password security
5. To ensure privacy by avoiding password storage or logging

III. Features

1. Secure password input with hidden typing
2. Password strength classification as Weak, Medium, or Strong
3. Weighted scoring system with preference for longer passwords
4. Entropy calculation to measure password randomness
5. Estimated password crack time analysis
6. Detection of blacklisted and commonly used passwords
7. Dictionary word detection to prevent dictionary attacks
8. Keyboard pattern and repeating character detection
9. Attack risk classification including brute-force and dictionary attacks
10. Privacy-focused design with no password storage

IV. Technologies Used

1. Python 3
2. Built-in Python libraries including re, math, and getpass
3. Optional external library colorama for colored command line output

V. Project Structure

PRODIGY_CS_07
|
└── Password-Complexity-Checker
    |
    ├── code
    |   └── password_checker.py
    |
    ├── output
    |   └── sample_output.txt
    |
    ├── common_passwords.txt
    └── README.md

VI. Installation and Setup

1. Clone or download the PRODIGY_CS_07 repository
2. Navigate to the Password-Complexity-Checker directory
3. Ensure Python 3 is installed on the system
4. Install the optional dependency using the command
   pip install colorama

VII. How to Run the Program

1. Open a command prompt or terminal
2. Navigate to the code directory
3. Execute the following command
   python password_checker.py

VIII. Sample Output

The program provides an analysis of the password including its strength level, entropy value, estimated crack time, attack risk classification, and security improvement suggestions. A sample output is available in the output directory for reference.

IX. Security and Privacy Considerations

1. Passwords are processed locally within the system
2. No password data is stored, logged, or transmitted
3. The tool is designed strictly for educational and ethical purposes

X. Future Enhancements

1. Development of a graphical user interface using Tkinter
2. Web-based implementation for browser usage
3. Integration with real-world password breach databases
4. Enhanced password policy customization

XI. Author Information

Name: Hema Lisa
Project: Password Complexity Checker
Repository: PRODIGY_CS_07
Domain: Cybersecurity

XII. License

This project is intended for educational and learning purposes and may be freely used or modified with proper attribution.
