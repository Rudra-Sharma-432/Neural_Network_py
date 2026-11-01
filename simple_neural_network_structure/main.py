class NeuralNetwork:
  def __init__(self, inputNeurons=1, hiddenLayersNeurons=[1], outputNeurons=1):
    self.inputNeurons = inputNeurons
    self.hiddenLayersNeurons = hiddenLayersNeurons
    self.hiddenLayers = len(hiddenLayersNeurons)
    self.outputNeurons = outputNeurons

  