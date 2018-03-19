#!flask/bin/python
from flask import Flask, make_response, jsonify, request
import forex_python.converter

app = Flask(__name__)

@app.route('/currency_converter', methods=['GET'])
def currency_converter():
  amount= request.args.get('amount', type = float)
  inputCurrency= request.args.get('input_currency')
  outputCurrency= request.args.get('output_currency', default = None)
  
  c = forex_python.converter.CurrencyRates()
  
  output= {}

  if outputCurrency:
    output[outputCurrency]= c.convert( inputCurrency, outputCurrency, amount)
    
  else:
    currencyDict= c.get_rates(inputCurrency)
    output= {key: value * amount for key, value in currencyDict.items()}

        

  result={
          "input": { 
                    "amount": amount,
                    "currency": inputCurrency
          },
          
          "output": output
  } 
  
  return jsonify(result)
  
if __name__ == '__main__':
    app.run(debug=True)