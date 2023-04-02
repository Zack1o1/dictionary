from english_dictionary.scripts.read_pickle import get_dict
english_dict = get_dict()

def eng_dict():

    user_input = input("Enter a word:" )

    if user_input in english_dict:
        print(user_input, english_dict[user_input])
        query_user()

    else:
        print("\nInvalid input!\n")
        query_user()

def query_user():
    query = input("Continue?[y/n]: ")
    if 'y' in query:
        eng_dict()
    elif 'n' in query:
        print("Thank u for using!")
        quit()
    else:
        print("Invalid option")
        query_user()

eng_dict()
