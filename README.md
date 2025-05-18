# ColtCruz-Building-a-Rule-Based-AI-System-with-Python

## Part 1: Initial Project Ideas

### 1. Project Idea 1: Recipe Recommender  
**Description:** A system that recommends recipes based on ingredients the user has on hand. The user enters ingredients, and the system matches them to recipes using predefined rules.  
**Rule-Based Approach:**  
- The system checks for exact matches and partial matches with the ingredients required for recipes in a dataset.  
- Missing ingredients are suggested for partial matches.

### 2. Project Idea 2: Simple Chatbot  
**Description:** A chatbot that responds to user inputs with predefined answers. The chatbot simulates a conversation by identifying keywords and phrases in user inputs.  
**Rule-Based Approach:**  
- Responses are based on keywords such as "hello," "help," or "bye."  
- For example, if the user says "hello," the system responds with "Hi there! How can I assist you?"

### 3. Project Idea 3: LOTR-Inspired MMO Character Creator  
**Description:** A system that helps users create a fantasy character by choosing a race and class, validating combinations based on lore-inspired rules.  
**Rule-Based Approach:**  
- The system uses rules to restrict race/class combinations based on lore (e.g., Hobbits can’t be Warriors, Elves can choose any class).  
- Rules are based on predefined restrictions inspired by the Lord of the Rings fantasy setting.

**Chosen Idea:** LOTR-Inspired MMO Character Creator  
**Justification:** I chose this project because it connects to my passion for fantasy worlds and games. It’s a great example of how rule-based systems can enforce lore accuracy and guide users through character creation without needing machine learning.

---

## Part 2: Rules/Logic for the Chosen System

- IF race is "Orc" AND class is "Paladin" → Orcs can't be Paladins. Try Warlock or Warrior.  
- IF race is on the “Good” side (Men, Elves, Dwarves, Hobbits) AND class is "Warlock" → Good races can’t be Warlocks. Try Lorebook or Paladin.  
- IF race is "Dwarf" AND class is "Assassin" → Dwarves can’t be Assassins. Try Warrior or Paladin.  
- IF race is "Hobbit" AND class is "Warrior" → Hobbits can’t be Warriors. Try Lorebook or Rogue.  
- IF race is "Goblin" AND class is "Warrior" → Goblins can’t be Warriors. Try Assassin or Warlock.  
- IF race is "Uruk" AND class is "Assassin" → Uruks can’t be Assassins. Try Warrior or Warlock.  
- IF race is "Orc" → Orcs can be any class **except** Paladin.  
- IF race is "Man" OR race is "Elf" → No restrictions.  
- ELSE → Character is valid.

---

## Part 3: Sample Input/Output

**Enter your choices:**  
Race: Orc  
Class: Paladin  
**Output:** Orcs can't be Paladins. Try Warlock or Warrior.

**Enter your choices:**  
Race: Elf  
Class: Warlock  
**Output:** Character created: Elf Warlock.  

**Enter your choices:**  
Race: Hobbit  
Class: Warrior  
**Output:** Hobbits can’t be Warriors. Try Lorebook or Rogue.

---

## Part 4: Reflection

**Overview:**  
This project involved building a rule-based fantasy character creator based on the Lord of the Rings world. The system uses logical if-else rules to guide users through valid race/class combinations and prevent lore-breaking choices.

**Challenges:**  
- Organizing rules to avoid conflicts or redundancy.  
- Handling exceptions like Orcs being mostly unrestricted but with one limitation.  
- Designing fallback responses that feel like in-universe guidance.

**What I learned:**  
Rule-based systems are perfect for enforcing logic in systems where structure and limitations matter, like fantasy lore or gameplay balance. This project helped me see how even a simple rule engine can simulate complex systems if the rules are clear and consistent.

---
