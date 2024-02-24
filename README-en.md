[![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=FFFFFF&size=35&center=true&vCenter=true&width=1000&lines=🖩+CALCULATOR+🖩)](https://git.io/typing-svg)


🌍
*[English](README-en.md) ∙ [Português](README.md) ∙ [简体中文](README-zh.md)*


![GitHub language count](https://img.shields.io/github/languages/count/amandfernandes/Calculator?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/amandfernandes/Calculator?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/amandfernandes/Calculator?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-017AD7?style=for-the-badge&logo=windows&logoColor=white)

This project is a simplified version of a calculator made in Python that accepts user commands to perform simple arithmetic calculations. The calculator is capable of performing the four fundamental operations: addition, subtraction, multiplication, and division. The program maintains a continuous cycle, requesting user inputs until they choose to end it.

## 💻 Prerequisites
![Python](https://img.shields.io/badge/Python-3.12.0-14354C?style=for-the-badge&logo=python&logoColor=white)

## ☕ How to use Calculator

To use Calculator, follow these steps:

**1. *Start the program:*** Run the Python script, Calculator.py, to start the calculator.

**2. *Enter the first number:*** The program will ask you to enter a number. Type a valid number and press Enter.

**3. *Choose the operation:*** Next, the program will ask you to enter an operator. The valid operators are '+' for addition, '-' for subtraction, '*' for multiplication, and '/' for division. Type the operator and press Enter.

**4. *Enter the second number:*** The program will ask you to enter a second number. Type a valid number and press Enter.

**5. *See the result:*** The program will perform the chosen operation on the two numbers and display the result.

**6. *Continue or exit:*** You can continue to perform more operations on the result or exit the program. To continue, repeat steps 3-4. To exit, type x when asked to enter an operator.

### Usage Example:
![resultadocalc](https://github.com/amandfernandes/Calculator/assets/144744139/6c3a33bc-e2c2-4cd4-b5db-9ff40e89d2b5)


### Error handling

The program has error handling for invalid entries:

- **Invalid number**: If you enter something that is not a number when asked to enter a number, the program will display an error message and ask you to enter a valid number.

- **Invalid operator**: If you enter something that is not a valid operator (`+`, `-`, `*`, `/`) when asked to enter an operator, the program will display an error message and ask you to enter a valid operator.

- **Division by zero**: If you try to divide by zero, the program will display an error message and restart.

### Known Difficulties
Currently, the project faces some difficulties that may be addressed in the future:
1. This block of code prints an error message if the divisor (b) is zero, but it does not automatically stop the execution of the program.
   
   ![calculatorerr](https://github.com/amandfernandes/Calculator/assets/144744139/b7e8f4e6-6315-4a7a-8c8b-067e4d09525d)
2. The user's input is not fully handled for more complex expressions, leading to unpredictable results in some cases

## 📝 Notes:
- The calculator uses a continuous loop to allow the user to perform multiple calculations until choosing to exit.
- The code uses Python 3.10's new pattern matching syntax for cleaner code.
- The calculator handles various scenarios and provides informative error messages for better user interaction.

## 💡 Ideas:
Here are some ideas to improve and expand this project in the future:
1. **Advanced Operations Support:** Add support for more advanced mathematical operations, such as exponentiation, square root, etc.
2. **Internationalization:** Add support for multiple languages, making the calculator accessible to users from different regions.

## 📫 Contributing to Calculator
To contribute to Calculator, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, refer to the GitHub documentation on [how to create a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

