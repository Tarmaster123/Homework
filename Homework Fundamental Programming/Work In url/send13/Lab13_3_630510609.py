#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab13_3
import string
def word_count(text):
	use = text.lower()
	cut = use.split()
	result = []
	keep = []
	print(cut)
	for i in cut:
		sp = i.strip()
		x = i.strip(string.punctuation)
		#use = x.lower()
		keep.append(x)
	for i in keep:
		count = keep.count(i)
		result.append((i,count))
	result = dict(result)
	return result

def main():
	text = "He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care."
	print(word_count(text))
	


if __name__ == "__main__":
	main()