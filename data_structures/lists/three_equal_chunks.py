'''
Given a list slice it into Three Equal Chunks and reverse each chunk.
'''

def three_chunks(p_list):
	chunk1 = []
	chunk2 = []
	chunk3 = []
	if len(p_list) % 3 == 0:
		divisor = len(p_list)/3
		divisor = int(divisor)
		for i in range(len(p_list)):
			chunk1.append(p_list[i])
			if i == divisor-1:
				break
		chunk1.reverse()
		for j in range(divisor, divisor + divisor):
			chunk2.append(p_list[j])
		chunk2.reverse()
		for k in range(divisor + divisor, divisor+divisor+divisor):
			chunk3.append(p_list[k])
		chunk3.reverse()
	else:
		print("This function won't work for this list")


	print(f"Chunk-1 = {chunk1}")
	print(f"Chunk-2 = {chunk2}")
	print(f"Chunk-3 = {chunk3}")
	

sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]
three_chunks(sample_list)