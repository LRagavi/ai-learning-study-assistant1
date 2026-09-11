"""
Tiny knowledge base simulating course materials / notes.
In a real RAG system, this would be a vector database (e.g. FAISS, Chroma).
Here we keep it simple: a list of topic notes with keyword matching.
"""

COURSE_MATERIALS = [
    {
        "id": 1,
        "topic": "python basics",
        "content": "Python is an interpreted, high-level language. Variables don't need explicit type declarations, and indentation defines code blocks instead of braces."
    },
    {
        "id": 2,
        "topic": "loops",
        "content": "Python has two main loop types: 'for' loops iterate over a sequence, while 'while' loops repeat as long as a condition is True."
    },
    {
        "id": 3,
        "topic": "functions",
        "content": "Functions are defined using the 'def' keyword. They can take parameters, have default values, and return one or more values."
    },
    {
        "id": 4,
        "topic": "data structures",
        "content": "Common Python data structures include lists (ordered, mutable), tuples (ordered, immutable), dictionaries (key-value pairs), and sets (unique items)."
    },
    {
        "id": 5,
        "topic": "oop",
        "content": "Object-Oriented Programming in Python uses classes and objects. Key concepts are encapsulation, inheritance, and polymorphism."
    },
]

# Quiz question bank, grouped by topic, used by the quiz-generator tool.
QUIZ_BANK = {
    "loops": [
        {"q": "Which loop is best when you know the exact number of iterations?", "a": "for loop"},
        {"q": "What keyword stops a loop early in Python?", "a": "break"},
    ],
    "functions": [
        {"q": "Which keyword defines a function in Python?", "a": "def"},
        {"q": "What statement sends a value back from a function?", "a": "return"},
    ],
    "data structures": [
        {"q": "Which data structure is immutable: list or tuple?", "a": "tuple"},
        {"q": "Which data structure stores unique, unordered items?", "a": "set"},
    ],
}
