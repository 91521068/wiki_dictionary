import json
file = open("wikipedia_links.json","r")
links = []
c1s = []
c2s = []
c3s = []

d = json.loads(file.read())
for item in d['topics']:
	c2 = item['name']
	for j in item['subTopics']:
		links.append(j['link'])
		c3s.append(j['name'])
		c2s.append(c2)
		c1s.append("")

for i in links:
	print "'" + i + "',"

print "\n"

for i in c3s:
	print "'" + i + "',"

print "\n"

for i in c2s:
	print "'" + i + "',"

print "\n"

for i in c1s:
	print "'" + i + "',"

print "\n"
print len(links)
file.close()
