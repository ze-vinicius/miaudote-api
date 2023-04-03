#!/usr/bin/env bash


# Start uvicorn
exec uvicorn app.main:app --reload
