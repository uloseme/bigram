import random
from collections import defaultdict
from PIL import Image, ImageDraw, ImageFont
from prettytable import PrettyTable
import matplotlib.pyplot as plt

def read_txt(file_path):
    with open(file_path, "r") as f:
        names = [name.strip().lower() for name in f.readlines()]
    return names

def counting(names):
    bigram_counts = defaultdict(int)
    for name in names:
        name = "^" + name + "$"
        for i in range(len(name)-1):
            bigram = name[i:i+2]
            bigram_counts[bigram] += 1
    return bigram_counts

def possibility(bigram_counts):
    total_count = sum(bigram_counts.values())
    bigram_probabilities = {}
    for bigram, count in bigram_counts.items():
        bigram_probabilities[bigram] = count / total_count
    return bigram_probabilities

def chose_name(probabilities):
    name = ""
    letter = random.choice(list(probabilities.keys()))[0]
    name += letter
    while True:
        possible_bigrams = [bigram for bigram in probabilities.keys() if bigram[0] == letter]
        if not possible_bigrams:
            break
        bigram_probabilities_list = [probabilities[bigram] for bigram in possible_bigrams]
        next_bigram = random.choices(possible_bigrams, weights=bigram_probabilities_list)[0]
        name += next_bigram[1]
        letter = next_bigram[1]
    return name


def bigram_in_console(probabilities):
    table = PrettyTable()
    table.field_names = ["Bigram", "Probability"]
    for bigram, probability in probabilities.items():
        table.add_row([bigram, "{:.2f}%".format(probability * 100)])
    print(table)

def bigram_in_graph(probabilities):
    fig, ax = plt.subplots()
    ax.bar(probabilities.keys(), probabilities.values())
    ax.set_xlabel('Bigram')
    ax.set_ylabel('Probability')
    ax.set_title('Bigram Probabilities')
    plt.xticks(rotation=90)
    plt.show()

def bigram_in_picture(probabilities):
    table_width = 600
    table_height = 50 + (len(probabilities) * 30)
    img = Image.new("RGB", (table_width, table_height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 16)

    draw.text((20, 20), "Bigram", font=font, fill=(0, 0, 0))
    draw.text((200, 20), "Probability", font=font, fill=(0, 0, 0))

    y_offset = 50
    for bigram, probability in probabilities.items():
        draw.text((20, y_offset), bigram, font=font, fill=(0, 0, 0))
        draw.text((200, y_offset), "{:.2f}%".format(probability*100), font=font, fill=(0, 0, 0))
        y_offset += 30

    img.show()  # Display the image (optional)
    img.save("bigram_table.png")  # Save the image to a file

names = read_txt("names.txt")

#Get bigram counts and probabilities
compute = counting(names)
probabilities = possibility(compute)

while(True):
        print("\n[1] Enter 1 to generate new Name.")
        print("[2] Enter 2 to get bigram probabilities in table.")
        print("[3] Enter 3 to get bigram probabilities in picture.")
        print("[4] Enter 4 to get bigram probabilities in graph.")
        print("[q] Enter q to quit.")
        select = input('Please enter a value: \n')
        if select == '1':
            # Step 3: Generate a name
            name = chose_name(probabilities)
            print("Generated name:", name)
        elif select == '2':
            # Visualize bigram probabilities with console
            bigram_in_console(probabilities)
        elif select == '3':
            # Visualize bigram probabilities with picture
            bigram_in_picture(probabilities)
        elif select == '4':
            # Visualize bigram probabilities with graph
            bigram_in_graph(probabilities)
        elif select == 'q':
            break



