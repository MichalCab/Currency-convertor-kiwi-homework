#!/usr/bin/env python3

import forex_python.converter
import argparse
import json

parser = argparse.ArgumentParser(description='Currency converter')
parser.add_argument('-o', '--output_currency', type=str, help='requested/output currency - 3 letters name', default=None)
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('-a', '--amount', type=float, help='amount which we want to convert - float', required=True)
requiredNamed.add_argument('-i', '--input_currency', type=str, help='input currency - 3 letters name', required=True)

args= parser.parse_args()

c = forex_python.converter.CurrencyRates()
output= {}

if args.output_currency:
  output[args.output_currency]= c.convert(args.input_currency , args.output_currency, args.amount)
  
else:
  currencyDict= c.get_rates(args.input_currency)
  output= {key: value * args.amount for key, value in currencyDict.items()}
      

result={
        "input": { 
                  "amount": args.amount,
                  "currency": args.input_currency
        },
        
        "output": output
} 
        
print(json.dumps(result, indent=4))
