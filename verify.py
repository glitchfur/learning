from sys import argv
from strictyaml import load, Map, Str, Int, YAMLError

schema = Map({"name": Str(), "abbr": Str(), "year": Int()})

fp = open(argv[1])

load(fp.read(), schema)
