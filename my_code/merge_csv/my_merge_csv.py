import csv

def merge_csv(csv_list, output_csv):
  #Combine filednames
  combinedfields = []
  for file in csv_list:
    with open(file, 'r') as f:
      #Read fieldnames from file
      reader = csv.DictReader(f).fieldnames
      #Add fieldnames to list, only add unique fieldnames
      combinedfields.extend(field for field in reader if field not in combinedfields)
  
  #Write to output file
  with open(output_csv, 'w') as outfile:
    #If fieldname does not exist, then use 'NA' as the replacement value
    writer = csv.DictWriter(outfile, fieldnames=combinedfields, restval='NA')
    #Write a row with the field names 
    writer.writeheader()
    for file in csv_list:
      with open(file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
          writer.writerow(row)

if __name__ == '__main__':
  merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')