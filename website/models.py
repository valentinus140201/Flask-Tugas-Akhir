from sklearn.svm import SVC

class SupportVectorMachine:
    def __init__(self, kernel, C, gamma, scaler):
        self.kernel = kernel
        self.gamma = gamma
        self.C = C
        self.scaler = scaler
        self.model = SVC(kernel=self.kernel, C=self.C, gamma=self.gamma)
        
    
    def fit(self, X, y):
        self.model.fit(X, y)
    
    def get_model(self):
        return self.model
    
    def scale(self, data):
        return self.scaler.transform([data])