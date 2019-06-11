linear = {('x0','x0'): -1, ('x1','x1'): -1, ('x2','x2'): -3}
quadratic = {('x0', 'x1'): 2, ('x0', 'x2'): 2, ('x1', 'x2'): 2}
 
Q = dict(linear)
Q.update(quadratic)
"""
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
response = EmbeddingComposite(DWaveSampler()).sample_qubo(Q, num_reads=1000)

for sample, energy, num_occurrences, chain_break_fraction in list(response.data()):
	    print(sample, "Energy: ", energy, "Occurrences: ", num_occurrences)
"""
import dimod

b = dimod.BinaryQuadraticModel.from_qubo(Q, 0.0)
r = dimod.SimulatedAnnealingSampler().sample(b)
for sample, energy, num_occurrences in r.data(['sample','energy','num_occurrences']):
	    print(sample, "Energy: ", energy, "Occurrences: ", num_occurrences)

