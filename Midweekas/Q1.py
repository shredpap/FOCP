# An adventure game requires a player to enter their name. The name entered must
# starts with"Lord" or "Lady". Write a program that prompts the user to enter their
# name, and reports whether or not the name is acceptable. For example:
# Greetings! How shall we call you? Mr Apricot
# You may not be known by that name!
# Greetings! How shall we call you? Lord Derek
# It shall be so, Lord Derek!
name=input("Greetings! How shall we call you?").capitalize()
title=name.split()[0]
titles=["Lord","Lady"]
if title in titles:
    print(f"It shall be so, {name}")
else:
    print(f"You may not be known by that name!")