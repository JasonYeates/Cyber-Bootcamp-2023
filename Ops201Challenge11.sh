#!/bin/bash
# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated

echo "How is your day?"
read response
case "$response" in
    "good")
        echo "Thats awesome!!!!"
        ;;
    "bad")
        echo "Thats not awesome."
        ;;
    *)
        echo "Invalid response"
        ;;
esac