# Blin

Blin helps to build a lucid interface between users and your system. It empowers the system with intelligence to recognize user intentions, provide information or control functionality via commands!
<br/>

## Key Features 

<!-- blin adds AI to your system and teaches it to reason which command to execute or what guidance to provide on non-obvious users requests. All that's needed is commands and/or text information to learn. -->
- **Prompt to commands**: understands user intentions from a text prompt and returns the best fitting commands

- **Multi-request**: returns multiple commands if user's intention is to perform several tasks simultaneously (e.g., increase temperature and decrease volume)

- **Valid command guarantee**: always returns a valid command with valid parameters

- **Additional knowledge**: ability to add texts that are used to provide additional context or guidance for the user

- **Infinite memory (almost)**: as long as there's space in cloud, there's room for learning

<br/>

## Usage is simple

<!-- #### Example: -->
```python
my_ai    = blin.open_project('MyAI', key=blin_key)
response = my_ai.request("I'm hot")
```

```
>>> response
{
    'commands': {'decrease_temperature': {'parameters': {'delta': 5}}}, 
    'text': "I've decreased the temperature by 5 degrees Fahrenheit."
}
```

<!-- #### Example: -->
```python    
response = my_ai.request("My ears are bleeding from this music")
```

```
>>> response
{
    'commands': {'audio_adjust_volume': {'parameters': {'delta': -10}}}, 
    'text': "I'm sorry to hear that. I've adjusted the volume for you."
}
```

<br/>

## Getting started

Install blin:
```
pip install blin
```

Create your AI: 
```python
blin_key = "<blin_key>"     # contact us: support@lemeni.com to get one
settings = {"openai_key"    : "<openai_key>",       # get your key @ https://openai.com/
            "pinecone_key"  : "<pinecone_key>",     # get your key @ https://www.pinecone.io/
            "pinecone_index": "<pinecone_index>" }  # create your index @ https://www.pinecone.io/

blin.create_project('MyAI', settings=settings, key=blin_key)
```

Define commands to control the system:
```python
commands = {
    "increase_temperature": {
        "brief" : "Increases temperature per user's request or when it's too low",
        "parameters": {
            "delta": "integer value from interval [1, 10] that represents temperature increase in Fahrenheit"
        }
    },
    "decrease_temperature": {
        "brief" : "Decreases temperature per user's request or when it's too high",
        "parameters": {
            "delta": "integer value from interval [1, 10] that represents temperature decrease in Fahrenheit"
        }
    },
    "adjust_volume": {
        "brief" : "Makes volume adjustment",
        "parameters": {
            "delta": "integer value from interval [-10, 10] that represents volume adjustment in %"
        }
    },
}
```

Train your AI:
```python
my_ai = blin.open_project('MyAI', blin_key)
my_ai.learn_commands(commands) 
```

Use it:
```python
my_ai    = blin.open_project('MyAI', blin_key)
command  = my_ai.request("I'm hot")
call(command) # your function to execute commands
```

<br/>

## API Documentation

### Create project
Create project. All learned commands/texts will be stored in it

```python
blin.create_project(project_id, settings, key)
```

- project_id (str) : name of the project
- settings (dict)  : project settings dict in the format:
     {
        "openai_key"    : "...",
        "pinecone_key"  : "...",
        "pinecone_index": "...",
     }
- key (str) : blin authorization key
- **returns:** str: result. Raises exception if the project was already created.


<br/>

### Open project
Open created project for learning or usage

```python
project = blin.open_project(project_id, key)
```

- project_id (str)  : project identifier     
- key (str)         : blin authorization key
- **returns:** Project object

<br/>

### Delete Project    
Remove project. Warning: all knowledge (commands and texts) associated will be removed, and cannot be restored!

```python
blin.delete_project(project_id, key)
```

- project_id (str)    : project identifier     
- key (str)      : blin authorization key
- **returns:** str: result. Raises exception if the project was not deleted.


<br/>

### Learn Commands

Add commands to the project

```python
project.learn_commands(commands)
```

- commands (dict) : commands dict to learn, in the format below
- **returns:** None


```python
# Commands dict format
commands = {
    "command_name_1"  : {
        "brief"     : "string description of command purpose",
        "parameters": {
            "parameter_name": "string description of parameter purpose, type, range",
            ...
    },
    "command_name_2" : ...
}
```

<br/>

### Learn Texts

Add texts to the project. This information is used by AI as additional context or to provide guidance for the user

```python
project.learn_texts(texts):
```


- texts (dict)   : texts to learn in the format: { "text_name"  : "text", ... }
- **returns:** None

<br/>

### Recall Command Names

Return a list of names of all learned commands

```python
project.recall_command_names()
```

- **returns:** list: names of all learned commands
        
<br/>

### Recall Text Names
    
Return a list of names of all learned texts

```python
project.recall_text_names()
```

- **returns:** list: names of all learned texts

<br/>

### Recall Command or Text
    
Return learned command or text for given name

```python
project.recall(name)
```

- name (str) : command or text name
- **returns:** dict: learned command or text (see [Learn Commands](#learn-commands)
, [Learn Texts](#learn-texts))
        

<br/>

### Forget Command or Text

Delete the knowledge (command of text)

```python
project.forget(name)
```


- name (str) : command or text name
- **returns:** str: result. Raises exception if the knowledge was not deleted.

<br/>
        
### Request AI Answer
  
Return command to execute or/and text response based on user request and project knowledge

```python
project.request(request)
```

- request (str)  : user request 
- **returns:** dict: commands to execute (can be {}) and text response (can be "") in the format below


```python     
{
    "commands"  : <commands_dict>, 
    "text"      : "text response"
}
```

<br/>
   
## Contacts

For any questions or feedback, you can reach us at support@lemeni.com.