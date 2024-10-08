from js import document

# Function to count words
def count_words():
    # Get the text content from the HTML element with the new id 'reflectionContent'
    content1 = document.getElementById('reflectionContent1').textContent
    content2 = document.getElementById('reflectionContent2').textContent
    content3 = document.getElementById('reflectionContent3').textContent
    content4 = document.getElementById('reflectionContent4').textContent
    # Split the text by spaces
    words1 = content1.split()
    words2 = content2.split()
    words3 = content3.split()
    words4 = content4.split()
    # Get the number of words
    word_count1 = len(words1)
    word_count2 = len(words2)
    word_count3 = len(words3)
    word_count4 = len(words4)
    # Display the word count in the element with id 'wordCount'
    document.getElementById('wordCount').textContent = word_count1 + word_count2 +word_count3 + word_count4

# Call the word count function
count_words()