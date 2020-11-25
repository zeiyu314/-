Target=open("tar2.py","r",encoding="utf-8").read();b=repr(Target)[1:][:-1].replace("\\n","\n").replace("    ","\t");open("product.py","w").write("exec("+repr(b)+")")
