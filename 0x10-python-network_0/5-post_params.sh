#!/bin/bash
# Sends a POST request with specified parameters
curl -sX POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
