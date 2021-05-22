def sort_by_date(filename):
	costs={}
	with open(filename) as f:
		header=f.readline()
		for line in f:
			date,city,cost,recommended = line.strip().split()
			cost= float(cost[1:])
			if 20.00 <= cost <= 50.00 and recommended =='Yes':
				costs[date] = line
			costs_sorted= sorted(costs.items(), key = lambda item:item[0], reverse=True)
	
	print(header, end='')
	for line in costs_sorted:
		print(str(line[1]), end='')

sort_by_date('city_cost.txt')