[![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=FFFFFF&size=35&center=true&vCenter=true&width=1000&lines=🖩+计算器+🖩)](https://git.io/typing-svg)


🌍
*[英语](README-en.md) ∙ [葡萄牙语](README.md) ∙ [简体中文](README-zh.md)*

![GitHub语言数量](https://img.shields.io/github/languages/count/amandfernandes/Calculator?style=for-the-badge)
![GitHub分叉数](https://img.shields.io/github/forks/amandfernandes/Calculator?style=for-the-badge)
![Bitbucket打开问题](https://img.shields.io/bitbucket/issues/amandfernandes/Calculator?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-017AD7?style=for-the-badge&logo=windows&logoColor=white)

这个项目是一个用Python制作的简化版本计算器，它接受用户的命令来执行简单的算术计算。该计算器能够执行四则基本运算：加法、减法、乘法和除法。程序将保持一个连续循环，要求用户输入，直到用户选择退出为止。


## 💻 先决条件
![Python](https://img.shields.io/badge/Python-3.12.0-14354C?style=for-the-badge&logo=python&logoColor=white)

## ☕ 如何使用Calculator

要使用Calculator，请按照以下步骤操作：


**1. *启动程序：*** 运行Python脚本Calculator.py以启动计算器。

**2. *输入第一个数字：*** 程序将要求您输入一个数字。输入有效数字并按Enter键。

**3. *选择操作：*** 然后，程序将要求您输入一个运算符。有效的运算符包括'+'表示加法，'-'表示减法，'*'表示乘法和'/'表示除法。输入运算符并按Enter键。

**4. *输入第二个数字：*** 程序将要求您输入第二个数字。输入有效数字并按Enter键。

**5. *查看结果：*** 程序将对所选的两个数字执行所选的操作，并显示结果。

**6. *继续还是退出：*** 您可以继续对结果进行更多操作，或退出程序。要继续，重复步骤3-4。要退出，请在提示输入运算符时键入x。


### 使用示例：
![resultadocalc](https://github.com/amandfernandes/Calculator/assets/144744139/e13fbdcf-4399-4e96-8b88-d54cba3a616c)


### 错误处理

该程序对无效输入进行了错误处理：

- **无效数字：** 如果您在提示输入数字时输入了非数字内容，程序将显示错误消息并要求您输入有效数字。

- **无效操作符：** 如果您在提示输入操作符时输入了非有效操作符（'+'、'-'、'*'、'/'），程序将显示错误消息并要求您输入有效操作符。

- **除以零：** 如果您尝试除以零，程序将显示错误消息并重新开始。


### 已知问题

目前，该项目面临一些已知问题，可能会在将来解决：

1. 当除数（b）为零时，此代码块会打印错误消息，但不会自动停止程序执行。
   
   ![calculatorerr](https://github.com/amandfernandes/Calculator/assets/144744139/f99571a0-1e7f-4f7c-ae8c-67b2de53eb48)
2. 用户输入未完全处理以进行更复杂的表达式，导致某些情况下结果不可预测。

## 📝 注：
- 该计算器使用连续循环，允许用户执行多个计算，直到选择退出。
- 代码使用Python 3.10的新模式匹配语法，使代码更清晰。
- 该计算器处理了多种情况，并提供了详细的错误消息，以提高用户交互体验。

## 💡 想法：
以下是扩展和改进此项目的一些想法：
1. **支持高级操作：** 添加对更高级的数学操作的支持，如乘方、根号等。
2. **国际化：** 添加对多种语言的支持，使计算器适用于不同地区的用户。

## 📫 为Calculator做贡献
要为Calculator做贡献，请按以下步骤操作：

1. Fork此存储库。
2. 创建一个分支：`git checkout -b <branch_name>`。
3. 进行更改并提交它们：`git commit -m '<commit_message>'`
4. 推送到原始分支：`git push origin <name_of_project>/<location>`
5. 创建拉取请求。

或者，查看GitHub文档中的[如何创建拉取请求](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)。


