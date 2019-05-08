import sys
if len(sys.argv) != 2:
	sys.exit("please input file_name:python query_workload.py file_name")
f = open(sys.argv[1], 'r')
wf = open('test.sql', 'w')
try:
	i = 0
	f.readline()
	f.readline()
	f.readline()
	while i < 10000:
		workload_line = f.readline()
		if workload_line:
			workload_line_list = workload_line.split("\t")
			command = workload_line_list[1].split()[1]
			if command == "Execute":
				wf.write(workload_line_list[2][:-1] + ';\n')
		else:
			break
		i = i + 1
finally:
	f.close()
	wf.close()
