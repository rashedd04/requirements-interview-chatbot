# Requirements-elicitation interview chatbot

A command-line chatbot that plays the role of a requirements analyst: it interviews a business owner, one short question at a time, to find out what they need from a new system. It runs fully locally on a small open model (Gemma 3, 4B) through [Ollama](https://ollama.com).

Course assignment at Grenoble INP – Génie Industriel (November 2025), based on the "Cool Ski Resorts" case study: the owner of three ski resorts wants an online booking, rental and payment system.

## What it shows

The interest of the project is the prompt, not the amount of code. Two versions are kept so the difference is visible:

| File | System prompt |
| --- | --- |
| `baseline.py` | One sentence: interview a ski-resort owner with short questions. |
| `main.py` | A structured prompt with the full case description as context and explicit interviewing rules. |

Rules encoded in `main.py`, taken from the classic mistakes analysts make in elicitation interviews:

1. One short, focused question per turn.
2. A fixed order: build rapport and understand the business, then current problems, then future needs.
3. Active listening: every two or three turns, stop, rephrase what the stakeholder said and ask for confirmation.
4. Ask about business problems and desired outcomes only, never about technical solutions.
5. Close with a structured summary of all requirements collected.

## Run it

1. Install [Ollama](https://ollama.com) and download the model:

   ```bash
   ollama pull gemma3:4b
   ```

2. Install the Python client and start the interview:

   ```bash
   pip install -r requirements.txt
   python main.py
   ```

You answer as the resort owner. Press Enter on an empty line to end the conversation. To use another model, change `model_name` at the top of the file.

## How it works

The script keeps the whole conversation in a list of messages (system prompt, then alternating turns) and sends it to the local model at every turn with `ollama.chat`. There is no external API and no data leaves the machine.

## Limits and next steps

- No transcripts or scores are included, so the effect of the structured prompt is not measured here.
- The rules are instructions to the model, not checks in the code; a 4B model does not always follow them.
- Next: save transcripts, score both prompts against a checklist of interviewer mistakes, and compare the requirements found with a reference list.

## Credits

The "Cool Ski Resorts" case description embedded in `main.py` was provided with the course assignment and is not covered by the licence of this repository.

## Licence

MIT (see `LICENSE`).
