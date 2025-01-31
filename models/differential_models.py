

import numpy as np


def NSIR(self, y, t, beta, r, betan, alpha, rn, *args):
  """
  """

  S, I, In, R = y

  Sdot  = -S*(alpha*I + beta*In)/self.N
  Idot  =  S*(alpha*I + beta*In)/self.N - (r+betan) * I
  Indot = betan*I - rn*In
  Rdot  = rn*In + r*I

  return Sdot, Idot, Indot, Rdot


def SIR(self, y, t, parameters, *args):
  """
    The function that computes the diferential set of 
    equations of the SIR Epidemic Model.

    :param tuple y: Tuple with the suceptible and infected data.
    :param array t: The time respective to each y set of samples.
    :param float Beta: The Beta parameter.
    :param float r: The r parameter.

    :return: The derivative of the suceptible and infected data.
    :rtype: tuple
  """
  # Creating the simulation parameters
  if len(parameters) == 3:
    Beta = parameters[0] / (parameters[1] * parameters[2])
    r = 1 / parameters[1]
  else:
    Beta = parameters[0] / parameters[1]
    r = 1 / parameters[1]

  # Simulating the model
  if len(y) == 2:
    S, I = y
    Sdot = -Beta * S * I / self.N
    Idot = Beta * S * I / self.N  - r * I
    return Sdot, Idot

  if len(y) == 3:
    S, I, R = y
    Sdot = -Beta * S * I / self.N
    Idot = Beta * S * I / self.N - r * I 
    Rdot = r * I
    return Sdot, Idot, Rdot


def SEIR(self, y, t, Beta, r, sigma):
  """
    The function that computes the diferential set of 
    equations of the SEIR Epidemic Model.
    
    :param tuple y: Tuple with the suceptible and infected data.
    :param array t: The time respective to each y set of samples.
    :param float Beta: The Beta parameter.
    :param float r: The r parameter.
    :param float sigma: The sigma parameter.
    
    :return: The derivative of the suceptible and infected data.
    :rtype: tuple
  """

  S, E, I, R = y
  Sdot = -Beta * S * I / self.N
  Edot = Beta * S * I / self.N - sigma * E
  Idot = sigma * E  - r * I
  Rdot = r * I
  return Sdot, Edot, Idot, Rdot



def SIRD(self, y, t, parameters):
  """
  The function that computes the diferential set of 
  equations of the SIRD Epidemic Model.

  :param tuple y: Tuple with the suceptible and infected data.
  :param array t: The time respective to each y set of samples.
  :param float Beta: The Beta parameter.
  :param float r: The r parameter.
  :param float mi: The mi parameter.

  :return: The derivative of the suceptible and infected data.
  :rtype: tuple
  """
  
  if len(parameters) == 4:
    Ro, D, mu, pop = parameters
    Beta = Ro / (D * pop)
  else:
    Ro, D, mu = parameters
    Beta = Ro / D
  r = 1 / D

  S, I, R, D = y
  Sdot = -Beta * I * S / self.N
  Idot = Beta * I * S  / self.N - r * I - mu * I
  Rdot = r * I
  Ddot = mu* I
  return Sdot, Idot, Rdot, Ddot