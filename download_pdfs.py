import csv, sys
import requests
import urllib
import os

filename = 'output_trim.csv'
with open(filename) as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            if 'sessions' in row[1]:
                course_name = row[0]
                if not os.path.exists(course_name):
                    os.makedirs(course_name)
            elif 'hbs' in row[4] and 'sessions' not in row[1]:
                print(row[5])
                #rev  = row[5][::-1]
                #i  = rev.index('/')
                #tmp = rev[0:i]
                #print(tmp[::-1])
                print(row[3])
                tmp = row[3].split(" : ")
                pdf_name = row[3].replace(tmp[0], "").replace(":", "").strip()
                # rq = urllib.request(row[0])
                if len(pdf_name) > 95:
                    pdf_name = pdf_name[:95]
                res = urllib.request.urlopen(row[5])
                if not os.path.exists("./" + course_name + "/" + pdf_name + ".pdf"):
                    pdf = open("./" + course_name + "/" + pdf_name + ".pdf", 'wb')
                    pdf.write(res.read())
                    pdf.close()
                else:
                    print("file: ", course_name + "/" + pdf_name + ".pdf", "already exist")
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
