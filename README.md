# basic-todo
A really basic todo list cli application

I was having a chat with someone on discord, and this is an example program that sprung up from it. It's not actually intended to be used.

# Usage:
Get your to do list:
```bash
python basicToDo.py list
```
The output is in format:
```
0: Task 1:	go shopping
1: Sitting:	be sitting
```
The first column is just an id, the second is your task name and the third one is the description.
You can always specify a different file to use:
```bash
python basicToDo.py --file my_todo.json list
```
This works with every command, just make sure the command goes after `--file`.
To add an item:
```bash
python basicToDo.py add "go shopping tomorrow morning"
```
If you want to name it something other than "Task N":
```bash
python basicToDo.py add "go shopping tomorrow morning" --name Shopping
```
To remove an item:
```bash
python basicToDo.py remove "Shopping"
```
You can also remove an item by id:
```bash
python basicToDo.py remove 0
```
To modify an item:
```bash
python basicToDo.py set 0 "My new description"
```
or:
```bash
python basicToDo.py set --name "Sitting" 0 "Actually don't go shopping, covid exists"
```
To clear the whole list:
```bash
python basicToDo.py clear
```
