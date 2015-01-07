# !/c/Python27/python
import fileinput

def assemble(output, rem_list):
	if not rem_list:
		return output
	if output == "":
		toAdd = max(rem_list, key=len)
		rem_list.remove(toAdd)
		return assemble(toAdd, rem_list)		
	max_overlap = 0
	toAdd = rem_list[0]
	for item in rem_list:
		curr_overlap = max(overlap(output, item), overlap(item, output))
		if curr_overlap >= max_overlap:
			max_overlap = curr_overlap
			toAdd = item
	if output[-max_overlap:] == toAdd[:max_overlap]:
		output = output + toAdd[max_overlap:]
	else:
		output = toAdd + output[max_overlap:]
	rem_list.remove(toAdd)
	return assemble(output, rem_list)

def overlap(s1, s2):
	if not s1 or not s2:
		return 0
	len1, len2 = len(s1), len(s2)		
	if len1 > len2:
		s1 = s1[-len2:]
	elif len2 > len1:
		s2 = s2[:len1]
	back = -1
	curr_overlap = 0
	while True:
		s2_idx = s2.find(s1[back:])
		if s2_idx == -1:
			return curr_overlap
		back -= s2_idx
		if s1[back:] == s2[:-back]:
			curr_overlap = -back
			back -= 1
			
if __name__ == "__main__":
	lst = []
	for line in fileinput.input():
		line = line.strip()
		if line not in lst:
			lst.append(line)
	toRemove = []
	for i in range(len(lst)):
		for j in range(i+1, len(lst)):
			if lst[i] == lst[j]:
				toRemove.append(lst[j])
			elif lst[i].find(lst[j]) != -1:
				toRemove.append(lst[j])
			elif lst[j].find(lst[i]) != -1:
				toRemove.append(lst[i])
	for i in set(toRemove):
		lst.remove(i)

	answer = assemble("", lst)
	print(answer)
	# print()
