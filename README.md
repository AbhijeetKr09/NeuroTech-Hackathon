# Project: Neuphony Dino Game

## Project Overview

This repository contains the codebase for the Neuphony Dino Game, a project focused on utilizing biopotential signals, specifically brain waves, for an interactive gaming experience.

## Folder Structure

- `__pycache__`: Python bytecode cache directory.
- `data`: Directory for storing data related to the game.
- `Formula.py`: Main algorithm for calculating the score.
- `tempCodeRunnerFile.py`: Temporary code runner file.
- `visual_mod.py`: Modified visualizer for displaying brain waves.
- `visual_unfocused.py`: Detects brain waves in an unfocused state.

## Synapse Module Overview
## Image
![Neuphony Synapse](![image](https://github.com/AbhijeetKr09/NeuroTech-Hackathon/assets/117449002/5ef4741b-8f85-47b1-b700-325e36b26e46)
)
The project incorporates Neuphony Synapse, a versatile solution for various physiological monitoring applications. It supports ECG, EEG, EOG, and EMG signals, ensuring compatibility with different platforms like Arduino, ESP32, STM32, and more. The optional bypass of the bandpass filter allows tailored signal output for diverse analysis.

## Project Components

### Formula.py

Contains the main algorithm responsible for calculating the score in the game.

### visual_mod.py

This file has been modified from the original `visualizer.py` to display brain waves during the gaming experience.

### visual_unfocused.py

Detects brain waves in an unfocused state, contributing to the interactive elements of the game.

### Dino Folder

Houses the game designed for focused state activity, leveraging the Neuphony Synapse module.

