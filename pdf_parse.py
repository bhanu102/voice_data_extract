import fitz
import itertools
import collections
import linecache
import re
import final

doc = fitz.open("file2.pdf")


len = doc.page_count


'''The reason for including the range that starts at is 3 because the actual voice word
 will appear in 4th position in the document and end will be length of the document'''

# Get the page numbers that contains voice data
def get_page_number():
	page_numbers = []
	for page in doc.pages(3, len+1,1):
		areas = page.search_for("voice")
		if areas != []:
			page_numbers.append(page.number)
	a,b=page_numbers
	return get_voice_data_file(a,b)

# create a new voice data in seperate pdf file
def get_voice_data_file(start,end):
	doc2 = fitz.open()                 # new empty PDF
	doc2.insert_pdf(doc,from_page = start, to_page = end)  # copy intermediate voice data
	doc2.save("voice_data.pdf")

# get the text data
def get_text_data():
	fname = "voice_data.pdf"  # get document filename
	doc = fitz.open(fname)  # open document
	out = open(fname + ".txt", "wb")  # open text output
	for page in doc:  # iterate the document pages
		text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
		out.write(text)  # write text of page
		out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
	out.close()
	
if __name__ == "__main__":
	# get voice data file
	get_page_number()
	# get the text data from the voice data file
	get_text_data()
	# getting the final result
	final.get_details()