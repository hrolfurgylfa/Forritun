def geraSkraMedVeldum(skraarnafn,haestaVeli):
    skra = open(skraarnafn,"w")

    for veldi in range(0,haestaVeli+1):
        tala = pow(2,veldi)
        skra.write(str(tala)+str(","))
    
    skra.close()

geraSkraMedVeldum("Skra.txt",20)