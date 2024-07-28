from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tkinter import *

# Function for clearing the contents of all entry boxes and text area.
def clearAll():
    negativeField.delete(0, END)
    neutralField.delete(0, END)
    positiveField.delete(0, END)
    overallField.delete(0, END)
    textArea.delete(1.0, END)

# Function to detect sentiment and update the GUI.
def detect_sentiment():
    # Get the whole input content from the text box.
    sentence = textArea.get("1.0", "end")
    
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
    
    # Get the sentiment scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
    
    # Update the fields with sentiment scores and corresponding emojis.
    negativeField.delete(0, END)
    neutralField.delete(0, END)
    positiveField.delete(0, END)
    overallField.delete(0, END)
    
    negativeField.insert(0, f"{sentiment_dict['neg']*100:.2f}% 😠 Negative")
    neutralField.insert(0, f"{sentiment_dict['neu']*100:.2f}% 😐 Neutral")
    positiveField.insert(0, f"{sentiment_dict['pos']*100:.2f}% 🙂 Positive")
    
    # Decide the overall sentiment.
    if sentiment_dict['compound'] >= 0.05:
        overallField.insert(0, "😊 Positive")
    elif sentiment_dict['compound'] <= -0.05:
        overallField.insert(0, "😠 Negative")
    else:
        overallField.insert(0, "😐 Neutral")

# Driver Code
if __name__ == "__main__":
    # Create a GUI window.
    gui = Tk()
    
    # Set the background color of the GUI window.
    gui.config(background="light green")
    
    # Set the name and size of the tkinter GUI window.
    gui.title("Sentiment Detector")
    gui.geometry("250x400")
    
    # Create and place widgets in the GUI window.
    enterText = Label(gui, text="Enter Your Sentence", bg="light green")
    textArea = Text(gui, height=5, width=25, font="lucida 13")
    check = Button(gui, text="Check Sentiment", fg="Black", bg="Red", command=detect_sentiment)
    
    negative = Label(gui, text="Negative Sentiment:", bg="light green")
    neutral = Label(gui, text="Neutral Sentiment:", bg="light green")
    positive = Label(gui, text="Positive Sentiment:", bg="light green")
    overall = Label(gui, text="Overall Sentiment:", bg="light green")
    
    negativeField = Entry(gui)
    neutralField = Entry(gui)
    positiveField = Entry(gui)
    overallField = Entry(gui)
    
    clear = Button(gui, text="Clear", fg="Black", bg="Red", command=clearAll)
    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=gui.quit)
    
    # Arrange widgets using grid method.
    enterText.grid(row=0, column=2)
    textArea.grid(row=1, column=2, padx=10, sticky=W)
    check.grid(row=2, column=2)
    negative.grid(row=3, column=2)
    neutral.grid(row=5, column=2)
    positive.grid(row=7, column=2)
    overall.grid(row=9, column=2)
    negativeField.grid(row=4, column=2)
    neutralField.grid(row=6, column=2)
    positiveField.grid(row=8, column=2)
    overallField.grid(row=10, column=2)
    clear.grid(row=11, column=2)
    Exit.grid(row=12, column=2)
    
    # Start the GUI main loop.
    gui.mainloop()
