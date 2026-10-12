import lifelib
r="b3s23-a5"
b=lifelib.load_rules(r)
lt=b.lifetree()
print("Loading config file for {}".format(r))
def load():
    with open("{}.ikebc".format(r), "r") as f:
        f=f.readlines()
        print("Config file loaded, {} lines".format(len(f)))
        l=[]
        tot=0
        for i in range(len(f)):
            h=[]
            g=lt.pattern(f[i].split(":")[1])
            p=g.period
            for j in range(4):
                for y in range(8):
                    for x in range(p):
                        cl=g.rle_string().splitlines()
                        cl=[i.strip()for i in cl]
                        cl="".join(cl[2:])
                        if cl not in h:
                            h.append(cl)
                            tot+=1
                        g=g[1]
                    g=g("rcw")
                g=g("flip_x") # works for obliques
            l.append([[i+1],h])
    print("Finished loading: {} orientations+phases total".format(tot))
    return l
#Plundered mostly STRAIGHT from Shinjuku since I didn't quite know how to approach this :money_mouth:
def extract(comp):
    res = lt.pattern()
    h=load()
    print(h)
    gliders=[lt.pattern(x) for x in h[0][1]]
    for block in zip(*[iter(gliders)]*4):
        salvo = sum((comp.match(g, halo="3o$3o$3o").convolve(g) for g in block), start=lt.pattern())
        res+=salvo
    return comp-res
print(extract(lt.pattern("""x = 41, y = 31, rule = B3/S23-a5
18b3o$18b3o$19bo10$35bo$34b3o$34b3o2$35bo2b2o$12b2o19b2obob3o$11bo2bo
18bobo2b2o$12b3o9b2o8b2o$23bo2bo$14b3o7b3o$14bo2bo$5b2o8b2o9b3o$b2o2b
obo18bo2bo$3obob2o19b2o$b2o2bo2$4b3o$4b3o$5bo!""")).rle_string())
#line format:
#orientation+source+timing>spaceship_id-orientation-x-y;spaceship_id2-orientation2-x2-y2;blah-blah-blah>target