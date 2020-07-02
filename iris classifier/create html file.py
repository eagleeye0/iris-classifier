title = '<title>Iris classifier</title>'
heading = '<body><h1>Enter features of iris plant</h1>'
form_start = '<form method="POST">'
form_end = '<input type="submit" name="predict"></form>'
page_end = "{{values}}<br/></body>"
with open('iris_features.txt','r') as file:
    t = file.readlines()
x = t[0].split(' ')[:-1]
y = t[1].split(' ')[:-1]
content = ''
for feature in x:
    content = content + '{}:<br/> <input type="text" name="{}"><br/><br/>'.format(feature,feature)

file = open('templates/index.html','w')
file.write(title)
file.write(heading)
file.write(form_start)
file.write(content)
file.write(form_end)
file.write(page_end)
file.close()
