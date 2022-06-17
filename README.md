# REST Chess solver

###### Here write description of the project

## How to run this application  following commands:
- 'git clone https://github.com/JaryjDementor/Chess_solver.git'
- 'python -m venv .venv'
- 'source .venv/bin/activate'
- 'pip install -r requirements.txt'
- 'python runner.py'

## API Description
### This API have two endpoint which requires GET Request:
- /api/v1/{chess-figure}/{current-field} ;
- /api/v1/{chess-figure}/{current-field}/{dest-field}.

### In case everything is ok and mail was successfully sent API returns empty response with status code 202. Otherwise you'll get response with error message and appropriative status code.

### The first endpoint displays a list of possible moves for a given {chess-figure} figure from the indicated {current-field}.
### Example:
- http://127.0.0.1:5000/api/v1/pawn/a1
### Returns:

### {
    "availableMoves": [
        [
            "a2"
        ]
    ],
    "error": "null",
    "figure": "pawn",
    "currentField": "a1"
}



