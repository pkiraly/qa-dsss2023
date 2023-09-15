validating a simple array

```
python3 main.py --schema simple-array.schema.json --instances simple-array.json
```

fixed list (`enum`) of values

```
python3 main.py --schema dog.schema.json --instances dog.json
```

with `required`:

```
python3 main.py --schema dog.schema2.json --instances dog.json
```


dependentRequired:

```
python3 main.py --schema dependentRequired.schema.json --instances dependentRequired.json
```

anyOf

```
python3 main.py --schema anyof.schema.json --instances anyof1.json
python3 main.py --schema anyof.schema.json --instances anyof2.json
python3 main.py --schema anyof.schema.json --instances anyof3.json
```

oneOf

```
python3 main.py --schema oneof.schema.json --instances oneof1.json
python3 main.py --schema oneof.schema.json --instances oneof2.json
python3 main.py --schema oneof.schema.json --instances oneof3.json
```

a complex example:

```
python3 main.py --schema persons.schema.json --instances persons.json
```
