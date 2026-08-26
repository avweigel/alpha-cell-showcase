#!/bin/bash
# Starts a tiny local web server and opens the showcase.
# Needed because browsers block 3D-model loading from a double-clicked file.
cd "$(dirname "$0")"
PORT=8765
if ! lsof -i :$PORT >/dev/null 2>&1; then
  python3 -m http.server $PORT >/dev/null 2>&1 &
  sleep 1
fi
open "http://localhost:$PORT"
