# Match That! — CLI

A Python command-line prototype of **Match That!**, a turn-based multiplayer fingerboarding game where players compete to land randomly generated tricks and earn points.

This project was developed to prototype the core gameplay mechanics of the upcoming **Match That! Flutter mobile app**, while practicing Python and object-oriented programming (OOP).

## Features

- **2–8 Players** — Play with friends using custom names or guest profiles.
- **150 Skateboarding Tricks** — Randomly selected from a predefined trick library.
- **Difficulty-Based Scoring** — Easy (3–5 points), Medium (10–15 points), and Hard (20–30 points).
- **Two Game Modes** — Quickplay (10 tricks) and Full Game (30 tricks).
- **Live Scoreboard** — Track player scores throughout the game.
- **Final Rankings** — Display the winner and player standings.

## How to Play

1. Choose the number of players, names, and game mode.
2. A random trick is generated for the first player.
3. **Matched:** The player earns points and a new trick is generated.
4. **Missed:** No points are awarded, and the next player attempts the same trick.
5. Turns rotate until 10 or 30 tricks have been successfully matched. The player with the highest score wins!

## Getting Started

**Requirements:** Python 3.12 or newer. No external dependencies required.

Clone the repository:

```bash
git clone https://github.com/yanyanDev/match-that-cli.git
cd match-that-cli
```

Run the game:

```bash
python main.py
```

Follow the terminal prompts to configure and start your game.

## Project Structure

| File | Description |
|---|---|
| `main.py` | Program entry point and main menu |
| `game_brain.py` | Game settings, turn management, and scoring logic |
| `game_components.py` | Player classes and trick library |
| `art.py` | Terminal ASCII art |
| `rules_text.py` | Game description and instructions |

## Project Status

**CLI prototype complete.**

This version focuses on validating the game's fundamental mechanics through a terminal interface. It does not yet include the timer-based gameplay planned for the mobile app.

**Built with:** Python · Object-Oriented Programming

---

*Small board. Big game.*
