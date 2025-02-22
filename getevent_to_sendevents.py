with open ("sendevent.sh","w") as oFile:
	outputList =[]
	with open("getevent_input.txt","r") as File:
		for line in File:
			tmp = line.strip().split(" ")
			for i in range (1,4):
				tmp[i] = int((tmp[i]),16)
				tmp[0] = tmp[0].replace(":","")
			tmp.insert(0, "sendevent") 
			s = ' '.join(str(x) for x in tmp)
			oFile.writelines(s+"\n")