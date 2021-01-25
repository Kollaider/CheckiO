# Python Basics UpSkill Lab #1

## Info
- Stepic course:
    - NAME: Программирование на Python
    - URL: https://stepik.org/course/67/syllabus
- Starts on 2021-01-25
- Ends on 2021-02-25 (roughly)

## Rules:
1. Make commits to `master` branch only via Pull Requests
2. Branches with tasks must have the following name structure that consists
from numbers of section, lesson, task. E.g.`task_1-12-1`
3. The same as above for commit's comments
4. 1 commit = 1 solved task (consists at least from 2 files: a task and a test)
5. Make any commit only after launching `flake8` and `python -m unittest`
6. Each task can be considered solved only if it includes and passes unittest
(and the more test cases is better) and doesn't violate the code style
7. Tasks and unittests must strongly follow PEP8, PEP257
8. File names for tasks must follow the PEP8's rules for variables

## Structure of filenames
### Task files
`task_N_NAME.py` where:
- `N` - index number of a task in a lesson
- `NAME` - name of the task
### Test files
`test_task_N_NAME.py` where:
- `N` - index number of a task in a lesson
- `NAME` - name of the task

## Catalogs structure
- stepic
    - section_number (e.g. section_1, section_2, ...)
        - lesson_number (e.g. lesson_1, lesson_2, ...)
            - task_number_name (e.g. task_1_some_name.py, ...)
            - ...
        - ...
    - ...
- tests
    - section_number (e.g. section_1, section_2, ...)
        - lesson_number (e.g. lesson_1, lesson_2, ...)
            - test_task_number_name (e.g. test_task_1_some_name.py, ...)
            - ...
        - ...
    - ...
- .flake8
- .gitignore
- readme.md
- requirements.txt

## Task structure
- Docstring with task definition. Consists from the fields: name (at the first
line), URL, DESCRIPTION, INPUT/OUTPUT EXAMPLE
- Imports (optional)
- Function `task_name` which should pass all the tests
- Function `main` should launch the task function against one input set of
input data
- Running `main` if the script is launching