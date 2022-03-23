#!/usr/bin/env bash
curl -X POST http://localhost:8000/simple/avg-list \
  -H 'Content-Type: application/json' \
  -d '{"values": [1, 2, 3, 4, 5]}' \
&& echo ""
