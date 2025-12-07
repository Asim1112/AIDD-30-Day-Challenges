🌐 AI-Driven Development – 30-Day Challenge | Task 9 Submission

Instructor: Sir Hamzah Syed
Task Objective: Learn and create Claude Code Skills and Sub-Agents for generating a book.

1. Directory Structure Screenshot (Proof of Completion)

As per submission instructions, this screenshot demonstrates the complete .claudecode directory structure in VS Code, confirming the creation of the skills folder and the three required skill files.

[PASTE YOUR VSCODE EXPLORER SCREENSHOT HERE]

(The screenshot must show your project root, the hidden .claudecode folder, the skills folder, and the three skill definition files inside it.)

2. Custom Claude Code Skills for Book Generation

To automate and enhance the book-writing process using Agentic AI, I have created three custom, reusable skills. These skills package specific, detailed instructions that Claude Code can execute on demand, minimizing manual steps and friction.

Skill 1: Chapter Outline Generator

Purpose: Structural Planning

Description: This skill takes a simple, one-sentence book concept or premise from the user and systematically generates a detailed 10-chapter outline.

Key Instructions:

The output must be structured in Markdown.

The structure is mandated to include an Introduction, 8 main Development chapters, and a Conclusion.

Each chapter summary must be rich and descriptive (2-3 sentences) to guide the subsequent writing phase.

This skill replaces the need to manually prompt for structure repeatedly.

Skill 2: Plot Consistency Checker

Purpose: Continuity Assurance

Description: This is a vital editing skill that accepts two different sections of text (e.g., Chapter 1 and Chapter 5) and actively compares them to identify any breaks in continuity.

Key Instructions:

The analysis must specifically focus on potential contradictions in Character Appearance (e.g., eye color, scars), Location Details (e.g., house description, city names), and the Event Timeline.

The output is a bulleted report listing all identified inconsistencies, including the exact textual reference.

This skill ensures the integrity of the narrative across the full manuscript.

Skill 3: Grammar and Style Enhancer

Purpose: Editorial Refinement

Description: This skill acts as a focused editor, taking a segment of written text and performing a two-phase cleanup: first correcting mechanics, and second, adjusting the artistic tone.

Key Instructions:

Phase 1 (Correction): Automatically fix all grammatical errors, typos, and awkward sentence structures.

Phase 2 (Enhancement): Rewrite the text to match a "Highly Descriptive and Literary Tone," favoring strong verbs and descriptive language.

The final output should contain only the revised, polished text.

This skill provides quick, consistent editorial polish before final review.

Concept Connection: The ability to define and reuse these specialized tools is a key demonstration of the Agentic AI Paradigm Shift discussed in the study material, where the AI moves from being a passive consultant to an active collaborator that can perform complex, multi-step tasks directly within the development environment.