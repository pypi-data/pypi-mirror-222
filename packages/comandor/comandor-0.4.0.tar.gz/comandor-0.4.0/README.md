# Comandor

Very Simple Script for Run your command!  
A simple tool to simplify some repetitive
tasks such as updating the Linux repository and daily tasks!

## How Install

> pip install comandor

### How Use

- make file .comandor  
- setup config like this (json file)

```json
{
  "name": "Update Apps!",
  "debug": true, // run debug mode ( not necessary )
  "logfile": "./logs.log", // where save logs ( not necessary )
  "actions": [
    {
      "action_name": "scoop update pkg",
      "path": "C:/",
      "commands": [
        "scoop update -g *"
      ],
      "timeout": 5000
    }
    // you can add more action
  ]
}
```  

OR yaml file:

```yaml
name: "test rund command"
debug: true
logfile: "./logs.log"
actions:
  - action_name: "test12"
    path: "."
    commands:
      - "cd ."
    timeout: 5000

```

- you can see .comandor.example for more example  
- and run this command

> comandor

### Command Line Help

```txt
❯ comandor -h
usage: comandor [-h] [-l LOGFILE] [-c CONFIG] [-d] [-sk SKIP]

options:
  -h, --help            show this help message and exit
  -l LOGFILE, --logfile LOGFILE
                        where save logfile
  -c CONFIG, --config CONFIG
                        where you have config file
  -d, --debug           run debug mod
  -sk SKIP, --skip SKIP
                        skip with text,check text and if found match skip
```

### How run tests?

> python -m unittest  test/test_comandor.py
