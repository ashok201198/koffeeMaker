# koffeeMaker

A basic CafeMachineServer implemented in Python serving different drinks (ofcourse based on the inventory). 

To start it:
1. Clone the repository and setup a .json file with the following format as mentioned in testdata.json
2. Run main.py with giving the file path as input!!

Describing the testdata.json: 
```json
{
  "machine": {
    "outlets": {
      "count_n": "integer to denote the nozzles"
    },
    "total_items_quantity": {
      "item": "quantity"
    },
    "beverages": {
      "name": {
        "ingredient": "quantity"
      }
    }
}
```

