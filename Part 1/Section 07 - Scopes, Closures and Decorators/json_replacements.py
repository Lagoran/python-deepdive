import fileinput

with fileinput.FileInput("json_text1", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace('"serviceType" : "YARN"','"serviceType" : "XXXX"'), end='')
        print(line.replace('"clusterDisplayName" : "Datalake_P01"', '"clusterDisplayName" : "XXX"'), end='')
        #print(line.replace('"serviceType" : "YARN"', '"serviceType" : "XXXX"'), end='')
        #print(line.replace('"serviceType" : "YARN"', '"serviceType" : "XXXX"'), end='')