#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 10:05:30 2024

@author: paigehoyer
"""
# I tried to do hangman for he last few weeks and it wasn't working at all so I switched to a much 
#less demanding number guesser but I am running into the same issue of streamlit auto matically creating a new game before the original had finished

#


# I tried to do hangman for he last few weeks and it wasn't working at all so I switched to a much 
#less demanding number guesser but I am running into the same issue of streamlit auto matically creating a new game before the original had finished

#I used streamlits video https://youtu.be/92jUAXBmZyU?list=TLGGYqrRVqMdT0wyMzA0MjAyNA about session state and base. It explains that session state is a way to share variables between reruns and abe to store and persist state.
#The article streamlit wrote about session state and sessions state https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
# sessions_state enhances the interactivity and user experience of Streamlit. It specifically allows you to store data in a way that even when/if the app reruns, the data will still be availble.
# specifically in my code this allows Streamlit to remember what number the user is trying to guess and not automatically reset every time a guess is submitted. 

import streamlit as st
import random

# Initialize variables
num_guesses = 0

# Set up Streamlit app title and slider for selecting highest number
st.title("Number Guessing Game")
highest_number = st.slider("Select the highest number to guess:", min_value=10, max_value=1000, value=10)

# Generate a random secret number between 1 and the highest number chosen by the user
secret_number = random.randint(1, highest_number)

# Welcome message and instructions for the user
st.write("Welcome to the Number Guessing Game!")
st.write(f"I'm thinking of a number between 1 and {highest_number}.")

# Check if 'secret_number' is already in session state, if not, add it
if "secret_number" not in st.session_state:
    st.session_state['secret_number'] = secret_number

# Check if 'num_guesses' is already in session state, if not, add it
if "num_guesses" not in st.session_state:
    st.session_state['num_guesses'] = num_guesses

# Input field for the user's guess
guess_value = st.number_input("Enter your guess:", min_value=1, max_value=highest_number, step=1, key="guess_input")

# Submit button
submit_button = st.button("Submit Guess")

# When the submit button is clicked
if submit_button:
    # Increment the number of guesses
    st.session_state['num_guesses'] += 1

    # Check if the guess is too high, too low, or correct
    if guess_value > st.session_state['secret_number']:
        st.write("Too high :(")
    elif guess_value < st.session_state['secret_number']:
        st.write("Too low :(")
    else:
        # If the guess is correct, display success message and number of guesses
        st.write("You guessed correctly!!! :)")
        st.write(f"It took you {st.session_state['num_guesses']} guesses.")

        # Open a file in append mode and write the game result to it
        with open("game_results.txt", "a") as file:
            file.write(f"Player guessed the number {st.session_state['secret_number']} in {st.session_state['num_guesses']} guesses.\n")

        # Clear session state for the next game
        for key in st.session_state.keys():
            st.session_state.pop(key)
            



#def play_guessing_game(secret_number, highest_number): er on youtube)