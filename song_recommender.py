import tkinter as tk
import pandas as pd
import tkinter.font as font

# First part of YouTube video https://www.youtube.com/watch?v=_xf1TMs0ysk&t=185s&ab_channel=TinaHuang

# Create the main window
window = tk.Tk()
window.title("Song Recommender")
window.geometry("400x400")

window.configure(bg="#333")
window.resizable(False,False)

# Load the song data into a pandas DataFrame
songs_df = pd.read_csv("songs.csv")


def recommend_songs(mood):
    """
    Create a function to get song recommendations based on the user's mood
    :param mood: str
    :return:list
    """
    # Filter the DataFrame to only include songs with the specified mood
    filtered_df = songs_df[songs_df["mood"] == mood]

    # Return a list of the song titles and artists from the filtered DataFrame
    return list(filtered_df["title"] + " - " + filtered_df["artist"])


def show_recommendations():
    """
    Create a function to display the song recommendations when the user clicks the "Recommend" button
    :return:
    """
    # Get the user's mood from the mood_var StringVar
    mood = mood_var.get()

    # Use the recommend_songs function to get the song recommendations for the user's mood
    recommendations = recommend_songs(mood)

    # Clear the output field
    output_field.delete(1.0, tk.END)

    # Add the song recommendations to the output field
    for recommendation in recommendations:
        output_field.insert(tk.END, recommendation + "\n")


# Create a StringVar to hold the user's selected mood
mood_var = tk.StringVar()

# Create a font for the given texts
chosen_Font = font.Font(family='Times 20 italic bold',size=10)

# Create a label to prompt the user to select their mood
mood_label = tk.Label(window, text="Select your mood:",bg="#DEDEB8",)
mood_label['font'] = chosen_Font
mood_label.pack()

# Create a set of push buttons for the user to select their mood
hype_button = tk.Button(window, text="Hype", bg="#9797FF", command=lambda: mood_var.set("hype"))
hype_button['font'] = chosen_Font
hype_button.pack()

chill_button = tk.Button(window, text="Chill",bg="#E0E0FF" ,command=lambda: mood_var.set("chill"))
chill_button['font'] = chosen_Font
chill_button.pack()

nostalgic_button = tk.Button(window, text="Nostalgic",bg="#9797FF" ,command=lambda: mood_var.set("nostalgic"))
nostalgic_button['font'] = chosen_Font
nostalgic_button.pack()

# Create a button that the user can click to get song recommendations
recommend_button = tk.Button(window, text="Recommend",bg="#DEDEB8" ,command=show_recommendations)
recommend_button['font'] = chosen_Font
recommend_button.pack()

# Create an output field to display the song recommendations
output_field = tk.Text(window)
output_field.pack()
output_field.config(bg="#DEDEB8")
output_field['font'] = chosen_Font

# Run program
window.mainloop()
