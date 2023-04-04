#!/usr/bin/env bash

# Start Uvicorn with live reload
exec uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
