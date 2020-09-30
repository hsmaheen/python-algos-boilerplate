# Python Algorithm Boilerplate

### Introduction

This repo will provide an easy way to start writing and testing python algorithms, please read further on how to use this

### Prerequisites

- Python 3
- Knowledge of Python virtual envs
- Visual Studio Code
- Python Plugin by Microsoft (id: ms-python.python)

### Setup

To use this repo, follow the steps below:

```sh
$ git clone https://github.com/hsmaheen/python-algos-boilerplate

$ cd python-algos-boilerplate
$ pip3 install pipenv
$ pipenv install
$ pre-commit install
```

Once done close and open your VS Code terminal (`Ctrl + ~ )` and the virtual env will automatically be picker by VS Code

The above steps will help to get all the required dependencies in the project

### Testing

#### Using VS Code Test Runner

We use pytest to run test, you can run the test using VS Codes inbuilt Test Runner which can be found in the sidebar of VS Code

#### Using Command Line

To run all tests using the command line just use the following command

```sh
$ pytest
```

### Debugging

To debug any particular python file, follow the steps below:

- Navigate to VS Code's Debug Menu (in the sidebar of VS Code)
- Choose the option "Python: Debug Current File"
- Click on Play and the the debugger while stop at the place where the breakpoint has been placed

### Writing Algo Challenges

I view Algorithmic questions as challenges rather than problems, hence you can see that I have created a challenges folder under which i have coded the solution for the simple binary search, you can follow the same folder structure where each challenge is a folder, inside which you can find the solution as well as the test for each

### Committing Code

If you wish to fork this and use it in your as your own repository then you will have to ensure that all tests are working as this project has pre-commit hook to ensure that all tests pass

### Contribution

Please feel to raise a PR if you think you can improve this boilerplate
