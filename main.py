from website import create_app
from website.models import SupportVectorMachine
from website.model_cotroller import ModelController
import pickle

app = create_app()

if __name__=='__main__':
    model = pickle.load(open("./website/model.pkl", "rb"))
    ModelController.add_element(model)
    app.run(debug=True)