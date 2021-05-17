import sys
sys.path.append('../')

from sql import Sql
from quart import Quart
from template import Template

app = Quart(__name__)

@app.route('/reset')
async def reset():
    # sql = Sql()
    # sql.reset()
    return Template().buttonBackHome() + 'reset manuality'

@app.route('/')
async def main():
    sql = Sql()
    topIndicatorsCoins = sql.get_top_coin_indicators()

    content = Template().buttonReset()
    content += Template().topCoin(topIndicatorsCoins)
    return content

if __name__ == "__main__":
    app.run(host='0.0.0.0')
