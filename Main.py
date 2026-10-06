import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# YouTube Inappropriate Content Detection - MCA Project
# Developed by Susmitha

def check_title(title):
    bad_words = ['abuse', 'violence', 'adult']
    for word in bad_words:
        if word in title.lower():
            return "Unsafe"
    return "Safe"

def main():
    print("YouTube Content Detection System")
    title = input("Enter video title: ")
    result = check_title(title)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
