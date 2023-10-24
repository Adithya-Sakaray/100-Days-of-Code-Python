from tkinter import *
from tkinter import filedialog as fd
import PyPDF2
from gtts import gTTS

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"
global FILE_PATH, FILE_NAME


def openFile():
    # selecting the file using the askopenfilename() method of filedialog
    global FILE_PATH, FILE_NAME
    FILE_PATH = fd.askopenfilename(
        title="Select a file of any type",
        filetypes=[("Pdf", "*.pdf*")]
    )

    file_name = FILE_PATH.split("/")[-1]
    FILE_NAME = file_name.split(".")[0]

    file_label.config(text=file_name)
    file_label.grid(row=1, column=0)
    convert_button.grid(row=4, column=0)


def convert_to_audiofile():
    global FILE_PATH
    file_text = ""

    status_label = Label(text="Loading....", pady=10)
    status_label.grid(row=3, column=0)

    try:
        with open(FILE_PATH, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                file_text += page.extract_text()

        tts = gTTS(file_text, lang='en')
        tts.save(f"{FILE_NAME}.mp3")

        status_label = Label(text="Conversion successful. File saved successfully", pady=10, bg=YELLOW)
        status_label.grid(row=3, column=0)



    except Exception as e:
        print(f"An error occurred: {e}")
        return None


window = Tk()
window.title("PDF to audiobook converter")
window.config(pady=30, padx=30, bg=YELLOW)

main_label = Label(text="Select a PDF file to get it's audio version.", font=(FONT_NAME, 14, "normal"), bg=YELLOW,
                   fg=RED)
main_label.grid(row=0, column=0)

file_label = Label(text="", font=(FONT_NAME, 14, "normal"), bg=YELLOW, fg=GREEN, pady=20)
file_label.grid(row=1, column=0)

select_button = Button(text="Select PDF", command=openFile)
select_button.grid(row=2, column=0)

status_label = Label(text="", pady=10, bg=YELLOW)
status_label.grid(row=3, column=0)

convert_button = Button(text="Convert to audiobook", command=convert_to_audiofile)

window.mainloop()
