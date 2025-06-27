def combine_and_iterate_texts():
    text1 = input("Enter first text: ")
    text2 = input("Enter second text: ")
    
    combined_text = text1 + text2
    char_list = [char for char in combined_text]
    
    print("Characters in combined text:", char_list)
    print("Thank you for using my application after processing the input.")
    
    return char_list

# Run it
combine_and_iterate_texts()
