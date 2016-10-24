def sed(pattern, rep, source, dest):
    try:
        fin = open(source)
        fout = open(dest, 'w')
        for line in fin:
            fout.write(line.replace(pattern, rep))
        fin.close()
        fout.close()
    except:
        print("There was an error of some sort.")

sed('tree','hammock','myfile.txt','myfile.txt.out')
