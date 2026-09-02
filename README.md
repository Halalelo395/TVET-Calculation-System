# TVET Calculation System

A FastAPI-based API that calculates TVET semester marks and determines qualification for final examination.

## How it works
The semester mark is calculated as:
- Test 1 (20%): test1 * 0.2
- Test 2 (30%): test2 * 0.3
- Internal / Assignment (50%): internal * 0.5

**Final = test_1 + test_2 + test_3**

If final >= 40, student qualifies for final examination.

## Tech Stack
- Python
- FastAPI
- Pydantic

## Installation

```bash
pip install -r requirements.txt
