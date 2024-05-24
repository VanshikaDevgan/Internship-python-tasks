def emoji_to_text(text_with_emojis):
    emoji_dict = {
        '🔥': ':fire:',
        '🚀': ':rocket:',
    }

    for emoji, text_rep in emoji_dict.items():
        text_with_emojis = text_with_emojis.replace(emoji, text_rep)

    return text_with_emojis

text_with_emojis = "I love 🔥 and 🚀️"
text_without_emojis = emoji_to_text(text_with_emojis)
print(text_without_emojis)
