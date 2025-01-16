
# Employee Discount Management System

## Overview
The **Employee Discount Management System** is a Python-based application designed to calculate employee discounts dynamically based on their employment type, years of service, and purchase history. The program enforces a maximum discount cap of $200 per employee while maintaining daily summary totals.

## Features
- **Dynamic Discount Calculation**: Calculates discounts using parameters like employee type (managerial or non-managerial) and years worked.
- **Robust Input Validation**: Ensures accurate data entry for integers, floats, and boolean inputs.
- **Modular Function Design**: Reusable functions for input validation, discount calculation, and result display.
- **Daily Totals Summary**: Tracks and summarizes daily purchase totals before and after discounts.
- **User-Friendly Output**: Provides clear and concise results for each employee and a final daily summary.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Usage](#usage)
3. [Key Functions](#key-functions)
4. [Technologies Used](#technologies-used)
5. [Future Enhancements](#future-enhancements)
6. [License](#license)

---

## Getting Started
To use this project:
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/employee-discount-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd employee-discount-system
   ```
3. Run the program:
   ```bash
   python employee_discount_system.py
   ```

---

## Usage
1. Launch the program, and follow the prompts to enter details such as:
   - Employee type (`YES` for managerial, `NO` for non-managerial).
   - Years worked by the employee.
   - Year-to-date (YTD) purchase total.
   - Today's purchase amount.
2. View the calculated discount details and totals for each employee.
3. Choose whether to enter details for another employee or end the session.
4. At the end of the session, view the daily totals summary.

---

## Key Functions
- **`DisplayInstructions`**: Displays program instructions and purpose.
- **`ValidateInteger`**: Ensures integer inputs are valid and non-negative.
- **`ValidateFloat`**: Validates and parses float inputs.
- **`ValidateBoolean`**: Validates string inputs for "YES" or "NO".
- **`DetermineDiscountBonus`**: Determines discount bonus for managerial employees.
- **`CalculateDiscountPercent`**: Calculates the discount percentage based on tenure and bonus.
- **`CalculateYTDiscount`**: Computes the YTD discount capped at $200.
- **`CalculateDiscount`**: Calculates the discount for today's purchase.
- **`DisplayResults`**: Displays individual employee results.
- **`DisplaySummary`**: Summarizes daily purchase totals.

---

## Technologies Used
- **Programming Language**: Python
- **Key Concepts**: Modular programming, input validation, control flow, and user I/O operations.

---

## Future Enhancements
- **Database Integration**: Store employee and purchase data persistently.
- **GUI Development**: Add a graphical user interface for improved usability.
- **Advanced Validation**: Include validations for edge cases and erroneous inputs.
- **Detailed Reporting**: Generate printable reports for daily summaries.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to contribute or provide feedback! 😊
