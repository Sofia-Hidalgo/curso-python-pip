import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter= ';')
    header = next(reader) # devuelve el nombre de las columnas
    data = [] 
    for row in reader:
      ite = zip(header,row)
      country_dict = {key: value for key, value in ite} # convirtiendolo en un diccionario
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data)
  # print(data[0])


