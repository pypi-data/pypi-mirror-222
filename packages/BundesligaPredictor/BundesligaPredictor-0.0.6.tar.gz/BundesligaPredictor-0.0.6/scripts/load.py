import pickle

def load_model():
	model = pickle.load(open('./model/model.pkl', 'rb'))

	return model