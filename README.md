## Flask Midtrans


### How to use:
```python
from flask_midtrans import Midtrans
from flask import Flask

# set environments
app = Flask(__name__)
app.config['MIDTRANS_IS_PRODUCTION'] = False
app.config['MIDTRANS_SERVER_KEY'] = 'SB-Mid-server-fRTQ4YyV5mVXB'
app.config['MIDTRANS_CLIENT_KEY'] = 'SB-Mid-client-hdv0voYgqK'

# instance
midtrans = Midtrans(app)

@app.route('/')
def hello_world():
    param = {
        "transaction_details": {
            "order_id": "test-transaction-123",
            "gross_amount": 200000
        }, "credit_card": {
            "secure": True
        }
    }

    # midtrans.snap or midtrans.core
    # https://github.com/Midtrans/midtrans-python-client
    response = midtrans.snap.create_transaction(param)
    
    # >> response
    #  {'token': 'thistoken', 'redirect_url': 'http://midtrans..'}
    return response['token']
```


### Contributes:
- agung96tm ( [github](https://github.com/agung96tm) | [website](https://agung96tm.com/) )
