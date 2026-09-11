"""
AI Learning & Study Assistant
------------------------------
A simple demo showing the 3 core agent capabilities:
  1. RAG    -> retrieves explanations from course materials (data/materials.py)
  2. Tools  -> generate_quiz() and create_study_plan() functions the agent can "use"
  3. Memory -> remembers topics studied and quiz results across the session

Run:
    python main.py
"""

from data.materials import COURSE_MATERIALS, QUIZ_BANK


# ---------- 1. MEMORY ----------
class Memory:
    """Tracks study history: topics asked about and quiz attempts."""
    def __init__(self):
        self.topics_studied = []
        self.quiz_log = []

    def log_topic(self, topic):
        if topic not in self.topics_studied:
            self.topics_studied.append(topic)

    def log_quiz(self, topic, num_questions):
        self.quiz_log.append({"topic": topic, "questions": num_questions})

    def show(self):
        print("\n--- Study Memory ---")
        print(f"Topics studied: {', '.join(self.topics_studied) if self.topics_studied else 'None yet'}")
        for entry in self.quiz_log:
            print(f"Quiz taken on '{entry['topic']}' ({entry['questions']} questions)")


# ---------- 2. RAG (Retrieval) ----------
STOPWORDS = {"what", "is", "are", "the", "explain", "me", "about", "a", "an", "how", "do", "does"}

def retrieve(query):
    """Simple keyword-based retrieval over course materials."""
    query_words = [w.strip("?.,") for w in query.lower().split() if w not in STOPWORDS]
    best_match, best_score = None, 0

    for note in COURSE_MATERIALS:
        text = (note["content"] + " " + note["topic"]).lower()
        score = sum(1 for w in query_words if w and w in text)
        if score > best_score:
            best_score, best_match = score, note

    return best_match if best_score > 0 else None


# ---------- 3. TOOLS ----------
def create_study_plan_tool(topics, days):
    """Distributes topics evenly across the given number of days."""
    plan = {f"Day {i+1}": [] for i in range(days)}
    for i, topic in enumerate(topics):
        day = f"Day {(i % days) + 1}"
        plan[day].append(topic)
    return plan


def generate_quiz_tool(topic):
    """Pulls a short quiz for a topic from the quiz bank."""
    return QUIZ_BANK.get(topic, [])


# ---------- AGENT LOGIC ----------
def study_assistant_agent(user_input, memory):
    text = user_input.lower()

    # Tool: study plan request
    if "study plan" in text:
        topics = ["loops", "functions", "data structures", "oop"]
        plan = create_study_plan_tool(topics, days=2)
        lines = [f"{day}: {', '.join(items)}" for day, items in plan.items()]
        return "Here is your study plan:\n   " + "\n   ".join(lines)

    # Tool: quiz request
    if "quiz" in text:
        topic = next((t for t in QUIZ_BANK if t in text), "loops")
        quiz = generate_quiz_tool(topic)
        memory.log_quiz(topic, len(quiz))
        lines = [f"Q{i+1}: {q['q']}" for i, q in enumerate(quiz)]
        return f"Quiz on '{topic}':\n   " + "\n   ".join(lines)

    # RAG: general concept question
    note = retrieve(user_input)
    if note:
        memory.log_topic(note["topic"])
        return note["content"]

    return "Sorry, I don't have material on that topic yet."


# ---------- DEMO ----------
if __name__ == "__main__":
    memory = Memory()

    inputs = [
        "What are Python data structures?",
        "Explain functions",
        "Give me a study plan",
        "Quiz me on loops",
    ]

    print("=== AI Learning & Study Assistant ===\n")
    for msg in inputs:
        print(f"You: {msg}")
        response = study_assistant_agent(msg, memory)
        print(f"Assistant: {response}\n")

    memory.show()
