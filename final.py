import itertools
import linecache
import collections
import re
import datetime

def get_details():
	filename = r"voice_data.pdf.txt"
		# The string that is to be searched
	key = "Voice"
	# Opening the file and storing its data into the variable lines
	with open(filename) as file:
		lines = file.readlines()
	# Going over each line of the file
	line_numbers = []
	for number, line in enumerate(lines, 1):
		# Condition true if the key exists in the line
		# If true then display the line number
		if key in line:
			line_numbers.append(number)
	start,end = line_numbers
	with open('voice_data.pdf.txt', 'r') as f:
		phone_number_list=[]
		call_duration_list = []
		for line in itertools.islice(f, start, end):
			start = start + 1
			x = re.search("^[0-9]{10,12}$", line)
			if x is not None:
				call_duration_list.append(linecache.getline('voice_data.pdf.txt',start+1).strip("\n"))
				phone_number_list.append(x.group())

		merged_list = [(phone_number_list[i], call_duration_list[i]) for i in range(0, len(phone_number_list))]
		Input = merged_list
		Output = []
		x=[]
		for i in Input:
			if i[0] not in x:
				x.append(i[0])
		for i in x:
			p=[]
			p.append(i)
			s=0
			for j in Input:
				if(j[0]==i):
					s+=int(j[1])
			p.append(s)
			Output.append(tuple(p))
		with open("results.csv", "w") as fr:
			dict_output = dict(Output)
			sorted_dict_output = sorted(dict_output.items(), key=lambda x:x[1], reverse=True)
			converted_dict_output = dict(sorted_dict_output)
			fr.write("phone_number,call_duration,no_of_times_called\n")
			freq = collections.Counter(phone_number_list)
			dic_freq_items = dict(freq.items())
			sorted_freq_items = sorted(dic_freq_items.items(), key=lambda x:x[1], reverse=True)
			dict_sorted_freq_items = dict(sorted_freq_items)
			for (key, value) in converted_dict_output.items():
				if key in dict_sorted_freq_items.keys():
					freq_value = str(datetime.timedelta(seconds = value))
					fr.write(f"{key},{freq_value},{dict_sorted_freq_items[key]}\n")