from PIL import Image
words = Image.open("D:/Users/sgade/PycharmProjects/QECCBATCHProject/word_matrix.png")


mask=Image.open("D:/Users/sgade/PycharmProjects/QECCBATCHProject/mask.png")
print(words.size)

mask = mask.resize((1015, 559))
print(mask.size)
mask.putalpha(200)
words.paste(mask, (0, 0), mask)
words.show()



