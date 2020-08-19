#!/bin/sh

run_tests() {
    pytest -sv tests/
}

run() {
    python app/ip_validator.py
}

#execute command
$1
