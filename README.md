# WebSocket Demo

A minimal WebSocket example with a **FastAPI** server and a **Python client** that echo messages back and forth.

## Overview

- **Server** (`websocket_demo.py`) — FastAPI app exposing a WebSocket at `/ws`. Accepts connections, sends a welcome message, then echoes every text message it receives.
- **Client** (`websocket_client.py`) — Connects to the server, lets you type messages in the terminal, and prints the server’s replies.

## Requirements

- Python 3.13+
- **Server:** FastAPI, uvicorn
- **Client:** `websockets`

## Installation

Using [uv](https://github.com/astral-sh/uv):

```bash
uv sync
```

For the client you also need the `websockets` library (add to `pyproject.toml` or install separately):

```bash
uv add websockets
```

Or with pip:

```bash
pip install fastapi uvicorn websockets
```

## Running

### 1. Start the server

```bash
python websocket_demo.py
```

Server runs at **http://localhost:8000**. The root path returns a short HTML message; the WebSocket endpoint is **ws://localhost:8000/ws**.

### 2. Run the client

In another terminal:

```bash
python websocket_client.py
```

- Type a message and press Enter to send it.
- The server echoes it back (e.g. `Message received: <your text>`).
- Press Enter with an empty line to exit.

## Endpoints

| Path   | Type       | Description                          |
|--------|------------|--------------------------------------|
| `GET /`  | HTTP       | Simple HTML: “Open a WebSocket at /ws” |
| `WS /ws` | WebSocket  | Echo server: sends back received text |

## Project structure

```
WebSocketDemo/
├── websocket_demo.py   # FastAPI WebSocket server
├── websocket_client.py # Interactive WebSocket client
├── pyproject.toml      # Project and dependencies (uv)
├── test_main.http      # HTTP test requests
└── README.md
```

## Quick test

1. `python websocket_demo.py` → leave it running.
2. `python websocket_client.py` → type e.g. `hello` → you should see `Server: Message received: hello`.
3. Empty Enter in the client to quit.
